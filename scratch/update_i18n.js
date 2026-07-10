const fs = require('fs');
let c = fs.readFileSync('index.html', 'utf8');

const t = {
  en: '🌐 Available in 10 Languages',
  id: '🌐 Tersedia dalam 10 Bahasa',
  zh: '🌐 提供 10 种语言',
  es: '🌐 Disponible en 10 idiomas',
  fr: '🌐 Disponible en 10 langues',
  de: '🌐 Verfügbar in 10 Sprachen',
  ar: '🌐 متوفر بـ 10 لغات',
  ru: '🌐 Доступно на 10 языках',
  ko: '🌐 10개 언어 지원',
  ja: '🌐 10言語で利用可能'
};

for (const [l, text] of Object.entries(t)) {
  const regex = new RegExp('(' + l + ':\\s*\\{[\\s\\S]*?"menu_home":\\s*".*?",)');
  c = c.replace(regex, `$1\n        "badge_languages": "${text}",`);
}
fs.writeFileSync('index.html', c);
console.log('Translations updated.');
