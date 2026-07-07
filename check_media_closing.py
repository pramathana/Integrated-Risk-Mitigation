import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Check for media queries involving closing-grid
for match in re.finditer(r'@media[^{]*\{[^\}]*\.closing-grid[^\}]*\}[^\}]*\}', content):
    print("Media query closing-grid:", match.group(0))

for match in re.finditer(r'@media\s*\([^)]+\)\s*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', content):
    if '.closing-grid' in match.group(0):
        print("Found in media query:", match.group(0))
