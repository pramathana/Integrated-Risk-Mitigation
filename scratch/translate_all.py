import json
import re
from deep_translator import GoogleTranslator

# 9 Languages to translate to
LANGUAGES = ['id', 'zh', 'es', 'fr', 'de', 'ar', 'ru', 'ko', 'ja']

# Google Translator uses standard codes, some might differ slightly from the JS codes.
# JS codes -> Google Translator codes
LANG_MAP = {
    'id': 'id', # Indonesian
    'zh': 'zh-CN', # Chinese (Simplified)
    'es': 'es', # Spanish
    'fr': 'fr', # French
    'de': 'de', # German
    'ar': 'ar', # Arabic
    'ru': 'ru', # Russian
    'ko': 'ko', # Korean
    'ja': 'ja'  # Japanese
}

# The keys we need to translate from EN to other languages
KEYS_TO_TRANSLATE = [
    "widget_title", "widget_filter_all", "widget_filter_changes", 
    "widget_filter_nochanges", "widget_filter_high", "widget_filter_relevant",
    "expert_notes_title", "fgd_title", "control_change_title",
    "PRE-CONTROLS", "POST-CONTROLS", "Nothing Changes", "widget_no_changes_req",
    "t10_notes", "t10_fgd", "t11_notes", "t11_fgd", "t09_notes", "t09_fgd",
    "t04_notes", "t04_fgd", "t02_notes", "t02_fgd", "t03_notes", "t03_fgd",
    "t05_notes", "t05_fgd", "t08_notes", "t08_fgd", "t01_notes", "t01_fgd",
    "t06_notes", "t06_fgd"
]

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print("Failed to read index.html:", e)
        return

    # 1. Extract EN object
    en_match = re.search(r'en:\s*\{([^}]*?\"widget_title\".*?)\}', content, re.DOTALL)
    if not en_match:
        print("Could not find en object or the injected keys.")
        return
        
    en_content = en_match.group(1)
    
    # Simple regex parser to get key-values from the en object
    en_dict = {}
    for key in KEYS_TO_TRANSLATE:
        # Match "key": "value"
        pattern = fr'"{key}"\s*:\s*"(.*?)"\s*(?:,|\n)'
        m = re.search(pattern, en_content)
        if m:
            en_dict[key] = m.group(1)
        else:
            print(f"Warning: Key {key} not found in en object.")
            
    print(f"Extracted {len(en_dict)} keys from English source.")

    # 2. Translate and inject for each language
    for lang in LANGUAGES:
        print(f"Processing language: {lang}")
        translator = GoogleTranslator(source='en', target=LANG_MAP[lang])
        
        translated_block = ""
        for key, val in en_dict.items():
            if not val or val == "-":
                translated_val = val
            else:
                try:
                    translated_val = translator.translate(val)
                    # Escape quotes
                    if translated_val:
                        translated_val = translated_val.replace('"', '\\"')
                except Exception as e:
                    print(f"Error translating {key} to {lang}: {e}")
                    translated_val = val
            
            translated_block += f'        "{key}": "{translated_val}",\n'
            
        # Find the language block in content and inject
        lang_pattern = re.compile(fr'({lang}:\s*{{)')
        m = lang_pattern.search(content)
        if m:
            insert_pos = m.end()
            content = content[:insert_pos] + '\n' + translated_block + content[insert_pos:]
            print(f"Successfully injected translations into {lang} block.")
        else:
            print(f"Warning: Could not find block for language {lang}")
            
    # 3. Write back to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("All translations complete!")

if __name__ == '__main__':
    main()
