import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

pub_match = re.search(r'<div id="view-publications".*?</p>\s*</div>', content, re.DOTALL)
if pub_match:
    print("PUB:\n", pub_match.group(0))

eval_match = re.search(r'<div id="view-evaluation".*?<div id="evaluation-widget-container"></div>', content, re.DOTALL)
if eval_match:
    print("EVAL:\n", eval_match.group(0))
