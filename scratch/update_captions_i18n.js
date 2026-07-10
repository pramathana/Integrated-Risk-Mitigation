const fs = require('fs');
let c = fs.readFileSync('index.html', 'utf8');

const captions = {
  en: {
    caption_doughnut_before: 'Distribution of the 11 risk threats based on severity level before mitigation is applied.',
    caption_bar_before: 'Count of mapped threats across the 5 architectural layers of the Zero Trust defense model before mitigation.',
    caption_sankey_before: 'Mapping of the 11 priority threats to ISO 27005 risk events, asset targets, and COBIT 2019 governance weaknesses before mitigation.',
    caption_doughnut_after: 'Distribution of the 11 risk threats based on severity level after the Zero Trust mitigation program is applied.',
    caption_bar_after: 'Count of mapped threats across the 5 architectural layers of the Zero Trust defense model after mitigation.',
    caption_sankey_after: 'Mapping of the 11 priority threats to ISO 27005 risk events, asset targets, and COBIT 2019 governance weaknesses after mitigation.'
  },
  id: {
    caption_doughnut_before: 'Distribusi 11 ancaman risiko berdasarkan tingkat keparahan sebelum mitigasi diterapkan.',
    caption_bar_before: 'Jumlah ancaman yang terpetakan pada 5 lapisan arsitektur model pertahanan Zero Trust sebelum mitigasi.',
    caption_sankey_before: 'Pemetaan 11 ancaman prioritas terhadap peristiwa risiko ISO 27005, target aset, dan kelemahan tata kelola COBIT 2019 sebelum mitigasi.',
    caption_doughnut_after: 'Distribusi 11 ancaman risiko berdasarkan tingkat keparahan setelah program mitigasi Zero Trust diterapkan.',
    caption_bar_after: 'Jumlah ancaman yang terpetakan pada 5 lapisan arsitektur model pertahanan Zero Trust setelah mitigasi.',
    caption_sankey_after: 'Pemetaan 11 ancaman prioritas terhadap peristiwa risiko ISO 27005, target aset, dan kelemahan tata kelola COBIT 2019 setelah mitigasi.'
  }
};

for (const lang of Object.keys(captions)) {
  const cap = captions[lang];
  let injectStr = '';
  for (const key of Object.keys(cap)) {
    injectStr += `\n        "${key}": "${cap[key]}",`;
  }
  
  // Inject into const translations = { lang: { ... } }
  // We can look for the first key in the lang block, e.g., "nav_research" or similar.
  // Wait, the safest way is to find `lang: {` inside `const translations` block.
  
  const regex = new RegExp(`(const translations\\s*=[\\s\\S]*?\\s+${lang}:\\s*\\{)`);
  c = c.replace(regex, `$1${injectStr}`);
}

fs.writeFileSync('index.html', c);
console.log('Captions injected successfully.');
