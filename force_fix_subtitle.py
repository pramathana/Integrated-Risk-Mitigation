import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Instead of regex that might fail, I'll just use string replacement or a very broad regex.
# Let's find all blocks that look like `.pub-subtitle { ... }`
content = re.sub(r'\.pub-subtitle\s*\{[^}]*\}', '', content)
content = re.sub(r'\[data-theme="light"\]\s*\.pub-subtitle\s*\{[^}]*\}', '', content)

# Now, add them back cleanly at the end of the style block
clean_rules = """
    .pub-subtitle {
      color: #38bdf8 !important;
    }

    [data-theme="light"] .pub-subtitle {
      color: #00629B !important;
    }
"""

content = content.replace("</style>", clean_rules + "\n  </style>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Properly replaced .pub-subtitle CSS.")
