with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'function switchView' in line:
        for j in range(i, i+30):
            print(f"{j+1}: {lines[j].strip()}")
        break
