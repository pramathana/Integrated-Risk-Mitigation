import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# fetch CSS for .pub-subtitle
matches = re.finditer(r'\.pub-subtitle\s*\{[^}]*\}', content)
for m in matches:
    print("CSS:", m.group(0))

matches_light = re.finditer(r'\[data-theme="light"\]\s*\.pub-subtitle\s*\{[^}]*\}', content)
for m in matches_light:
    print("LIGHT CSS:", m.group(0))

# fetch the HTML where pub-subtitle is used
match_html = re.search(r'<h3 class="pub-subtitle"[^>]*>.*?</h3>', content, re.DOTALL)
if match_html:
    print("HTML:", match_html.group(0))
