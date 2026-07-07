import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# fetch the entire CSS block
match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if match:
    css = match.group(1)
    if "view-publications" in css or "view-evaluation" in css:
        for line in css.split("\n"):
            if "view-publications" in line or "view-evaluation" in line:
                print(line.strip())
