const fs = require('fs');
const path = require('path');

const targetFile = path.resolve(__dirname, '../index.html');
let content = fs.readFileSync(targetFile, 'utf8');

// The incorrect injection inserted literal backslashes and n's: \\n
// Let's replace the specific broken sequences.
content = content.replace(/\\n        "comparison_title"/g, '\n        "comparison_title"');
content = content.replace(/",\\n        "comparison/g, '",\n        "comparison');
content = content.replace(/",\\n        "btn_view_comparison/g, '",\n        "btn_view_comparison');
content = content.replace(/>",\\n/g, '",\n');

fs.writeFileSync(targetFile, content, 'utf8');
console.log("Fixed syntax errors");
