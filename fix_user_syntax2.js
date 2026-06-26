const fs = require('fs');
const file = 'c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html';
let content = fs.readFileSync(file, 'utf8');

// 1. Remove the extra closing brace using regex
content = content.replace(/}\s*}\s*}\s*function renderEvaluationGrid/g, '} \n    }\n\n    function renderEvaluationGrid');

fs.writeFileSync(file, content, 'utf8');
console.log("Syntax errors fixed with regex!");
