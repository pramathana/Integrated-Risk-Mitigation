const fs = require('fs');
const filePath = 'index.html';
let content = fs.readFileSync(filePath, 'utf8');

const prefix = '<!doctype html>\r\n';
const prefix2 = '<!doctype html>\n';

let actualPrefix = content.startsWith(prefix) ? prefix : (content.startsWith(prefix2) ? prefix2 : '');
if (!actualPrefix) {
    console.log("Could not find DOCTYPE prefix.");
    process.exit(1);
}

const headIndex = content.indexOf('<head>');
if (headIndex === -1) {
    console.log("Could not find <head>");
    process.exit(1);
}

const newContent = actualPrefix + '<html lang="en">\r\n\r\n' + content.slice(headIndex);
fs.writeFileSync(filePath, newContent, 'utf8');
console.log("Fixed HTML head!");
