import sys
import re
import json

try:
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    print('Failed to read:', e)
    sys.exit(1)

# 1. Fix the t() function
old_t = '''function t(key) {
      const lang = (typeof currentLang !== 'undefined') ? currentLang : 'en';
      if (translations[key] && translations[key][lang]) {
        return translations[key][lang];
      }
      return translations[key] ? translations[key]['en'] : key;
    }'''

new_t = '''function t(key) {
      const lang = (typeof currentLang !== 'undefined') ? currentLang : 'en';
      if (translations[lang] && translations[lang][key]) {
        return translations[lang][key];
      }
      return translations['en'] && translations['en'][key] ? translations['en'][key] : key;
    }'''

if old_t in content:
    content = content.replace(old_t, new_t)
    print('Replaced t() function')
else:
    print('WARNING: old t() function not found exactly as expected, attempting regex')
    t_pattern = re.compile(r'function t\(key\) \{.*?\return translations\[key\] \? translations\[key\]\[\'en\'\] : key;\s*\}', re.DOTALL)
    if t_pattern.search(content):
        content = t_pattern.sub(new_t, content)
        print('Replaced t() function via regex')
    else:
        print('Failed to find t() function to replace')

# 2. Add keys to translations.en
injection_block = '''
        "widget_title": "Expert Notes & Focus Group Discussion (FGD) Results",
        "widget_filter_all": "All",
        "widget_filter_changes": "Changes",
        "widget_filter_nochanges": "No Changes",
        "widget_filter_high": "Highly Relevant",
        "widget_filter_relevant": "Relevant",
        "expert_notes_title": "Expert Notes",
        "fgd_title": "FGD Discussion Content",
        "control_change_title": "Control Change Results",
        "PRE-CONTROLS": "PRE-CONTROLS",
        "POST-CONTROLS": "POST-CONTROLS",
        "Nothing Changes": "Nothing Changes",
        "widget_no_changes_req": "Nothing Changes",
'''

en_match = re.search(r'en:\s*\{', content)
if en_match:
    insert_pos = en_match.end()
    content = content[:insert_pos] + '\n' + injection_block + content[insert_pos:]
    print('Injected base keys into translations.en')
else:
    print('Failed to find en: { block')

# 3. Extract and replace long texts in getEvaluationData
eval_data_pattern = re.compile(r'id:\s*"(T\.\d+)",.*?expertNotes:\s*t\("(.*?)"\),.*?fgd:\s*t\("(.*?)"\)', re.DOTALL)

matches = eval_data_pattern.findall(content)
print(f'Found {len(matches)} threat items in getEvaluationData')

dynamic_keys_injection = ''

for match in matches:
    t_id = match[0] # e.g., T.10
    key_prefix = t_id.lower().replace('.', '') # e.g., t10
    
    notes_val = match[1]
    fgd_val = match[2]
    
    notes_key = f"{key_prefix}_notes"
    fgd_key = f"{key_prefix}_fgd"
    
    # Escape quotes inside the values if they exist, to safely place in JSON-like structure
    safe_notes_val = notes_val.replace('"', '\\"')
    safe_fgd_val = fgd_val.replace('"', '\\"')
    
    dynamic_keys_injection += f'        "{notes_key}": "{safe_notes_val}",\n'
    dynamic_keys_injection += f'        "{fgd_key}": "{safe_fgd_val}",\n'
    
    # Replace in content
    # We must be careful because notes_val contains exact matched strings with possible regex chars
    old_notes_str = f'expertNotes: t("{notes_val}")'
    new_notes_str = f'expertNotes: t("{notes_key}")'
    content = content.replace(old_notes_str, new_notes_str)
    
    old_fgd_str = f'fgd: t("{fgd_val}")'
    new_fgd_str = f'fgd: t("{fgd_key}")'
    content = content.replace(old_fgd_str, new_fgd_str)

if dynamic_keys_injection:
    en_match = re.search(r'en:\s*\{', content)
    if en_match:
        insert_pos = en_match.end()
        content = content[:insert_pos] + '\n' + dynamic_keys_injection + content[insert_pos:]
        print('Injected dynamic keys into translations.en')

# 4. Update hardcoded text in HTML strings to use t()
html_replacements = [
    ('<h4>Expert Notes</h4>', '<h4>${t(\'expert_notes_title\')}</h4>'),
    ('<h4>FGD Discussion Content</h4>', '<h4>${t(\'fgd_title\')}</h4>'),
    ('<h4>Control Change Results</h4>', '<h4>${t(\'control_change_title\')}</h4>')
]

for old_str, new_str in html_replacements:
    if old_str in content:
        content = content.replace(old_str, new_str)
        print(f'Replaced {old_str}')
    else:
        print(f'Failed to find {old_str}')
        
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Update complete.')
