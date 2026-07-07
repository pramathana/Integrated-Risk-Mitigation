import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# get pub header box style
pub_match = re.search(r'<div\s+style="([^"]+)">\s*<h2[^>]*>\s*Related Publications', content)
if pub_match:
    print("PUB HEADER STYLE:", pub_match.group(1))

# get eval-widget CSS
eval_match = re.search(r'\.eval-widget\s*\{([^}]*)\}', content)
if eval_match:
    print("EVAL CSS:", eval_match.group(1))
