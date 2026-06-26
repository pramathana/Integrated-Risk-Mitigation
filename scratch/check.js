const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const regex = /<script>([\s\S]*?)<\/script>/g;
let match;
let scripts = [];
while ((match = regex.exec(html)) !== null) {
  scripts.push(match[1]);
}
fs.writeFileSync('temp.js', scripts.join('\n'));
try {
  require('vm').Script(scripts.join('\n'));
  console.log("Syntax is OK!");
} catch (e) {
  console.error("Syntax Error:", e);
}
