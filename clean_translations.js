const fs = require('fs');

let content = fs.readFileSync('evalDataTarget.txt', 'utf8');

let braceCount = 0;
let endIndex = -1;
let started = false;
for (let i = 0; i < content.length; i++) {
    if (content[i] === '[') { braceCount++; started = true; }
    else if (content[i] === ']') { braceCount--; }
    
    if (started && braceCount === 0) {
        endIndex = i;
        break;
    }
}

let arrayStr = content.substring(0, endIndex + 1);
arrayStr = arrayStr.replace('const evaluationData = ', '').trim();

// Clean up weird characters BEFORE parsing
arrayStr = arrayStr
    .replace(/\?o/g, '\\"')
    .replace(/\?\?/g, '\\"')
    .replace(/\?T/g, "\\'")
    .replace(/\?~/g, '\\"')
    .replace(/\+'/g, "->")
    .replace(/A/g, "|")
    

let evalData;
try {
    evalData = eval('(' + arrayStr + ')');
} catch (e) {
    console.log("Eval failed, trying to fix syntax", e);
}

if (evalData) {
    let output = '';
    evalData.forEach(item => {
        let key = item.id.replace('T.', 't').toLowerCase();
        let notes = item.expertNotes.replace(/"/g, '\\"').replace(/\n/g, '<br>');
        let fgd = item.fgd.replace(/"/g, '\\"').replace(/\n/g, '<br>');
        
        output += '    translations.en.' + key + '_notes = "' + notes + '";\n';
        output += '    translations.en.' + key + '_fgd = "' + fgd + '";\n\n';
    });
    
    fs.writeFileSync('translations_cleaned.txt', output);
    console.log('Cleaned translations generated!');
}
