import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

pub = re.search(r'<div id="view-publications"(.*?)<div class="pub-grid">', content, re.DOTALL)
if pub: print(pub.group(1).strip())
