import re
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()
matches = re.finditer(r'pub-grid', content)
for m in matches:
    start = max(0, m.start() - 50)
    end = min(len(content), m.end() + 150)
    print("MATCH:\n", content[start:end])
