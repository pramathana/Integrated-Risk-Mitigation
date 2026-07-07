with open("index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
in_style = False
skip = False
for line in lines:
    if "<style>" in line:
        in_style = True
    if "</style>" in line:
        in_style = False
    
    if in_style and (".pub-subtitle {" in line or '[data-theme="light"] .pub-subtitle {' in line or '[data-theme="light"] \n\n  \n    .pub-subtitle {' in line):
        skip = True
        
    if not skip:
        new_lines.append(line)
        
    if skip and "}" in line:
        skip = False

# Insert the clean ones before </style>
for i, line in enumerate(new_lines):
    if "</style>" in line:
        clean_rules = """
    .pub-subtitle {
      color: #38bdf8 !important;
    }

    [data-theme="light"] .pub-subtitle {
      color: #00629B !important;
    }
"""
        new_lines.insert(i, clean_rules)
        break

with open("index.html", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Robustly fixed .pub-subtitle!")
