import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any variation with the correct exact filename
content = re.sub(r'\]\([^)]*5[^)]*ZTA[^)]*\.png\)', '](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Forced all ZTA image paths to 5%20Layer%20ZTA%20PNG%20BAG.drawio.png")
