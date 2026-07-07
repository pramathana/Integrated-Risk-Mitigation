import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'\*\s*\{[^}]*\}', content)
if match:
    print(match.group(0))
