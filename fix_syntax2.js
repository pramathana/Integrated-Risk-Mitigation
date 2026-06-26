const fs = require('fs');
const file = 'c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html';
let content = fs.readFileSync(file, 'utf8');

// The exact string to replace is a literal backslash followed by n, standing alone on a line
content = content.replace(/\r?\n\\n\r?\n/g, '\n\n');

// Also check if there's any remaining literal \n that shouldn't be there
// But ONLY at the start of lines:
content = content.replace(/^\\n$/gm, '');

fs.writeFileSync(file, content, 'utf8');
console.log("Fixed isolated \\n syntax errors!");
