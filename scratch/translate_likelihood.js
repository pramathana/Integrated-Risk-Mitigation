const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, '../index.html');
let content = fs.readFileSync(filePath, 'utf8');

const likelihoodTranslations = {
  "id": `## 1. Skala Kemungkinan
**Sumber:** ISO 27005:2022 & Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI)

| Skala | Kategori | Deskripsi |
|:---:|---|---|
| **1** | Tidak Mungkin | • Risiko sangat kecil kemungkinannya untuk terjadi, paling banyak setahun sekali<br>• Frekuensi kejadian < 0.1% per tahun<br>• Probabilitas risiko terjadi antara 0% dan 19% |
| **2** | Agak Tidak Mungkin | • Risiko jarang terjadi, mungkin hanya dua kali setahun<br>• Frekuensi kejadian dari 0.1% hingga 1% per tahun<br>• Probabilitas risiko terjadi antara 20% dan 39% |
| **3** | Mungkin | • Risiko telah terjadi tetapi tidak sering; itu terjadi tiga kali setahun<br>• Frekuensi kejadian antara 1% dan 1.5% per tahun<br>• Probabilitas risiko terjadi antara 40% dan 59% |
| **4** | Sangat Mungkin | • Risiko sering terjadi, enam kali setahun<br>• Frekuensi kejadian antara 1.5% dan 2% per tahun<br>• Probabilitas kejadian antara 60% dan 79% |
| **5** | Hampir Pasti | • Risiko selalu terjadi, terjadi dua belas kali setahun<br>• Frekuensi kejadian dari 2% hingga 5% per tahun<br>• Probabilitas kejadian antara 80% dan 100% |

---`,
  "zh": `## 1. 可能性等级
**来源:** ISO 27005:2022 & DetereCo 内部程序（IT 风险管理实施）

| 等级 | 类别 | 描述 |
|:---:|---|---|
| **1** | 不太可能 | • 风险发生的可能性极小，最多每年一次<br>• 发生频率 < 0.1% 每年<br>• 风险发生概率在 0% 到 19% 之间 |
| **2** | 较不可能 | • 风险很少发生，可能每年只有两次<br>• 发生频率从 0.1% 到 1% 每年<br>• 风险发生概率在 20% 到 39% 之间 |
| **3** | 可能 | • 风险已发生但不频繁；每年发生三次<br>• 发生频率在 1% 到 1.5% 每年<br>• 风险发生概率在 40% 到 59% 之间 |
| **4** | 很有可能 | • 风险经常发生，每年六次<br>• 发生频率在 1.5% 到 2% 每年<br>• 发生概率在 60% 到 79% 之间 |
| **5** | 几乎确定 | • 风险总是发生，每年发生十二次<br>• 发生频率从 2% 到 5% 每年<br>• 发生概率在 80% 到 100% 之间 |

---`,
  "es": `## 1. Escala de Probabilidad
**Fuente:** ISO 27005:2022 & Procedimientos Internos de DetereCo (Implementación de Gestión de Riesgos de TI)

| Escala | Categoría | Descripción |
|:---:|---|---|
| **1** | Improbable | • El riesgo es muy improbable que ocurra, como máximo una vez al año<br>• Frecuencia de ocurrencia < 0.1% por año<br>• Probabilidad de que el riesgo ocurra entre 0% y 19% |
| **2** | Poco Probable | • El riesgo ocurre raramente, quizás solo dos veces al año<br>• Frecuencia de ocurrencia del 0.1% al 1% por año<br>• Probabilidad de que el riesgo ocurra entre 20% y 39% |
| **3** | Probable | • El riesgo ha ocurrido pero no frecuentemente; ocurre tres veces al año<br>• Frecuencia de ocurrencia entre 1% y 1.5% por año<br>• Probabilidad de que el riesgo ocurra entre 40% y 59% |
| **4** | Muy Probable | • El riesgo ocurre frecuentemente, seis veces al año<br>• Frecuencia de ocurrencia entre 1.5% y 2% por año<br>• Probabilidad de ocurrencia entre 60% y 79% |
| **5** | Casi Seguro | • El riesgo siempre ocurre, sucediendo doce veces al año<br>• Frecuencia de ocurrencia del 2% al 5% por año<br>• Probabilidad de ocurrencia entre 80% y 100% |

---`,
  "fr": `## 1. Échelle de Probabilité
**Source:** ISO 27005:2022 & Procédures Internes de DetereCo (Mise en Œuvre de la Gestion des Risques Informatiques)

| Échelle | Catégorie | Description |
|:---:|---|---|
| **1** | Improbable | • Il est très peu probable que le risque se produise, au plus une fois par an<br>• Fréquence d'occurrence < 0.1% par an<br>• Probabilité d'occurrence du risque entre 0% et 19% |
| **2** | Peu Probable | • Le risque se produit rarement, peut-être seulement deux fois par an<br>• Fréquence d'occurrence de 0.1% à 1% par an<br>• Probabilité d'occurrence du risque entre 20% et 39% |
| **3** | Probable | • Le risque s'est produit mais pas fréquemment ; il se produit trois fois par an<br>• Fréquence d'occurrence entre 1% et 1.5% par an<br>• Probabilité d'occurrence du risque entre 40% et 59% |
| **4** | Très Probable | • Le risque se produit fréquemment, six fois par an<br>• Fréquence d'occurrence entre 1.5% et 2% par an<br>• Probabilité d'occurrence entre 60% et 79% |
| **5** | Presque Certain | • Le risque se produit toujours, arrivant douze fois par an<br>• Fréquence d'occurrence de 2% à 5% par an<br>• Probabilité d'occurrence entre 80% et 100% |

---`,
  "de": `## 1. Wahrscheinlichkeitsskala
**Quelle:** ISO 27005:2022 & Interne Verfahren von DetereCo (Implementierung des IT-Risikomanagements)

| Skala | Kategorie | Beschreibung |
|:---:|---|---|
| **1** | Unwahrscheinlich | • Das Risiko tritt sehr unwahrscheinlich ein, höchstens einmal im Jahr<br>• Eintrittshäufigkeit < 0.1% pro Jahr<br>• Eintrittswahrscheinlichkeit des Risikos zwischen 0% und 19% |
| **2** | Eher Unwahrscheinlich | • Das Risiko tritt selten auf, vielleicht nur zweimal im Jahr<br>• Eintrittshäufigkeit von 0.1% bis 1% pro Jahr<br>• Eintrittswahrscheinlichkeit des Risikos zwischen 20% und 39% |
| **3** | Wahrscheinlich | • Das Risiko ist aufgetreten, aber nicht häufig; es tritt dreimal im Jahr auf<br>• Eintrittshäufigkeit liegt zwischen 1% und 1.5% pro Jahr<br>• Eintrittswahrscheinlichkeit des Risikos liegt zwischen 40% und 59% |
| **4** | Sehr Wahrscheinlich | • Das Risiko tritt häufig auf, sechsmal im Jahr<br>• Eintrittshäufigkeit liegt zwischen 1.5% und 2% pro Jahr<br>• Eintrittswahrscheinlichkeit zwischen 60% und 79% |
| **5** | Fast Sicher | • Das Risiko tritt immer auf, zwölfmal im Jahr<br>• Eintrittshäufigkeit von 2% bis 5% pro Jahr<br>• Eintrittswahrscheinlichkeit zwischen 80% und 100% |

---`,
  "ar": `## 1. مقياس الاحتمالية
**المصدر:** ISO 27005:2022 & الإجراءات الداخلية لشركة DetereCo (تنفيذ إدارة مخاطر تكنولوجيا المعلومات)

| المقياس | الفئة | الوصف |
|:---:|---|---|
| **1** | غير محتمل | • من غير المحتمل جدا أن يحدث الخطر، على الأكثر مرة واحدة في السنة<br>• وتيرة الحدوث < 0.1% سنويا<br>• احتمالية حدوث الخطر بين 0% و 19% |
| **2** | غير محتمل نوعا ما | • يحدث الخطر نادرا، ربما مرتين فقط في السنة<br>• وتيرة الحدوث من 0.1% إلى 1% سنويا<br>• احتمالية حدوث الخطر بين 20% و 39% |
| **3** | محتمل | • حدث الخطر ولكن ليس بشكل متكرر؛ يحدث ثلاث مرات في السنة<br>• وتيرة الحدوث بين 1% و 1.5% سنويا<br>• احتمالية حدوث الخطر بين 40% و 59% |
| **4** | محتمل جدا | • يحدث الخطر بشكل متكرر، ست مرات في السنة<br>• وتيرة الحدوث بين 1.5% و 2% سنويا<br>• احتمالية الحدوث بين 60% و 79% |
| **5** | شبه مؤكد | • يحدث الخطر دائما، بواقع اثنتي عشرة مرة في السنة<br>• وتيرة الحدوث من 2% إلى 5% سنويا<br>• احتمالية الحدوث بين 80% و 100% |

---`,
  "ru": `## 1. Шкала вероятности
**Источник:** ISO 27005:2022 & Внутренние процедуры DetereCo (Внедрение управления ИТ-рисками)

| Шкала | Категория | Описание |
|:---:|---|---|
| **1** | Маловероятно | • Риск очень маловероятен, не чаще одного раза в год<br>• Частота возникновения < 0.1% в год<br>• Вероятность возникновения риска от 0% до 19% |
| **2** | Скорее маловероятно | • Риск возникает редко, возможно, только два раза в год<br>• Частота возникновения от 0.1% до 1% в год<br>• Вероятность возникновения риска от 20% до 39% |
| **3** | Вероятно | • Риск возникал, но не часто; он возникает три раза в год<br>• Частота возникновения от 1% до 1.5% в год<br>• Вероятность возникновения риска от 40% до 59% |
| **4** | Весьма вероятно | • Риск возникает часто, шесть раз в год<br>• Частота возникновения от 1.5% до 2% в год<br>• Вероятность возникновения от 60% до 79% |
| **5** | Почти наверняка | • Риск возникает всегда, случаясь двенадцать раз в год<br>• Частота возникновения от 2% до 5% в год<br>• Вероятность возникновения от 80% до 100% |

---`,
  "ko": `## 1. 발생 가능성 척도
**출처:** ISO 27005:2022 & DetereCo 내부 절차 (IT 위험 관리 구현)

| 척도 | 범주 | 설명 |
|:---:|---|---|
| **1** | 희박함 | • 위험이 발생할 가능성이 매우 희박하며, 기껏해야 1년에 한 번 발생<br>• 발생 빈도 연간 < 0.1%<br>• 위험 발생 확률 0% ~ 19% |
| **2** | 다소 희박함 | • 위험이 드물게 발생하며, 아마도 1년에 두 번 정도 발생<br>• 발생 빈도 연간 0.1% ~ 1%<br>• 위험 발생 확률 20% ~ 39% |
| **3** | 가능성 있음 | • 위험이 발생한 적이 있지만 자주 발생하지는 않음; 1년에 세 번 발생<br>• 발생 빈도는 연간 1% ~ 1.5% 사이<br>• 위험 발생 확률 40% ~ 59% |
| **4** | 가능성 높음 | • 위험이 자주 발생하며, 1년에 여섯 번 발생<br>• 발생 빈도는 연간 1.5% ~ 2% 사이<br>• 발생 확률 60% ~ 79% |
| **5** | 거의 확실함 | • 위험이 항상 발생하며, 1년에 열두 번 발생<br>• 발생 빈도 연간 2% ~ 5%<br>• 발생 확률 80% ~ 100% |

---`,
  "ja": `## 1. 可能性スケール
**出典:** ISO 27005:2022 & DetereCo 内部手順 (ITリスク管理の実装)

| スケール | カテゴリ | 説明 |
|:---:|---|---|
| **1** | 起こりそうにない | • リスクが発生する可能性は非常に低く、多くても年に1回<br>• 発生頻度 年間 < 0.1%<br>• リスクの発生確率 0% ～ 19% |
| **2** | あまり起こりそうにない | • リスクはまれに発生し、おそらく年に2回程度<br>• 発生頻度 年間 0.1% ～ 1%<br>• リスクの発生確率 20% ～ 39% |
| **3** | 起こり得る | • リスクは発生したことがあるが頻繁ではない。年に3回発生する<br>• 発生頻度は年間 1% ～ 1.5%<br>• リスクの発生確率は 40% ～ 59% |
| **4** | 可能性が高い | • リスクは頻繁に発生し、年に6回発生する<br>• 発生頻度は年間 1.5% ～ 2%<br>• 発生確率は 60% ～ 79% |
| **5** | ほぼ確実 | • リスクは常に発生し、年に12回発生する<br>• 発生頻度 年間 2% ～ 5%<br>• 発生確率 80% ～ 100% |

---`
};

// Also apply a fix for "en" in case it's lacking something, but "en" already looks correct.

// Replace for each language
for (const [lang, newLikelihood] of Object.entries(likelihoodTranslations)) {
  const regex = new RegExp(`("${lang}"\\s*:\\s*"[\\s\\S]*?## 1\\.[^\\n]*\\n)(?:\\*\\*Source[\\s\\S]*?\\n---)`, 'g');
  content = content.replace(regex, (match, p1) => {
    // Actually, the newLikelihood includes the ## 1. title, so let's adjust regex to match starting from ## 1.
    return match;
  });
}

// A better way is to parse the embeddedMarkdown block, update it, and stringify it back.
// Since we only need to replace inside the `criteria` object.
const criteriaMatch = content.match(/criteria:\s*(\{[\s\S]+?\n      \}),/);
if (criteriaMatch) {
  let criteriaStr = criteriaMatch[1];
  for (const [lang, newLikelihood] of Object.entries(likelihoodTranslations)) {
    // Replace from ## 1. <Title> up to the first ---
    const regex = new RegExp(`(## 1\\.[\\s\\S]*?)(?=\\n## 2\\.)`, 'g');
    
    // We only want to replace inside the specific language.
    // So let's isolate each language string.
    const langRegex = new RegExp(`"${lang}"\\s*:\\s*"([\\s\\S]*?)"(?=\\n\\s*(?:,\\s*"|\\}))`, 'g');
    criteriaStr = criteriaStr.replace(langRegex, (match, mdStr) => {
      // Replace the likelihood section
      const replacedMd = mdStr.replace(/## 1\.[^]*?(?=\\n---)/, newLikelihood.replace(/\n/g, '\\n'));
      return `"${lang}": "${replacedMd}"`;
    });
  }
  content = content.replace(criteriaMatch[1], criteriaStr);
  fs.writeFileSync(filePath, content, 'utf8');
  console.log("Successfully updated Likelihood Scale translations!");
} else {
  console.log("Could not find criteria object");
}
