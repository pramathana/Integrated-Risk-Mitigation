import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("md-content CSS:")
match = re.search(r'\.md-content\s*\{[^}]*\}', content)
if match: print(match.group(0))

print("view-evaluation CSS:")
match = re.search(r'\#view-evaluation\s*\{[^}]*\}', content)
if match: print(match.group(0))
