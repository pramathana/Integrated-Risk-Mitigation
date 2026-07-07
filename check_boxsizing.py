import re
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()
if "box-sizing: border-box" in content:
    print("Has box-sizing reset.")
else:
    print("NO box-sizing reset found.")
