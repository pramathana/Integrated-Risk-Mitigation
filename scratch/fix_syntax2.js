const fs = require('fs');
const path = require('path');

const targetFile = path.resolve(__dirname, '../index.html');
let content = fs.readFileSync(targetFile, 'utf8');

content = content.replace(/<\/i",/g, '</i>",');

fs.writeFileSync(targetFile, content, 'utf8');
console.log("Fixed missing >");
