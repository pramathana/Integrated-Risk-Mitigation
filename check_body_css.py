import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'body\s*\{[^}]*\}', content)
if match:
    print("body:\n", match.group(0))
