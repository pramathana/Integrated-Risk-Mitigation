const fs = require('fs');
let c = fs.readFileSync('index.html', 'utf8');

const t_lang = {
  en: 'Available in 10 Languages',
  id: 'Tersedia dalam 10 Bahasa',
  zh: '提供 10 种语言',
  es: 'Disponible en 10 idiomas',
  fr: 'Disponible en 10 langues',
  de: 'Verfügbar in 10 Sprachen',
  ar: 'متوفر بـ 10 لغات',
  ru: 'Доступно на 10 языках',
  ko: '10개 언어 지원',
  ja: '10言語で利用可能'
};

const t_watermark = {
  en: 'Telkom University - 2026',
  id: 'Universitas Telkom - 2026',
  zh: 'Telkom 大学 - 2026',
  es: 'Universidad Telkom - 2026',
  fr: 'Université Telkom - 2026',
  de: 'Telkom Universität - 2026',
  ar: 'جامعة تيلكوم - 2026',
  ru: 'Университет Telkom - 2026',
  ko: '텔콤 대학교 - 2026',
  ja: 'テルコム大学 - 2026'
};

// Replace inside homeTransl
for (const lang of Object.keys(t_lang)) {
  const regex = new RegExp(`(homeTransl\\s*=[\\s\\S]*?\\s+${lang}:\\s*\\{[\\s\\S]*?menu_home:\\s*"[^"]*",)`);
  c = c.replace(regex, `$1\n        badge_languages: "${t_lang[lang]}",\n        badge_watermark: "${t_watermark[lang]}",`);
}

// Replace inside translations
for (const lang of Object.keys(t_lang)) {
  const regex = new RegExp(`(const translations\\s*=[\\s\\S]*?\\s+${lang}:\\s*\\{[\\s\\S]*?"menu_home":\\s*"[^"]*",)`);
  c = c.replace(regex, `$1\n        "badge_languages": "${t_lang[lang]}",\n        "badge_watermark": "${t_watermark[lang]}",`);
}

fs.writeFileSync('index.html', c);
console.log('Keys injected successfully.');
