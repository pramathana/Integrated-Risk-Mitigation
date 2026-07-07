import re

with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "Conclusion" in line or "Recommendation" in line:
        start = max(0, i-5)
        end = min(len(lines), i+6)
        print(f"MATCH AT LINE {i+1}:")
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
        break
