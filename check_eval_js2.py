import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# grab initEvaluationWidget
match = re.search(r'function initEvaluationWidget\(\)\s*\{(.*?)\}', content, re.DOTALL)
if match:
    # check if there's any style being applied to container or widget
    js = match.group(1)
    if "style" in js:
        # print lines with style
        for line in js.split("\n"):
            if "style" in line:
                print(line.strip())
