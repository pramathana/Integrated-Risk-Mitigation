const fs = require('fs');

let content = fs.readFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', 'utf8');

const oldT = `    function t(key) {
      const lang = (typeof currentLang !== 'undefined') ? currentLang : 'en';
      if (translations[key] && translations[key][lang]) {
        return translations[key][lang];
      }
      return translations[key] ? translations[key]['en'] : key;
    }`;

const newT = `    function t(key) {
      const lang = (typeof currentLang !== 'undefined') ? currentLang : 'en';
      if (translations[lang] && translations[lang][key]) {
        return translations[lang][key];
      }
      if (translations['en'] && translations['en'][key]) {
        return translations['en'][key];
      }
      return key;
    }`;

if (content.includes(oldT)) {
    content = content.replace(oldT, newT);
    fs.writeFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', content, 'utf8');
    console.log("Translation function fixed!");
} else {
    console.log("Could not find the old translation function.");
}
