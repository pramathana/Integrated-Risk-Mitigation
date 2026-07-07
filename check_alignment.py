import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# check closing-grid and closing-card css again
match = re.search(r'\.closing-grid\s*\{[^}]*\}', content)
if match: print("closing-grid CSS:\n", match.group(0))

# check eval-grid and eval-card CSS
match = re.search(r'\.eval-grid\s*\{[^}]*\}', content)
if match: print("eval-grid CSS:\n", match.group(0))
