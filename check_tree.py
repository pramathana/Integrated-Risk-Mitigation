import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Let's extract the exact DOM tree from dashboard-container down
match = re.search(r'<div class="dashboard-container">(.*?)</body>', content, re.DOTALL)
if match:
    sub = match.group(1)
    # just print the top level div ids
    divs = re.findall(r'<div id="([^"]+)"', sub)
    print("Divs:", divs)
