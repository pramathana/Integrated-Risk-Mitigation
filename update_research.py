import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the image name
content = content.replace('The%205-Layer%20Zero%20Trust%20Defense%20Model.png', '5%20Layer%20ZTA%20PNG.png')
content = content.replace('The 5-Layer Zero Trust Defense Model.png', '5 Layer ZTA PNG.png')

# Add the CSS for #md-research
css_injection = """
    #md-research p,
    #md-research ul,
    #md-research ol,
    #md-research li,
    #md-research td,
    #md-research th,
    #md-research blockquote {
      color: #fff !important;
    }
  </style>"""

content = content.replace('  </style>', css_injection)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced image paths and added CSS.")
