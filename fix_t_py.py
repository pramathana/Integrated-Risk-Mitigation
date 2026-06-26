import re

with open('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r"function t\(key\) \{[\s\S]*?return translations\[key\] \? translations\[key\]\['en'\] : key;\s*\}"

replacement = """function t(key) {
      const lang = (typeof currentLang !== 'undefined') ? currentLang : 'en';
      if (translations[lang] && translations[lang][key]) {
        return translations[lang][key];
      }
      if (translations['en'] && translations['en'][key]) {
        return translations['en'][key];
      }
      return key;
    }"""

if re.search(pattern, content):
    content = re.sub(pattern, replacement, content)
    with open('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Not found")
