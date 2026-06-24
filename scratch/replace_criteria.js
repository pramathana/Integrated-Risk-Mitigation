const fs = require('fs');
const filePath = 'index.html';
let content = fs.readFileSync(filePath, 'utf8');

// The original file has:
//     const embeddedMarkdown = {
//       criteria:
//         "# Likelihood Criteria...
//       assessment: {

const startIndex = content.indexOf('    const embeddedMarkdown = {\r\n      criteria:\r\n        "# Likelihood Criteria');
if (startIndex === -1) {
  const startIndex2 = content.indexOf('    const embeddedMarkdown = {\n      criteria:\n        "# Likelihood Criteria');
  if (startIndex2 === -1) {
      console.log("Could not find start index.");
      process.exit(1);
  }
}

const assessmentIndex = content.indexOf('      assessment: {');
if (assessmentIndex === -1) {
  console.log("Could not find assessment index.");
  process.exit(1);
}

// Find exactly where "      criteria:\n        \"# Likelihood..." begins.
const criteriaPropStart = content.indexOf('      criteria:\r\n', startIndex) !== -1 ? content.indexOf('      criteria:\r\n', startIndex) : content.indexOf('      criteria:\n', startIndex);

// We replace everything between criteriaPropStart and assessmentIndex
const replacement = fs.readFileSync('scratch/criteria_out.txt', 'utf8') + '\r\n';

const newContent = content.slice(0, criteriaPropStart) + '      ' + replacement + content.slice(assessmentIndex);

fs.writeFileSync(filePath, newContent, 'utf8');
console.log("Replaced successfully!");
