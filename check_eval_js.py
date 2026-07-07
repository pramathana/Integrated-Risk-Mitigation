import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r'function initEvaluationWidget\(\)\s*\{[^}]*\}', content)
if match:
    print(match.group(0)[:500])
