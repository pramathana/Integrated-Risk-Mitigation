const fs = require('fs');

const content = fs.readFileSync('evalDataTarget.txt', 'utf8');
const startIndex = content.indexOf('const evaluationData = [');

let braceCount = 0;
let endIndex = -1;
let started = false;
for (let i = startIndex; i < content.length; i++) {
    if (content[i] === '[') { braceCount++; started = true; }
    else if (content[i] === ']') { braceCount--; }
    
    if (started && braceCount === 0) {
        endIndex = i;
        break;
    }
}

if (endIndex !== -1) {
    const arrayContent = content.substring(startIndex, endIndex + 1);
    fs.writeFileSync('evalDataTargetArray.js', arrayContent);
    console.log('Saved to evalDataTargetArray.js');
} else {
    console.log('End not found');
}
