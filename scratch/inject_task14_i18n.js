const fs = require('fs');
const path = require('path');

const targetFile = path.resolve(__dirname, '../index.html');
let content = fs.readFileSync(targetFile, 'utf8');

// First, remove the dynamic injection we added earlier
const dynamicBlockStart = "// Add Comparison translations dynamically";
const dynamicBlockEnd = "    const homeTransl = {";
if (content.includes(dynamicBlockStart)) {
  const startIdx = content.indexOf(dynamicBlockStart);
  const endIdx = content.indexOf(dynamicBlockEnd);
  if (startIdx !== -1 && endIdx !== -1) {
    content = content.substring(0, startIdx) + content.substring(endIdx);
  }
}

const transData = {
  zh: {
    comparison_title: "缓解前后比较",
    comparison_before_label: "缓解前",
    comparison_before_desc: "所有架构层的总威胁。",
    comparison_after_label: "缓解后",
    comparison_after_desc: "应用零信任后的剩余威胁。",
    btn_view_comparison: "查看完整比较 <i class=\"ph ph-arrow-right\"></i>"
  },
  es: {
    comparison_title: "Comparación antes vs después de la mitigación",
    comparison_before_label: "Antes de la mitigación",
    comparison_before_desc: "Amenazas totales en todas las capas arquitectónicas.",
    comparison_after_label: "Después de la mitigación",
    comparison_after_desc: "Amenazas restantes después de aplicar Zero Trust.",
    btn_view_comparison: "Ver comparación completa <i class=\"ph ph-arrow-right\"></i>"
  },
  fr: {
    comparison_title: "Comparaison avant et après atténuation",
    comparison_before_label: "Avant atténuation",
    comparison_before_desc: "Menaces totales sur toutes les couches architecturales.",
    comparison_after_label: "Après atténuation",
    comparison_after_desc: "Menaces restantes après l'application du Zero Trust.",
    btn_view_comparison: "Voir la comparaison complète <i class=\"ph ph-arrow-right\"></i>"
  },
  de: {
    comparison_title: "Vergleich vor vs. nach der Minderung",
    comparison_before_label: "Vor der Minderung",
    comparison_before_desc: "Gesamte Bedrohungen über alle Architekturschichten hinweg.",
    comparison_after_label: "Nach der Minderung",
    comparison_after_desc: "Verbleibende Bedrohungen nach Anwendung von Zero Trust.",
    btn_view_comparison: "Vollständigen Vergleich anzeigen <i class=\"ph ph-arrow-right\"></i>"
  },
  ar: {
    comparison_title: "مقارنة قبل وبعد التخفيف",
    comparison_before_label: "قبل التخفيف",
    comparison_before_desc: "إجمالي التهديدات عبر جميع الطبقات المعمارية.",
    comparison_after_label: "بعد التخفيف",
    comparison_after_desc: "التهديدات المتبقية بعد تطبيق نهج انعدام الثقة (Zero Trust).",
    btn_view_comparison: "عرض المقارنة الكاملة <i class=\"ph ph-arrow-right\"></i>"
  },
  ru: {
    comparison_title: "Сравнение до и после смягчения",
    comparison_before_label: "До смягчения",
    comparison_before_desc: "Общее количество угроз на всех архитектурных уровнях.",
    comparison_after_label: "После смягчения",
    comparison_after_desc: "Оставшиеся угрозы после применения Zero Trust.",
    btn_view_comparison: "Посмотреть полное сравнение <i class=\"ph ph-arrow-right\"></i>"
  },
  ko: {
    comparison_title: "완화 이전 대 이후 비교",
    comparison_before_label: "완화 이전",
    comparison_before_desc: "모든 아키텍처 계층에 걸친 총 위협.",
    comparison_after_label: "완화 이후",
    comparison_after_desc: "제로 트러스트 적용 후 남은 위협.",
    btn_view_comparison: "전체 비교 보기 <i class=\"ph ph-arrow-right\"></i>"
  },
  ja: {
    comparison_title: "緩和策の前後比較",
    comparison_before_label: "緩和前",
    comparison_before_desc: "すべてのアーキテクチャ層全体での総脅威。",
    comparison_after_label: "緩和後",
    comparison_after_desc: "ゼロトラスト適用後の残存脅威。",
    btn_view_comparison: "完全な比較を表示 <i class=\"ph ph-arrow-right\"></i>"
  }
};

let contentBeforeHomeTransl = content;
let contentAfterHomeTransl = "";
const homeTranslIndex = content.indexOf("const homeTransl");
if (homeTranslIndex !== -1) {
  contentBeforeHomeTransl = content.substring(0, homeTranslIndex);
  contentAfterHomeTransl = content.substring(homeTranslIndex);
}

for (const lang of Object.keys(transData)) {
  const marker = "      " + lang + ": {";
  const insertIndex = contentBeforeHomeTransl.indexOf(marker);
  if (insertIndex !== -1) {
    let insertStr = "";
    for (const [k, v] of Object.entries(transData[lang])) {
      insertStr += '        "' + k + '": ' + JSON.stringify(v) + ',\\n';
    }
    
    if (!contentBeforeHomeTransl.includes('"comparison_title": ' + JSON.stringify(transData[lang].comparison_title))) {
      const braceIndex = contentBeforeHomeTransl.indexOf('{', insertIndex);
      contentBeforeHomeTransl = contentBeforeHomeTransl.substring(0, braceIndex + 1) + '\\n' + insertStr + contentBeforeHomeTransl.substring(braceIndex + 1);
    }
  } else {
    console.log("Could not find block for " + lang);
  }
}

fs.writeFileSync(targetFile, contentBeforeHomeTransl + contentAfterHomeTransl, 'utf8');
console.log("Done");
