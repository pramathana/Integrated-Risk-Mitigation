import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to remove the extra text inside the 'en' string that was added by mistake.
# The 'en' string has: | 🔴 20 |\n\",\n        \"id\": \"# Kriteria ... | 🔴 20 |\n",
# We will use a regex to fix it.
# The criteria object starts with:
# criteria: {
#   "en": "... | 🔴 20 |\n\",\n        \"id\": \"# Kriteria ... | 🔴 20 |\n",

# The correct string for 'en' should end at | 🔴 20 |\n",
# Wait, the literal text to replace is:
# \\",\\n        \\"id\\": \\"# Kriteria Kemungkinan, Kriteria Dampak, dan Kriteria Tingkat Risiko\\n\\n## 1. Skala Kemungkinan
# Wait, no. The whole duplicated text is exactly the 'id' text but with escaped quotes.
# Actually, let's just find the exact line 3650 and replace it.
lines = content.split('\n')
for i, line in enumerate(lines):
    if line.startswith('        "en": "# Likelihood Criteria'):
        # This line is the bad line.
        # Find where the English text should end:
        # It ends right after | 🔴 20 |\n
        match = re.search(r'(\| 🔴 20 \|\\n)\\",\\n\s+\\"id\\": \\"# Kriteria.*?\| 🔴 20 \|\\n",', line)
        if match:
            # Replace the match with just the correct end of the string
            lines[i] = line[:match.start()] + match.group(1) + '",'
            print('Fixed line!')
        else:
            print('Could not find the exact pattern in the line.')
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
