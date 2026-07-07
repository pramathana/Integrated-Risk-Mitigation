import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'<div id="view-evaluation"[^>]*>.*?</div>', content, re.DOTALL)
if match:
    # Print the parent elements up to the widget container
    print(match.group(0)[:500])
