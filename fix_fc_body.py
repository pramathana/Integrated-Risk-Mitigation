file_path = "c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<p class="fc-body">', '<p class="fc-body" data-i18n="ack_fam_body">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done fixing fc-body")
