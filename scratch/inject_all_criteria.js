const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, '../index.html');
let content = fs.readFileSync(filePath, 'utf8');

const getDict = (scriptPath, dictName) => {
  const code = fs.readFileSync(scriptPath, 'utf8');
  const startStr = `const ${dictName} = {`;
  const startIndex = code.indexOf(startStr);
  const vm = require('vm');
  const sandbox = {};
  const codeToRun = code.substring(startIndex, code.indexOf('};', startIndex) + 2) + `\n this.${dictName} = ${dictName};`;
  vm.createContext(sandbox);
  vm.runInContext(codeToRun, sandbox);
  return sandbox[dictName];
}

const likelihoodTranslations = getDict(path.resolve(__dirname, 'translate_likelihood.js'), 'likelihoodTranslations');
const impactTranslations = getDict(path.resolve(__dirname, 'translate_impact.js'), 'impactTranslations');
const riskLevelTranslations = getDict(path.resolve(__dirname, 'translate_risk.js'), 'riskLevelTranslations');

// Find boundaries using regex
const criteriaMatch = content.match(/criteria:\s*\{([\s\S]+?)\},\r?\n\s*assessment:\s*\{/);

if (!criteriaMatch) {
    throw new Error("Could not find criteria block via regex.");
}

const criteriaStr = "{" + criteriaMatch[1] + "}";

// Extract en and id
const enMatch = criteriaStr.match(/"en":\s*"([\s\S]*?)"(?=\n\s*,\s*"id"|\r?\n\s*\})/);
const idMatch = criteriaStr.match(/"id":\s*"([\s\S]*?)"(?=\n\s*,\s*"|(?:\r?\n\s*\}))/);

const newCriteria = {
  en: enMatch[1].replace(/\\n/g, '\n').replace(/\\"/g, '"'),
  id: idMatch[1].replace(/\\n/g, '\n').replace(/\\"/g, '"')
};

const langs = ['zh', 'es', 'fr', 'de', 'ar', 'ru', 'ko', 'ja'];

for (const lang of langs) {
  let fullString = likelihoodTranslations[lang];
  fullString += '\\n\\n---\\n\\n';
  fullString += impactTranslations[lang];
  fullString += '\\n\\n---\\n\\n';
  fullString += riskLevelTranslations[lang];
  
  fullString = fullString.replace(/\\n---\\n---\\n/g, '\\n---\\n');
  fullString = fullString.replace(/\\n---\\n\\n---\\n/g, '\\n---\\n');
  
  let parsedFullString = likelihoodTranslations[lang] + '\n\n---\n\n' + impactTranslations[lang] + '\n\n---\n\n' + riskLevelTranslations[lang];
  
  newCriteria[lang] = parsedFullString;
}

const newCriteriaStr = "criteria: " + JSON.stringify(newCriteria, null, 8).replace(/\n/g, '\n      ') + ",\n      assessment: {";
const newContent = content.replace(criteriaMatch[0], newCriteriaStr);

fs.writeFileSync(filePath, newContent, 'utf8');
console.log("Successfully injected all 10 languages into criteria!");
