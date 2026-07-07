import re

file_path = "c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML
content = re.sub(
    r'<h3 class="sup-name">\s*Ibu\s*(Widyatasya.*?)</h3>',
    r'<h3 class="sup-name"><span data-i18n="ack_title_ibu">Ibu</span> \1</h3>',
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<h3 class="sup-name">\s*Bapak\s*(Dhata.*?)</h3>',
    r'<h3 class="sup-name"><span data-i18n="ack_title_bapak">Bapak</span> \1</h3>',
    content,
    flags=re.DOTALL
)

# 2. Add translations
translations = {
    'en': {
        'ack_title_ibu': 'Mrs.',
        'ack_title_bapak': 'Mr.'
    },
    'id': {
        'ack_title_ibu': 'Ibu',
        'ack_title_bapak': 'Bapak'
    },
    'es': {
        'ack_title_ibu': 'Sra.',
        'ack_title_bapak': 'Sr.'
    },
    'fr': {
        'ack_title_ibu': 'Mme',
        'ack_title_bapak': 'M.'
    },
    'de': {
        'ack_title_ibu': 'Frau',
        'ack_title_bapak': 'Herr'
    },
    'zh': {
        'ack_title_ibu': '女士',
        'ack_title_bapak': '先生'
    },
    'ja': {
        'ack_title_ibu': 'Ms.',
        'ack_title_bapak': 'Mr.'
    },
    'ko': {
        'ack_title_ibu': 'Ms.',
        'ack_title_bapak': 'Mr.'
    },
    'ar': {
        'ack_title_ibu': 'السيدة',
        'ack_title_bapak': 'السيد'
    },
    'ru': {
        'ack_title_ibu': 'Г-жа',
        'ack_title_bapak': 'Г-н'
    }
}

for lang, trans_dict in translations.items():
    entries_str = ""
    for k, v in trans_dict.items():
        val = v.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", " ")
        entries_str += f'          "{k}": "{val}",\n'
    
    # Inject into content right after the language key
    pattern = r'(' + lang + r':\s*\{)'
    replacement = r'\1\n' + entries_str
    content = re.sub(pattern, replacement, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done translating titles")
