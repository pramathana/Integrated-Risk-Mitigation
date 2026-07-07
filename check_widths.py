import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("view-evaluation HTML:")
match = re.search(r'<div id="view-evaluation"[^>]*>', content)
if match: print(match.group(0))

print("view-publications HTML:")
match = re.search(r'<div id="view-publications"[^>]*>', content)
if match: print(match.group(0))

print("eval-widget css:")
match = re.search(r'\.eval-widget\s*\{[^}]*\}', content)
if match: print(match.group(0))

print("pub-grid css:")
match = re.search(r'\.pub-grid\s*\{[^}]*\}', content)
if match: print(match.group(0))
