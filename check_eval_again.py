import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'\.eval-widget\s*\{[^}]*\}', content)
if match:
    print("EVAL-WIDGET:\n", match.group(0))

# Also check for any other css rules affecting view-evaluation
match = re.search(r'\#view-evaluation\s*\{[^}]*\}', content)
if match: print("VIEW-EVAL:", match.group(0))
