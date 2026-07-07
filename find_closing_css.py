import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find closing-title and closing-card css rules
for match in re.finditer(r'\.closing-title\s*\{[^}]*\}', content):
    print("Match:", match.group(0))

for match in re.finditer(r'\.closing-card\s*\{[^}]*\}', content):
    print("Match:", match.group(0))
