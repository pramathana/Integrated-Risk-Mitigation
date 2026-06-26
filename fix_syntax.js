const fs = require('fs');
const file = 'c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html';
let content = fs.readFileSync(file, 'utf8');

// 1. Fix the \n syntax error
content = content.replace(/";\\n\s*translations\.en\.t10_title/g, '";\n    translations.en.t10_title');

fs.writeFileSync(file, content, 'utf8');
console.log("Fixed \\n syntax error!");
