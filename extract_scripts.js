const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Extract all scripts
const scriptRegex = /<script>([\s\S]*?)<\/script>/g;
let match;
let count = 0;
while ((match = scriptRegex.exec(html)) !== null) {
  const scriptContent = match[1];
  fs.writeFileSync(`temp_script_${count}.js`, scriptContent);
  count++;
}
console.log(`Extracted ${count} scripts.`);
