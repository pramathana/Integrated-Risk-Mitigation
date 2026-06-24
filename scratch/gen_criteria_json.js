const fs = require('fs');

const en = `# Likelihood Criteria, Impact Criteria, and Risk Level Criteria

## 1. Likelihood Scale
**Source:** ISO 27005:2022 & DetereCo Internal Procedures (IT Risk Management Implementation)

| Scale | Category | Description |
|:---:|---|---|
| **1** | Unlikely | • The risk is very unlikely to occur, at most once a year<br>• Occurrence frequency < 0.1% per year<br>• Probability of the risk occurring between 0% and 19% |
| **2** | Rather Unlikely | • The risk occurs rarely, perhaps only twice a year<br>• Occurrence frequency from 0.1% to 1% per year<br>• Probability of the risk occurring between 20% and 39% |
| **3** | Likely | • The risk has occurred but not frequently; it occurs three times a year<br>• Occurrence frequency is between 1% and 1.5% per year<br>• Probability of the risk occurring is between 40% and 59% |
| **4** | Very Likely | • The risk occurs frequently, six times a year<br>• Occurrence frequency is between 1.5% and 2% per year<br>• Probability of occurrence between 60% and 79% |
| **5** | Almost Certain | • The risk always occurs, happening twelve times a year<br>• Occurrence frequency from 2% to 5% per year<br>• Probability of occurrence between 80% and 100% |

---

## 2. Impact Scale
**Source:** ISO 27005:2022; DetereCo Internal Procedures (IT Risk Management Implementation); and the DetereCo IT Asset Assessment Form Template

> **Asset Book Value** = Asset Acquisition Price − Accumulated Depreciation/Impairment
> Calculated from directly impacted assets.

| Scale | Category | Infrastructure & Application Systems | Financial Impact | Operational Impact |
|:---:|---|---|---|---|
| **1** | Minor | Less critical supporting applications & infrastructure<br>not functioning for **1 day**<br>*(e.g., employee attendance, website, printer, HR portal)* | < 1% of asset book value | Operations run at 97% ≤ X < 100%.<br>Recovers on the same day.<br>Impact consequences are negligible.<br>The company can overcome it without much difficulty. |
| **2** | Significant | Less critical supporting applications & infrastructure<br>not functioning for **more than 1 day up to 3 days**<br>*(e.g., employee attendance, website, printer, HR portal)* | 1% to 5% of asset book value | Operations run at 93% ≤ X < 97%.<br>Full recovery in maximum 2 working days.<br>Affects activity performance.<br>The company faces some difficulties. |
| **3** | Serious | Important vital applications and infrastructure<br>not functioning (Downtime) for **< 1 hour**<br>*(e.g., electricity, water, communication networks, security systems & online systems)* | 5.1% to 10% of asset book value | Operations run at 90% ≤ X < 93%.<br>Full recovery between 2–7 working days.<br>Major performance drop concerning important data security.<br>The company faces manageable complications. |
| **4** | Critical | Important vital applications and infrastructure<br>not functioning (Downtime) for **> 1 hour up to 6 hours**<br>*(e.g., electricity, water, communication networks, security systems & online systems)* | 11% to 15% of asset book value | Operations run at 80% ≤ X < 90%.<br>Full recovery in 8–15 working days.<br>Serious impact and loss of partial critical confidential data.<br>The company experiences serious difficulties. |
| **5** | Catastrophic | Important vital infrastructure not functioning (Downtime)<br>for **more than 6 hours**<br>*(e.g., electricity, water, communication networks, security systems & online systems)* | > 15% of asset book value | Operations run at X < 80%.<br>Full recovery > 15 working days.<br>Extremely severe impact and loss of all critical confidential data.<br>The company experiences very severe and fatal difficulties. |

---

## 3. Risk Level
**Source:** ISO 27005:2022 & DetereCo Internal Procedures (IT Risk Management Implementation)

> **Formula:** Risk Level = Likelihood (P) × Impact (I)

### 3a. Risk Level Classification

| Score Range (P × I) | Risk Level | Color Indicator | Mitigation Action |
|:---:|---|:---:|---|
| **1 – 5** | Low | 🟢 Light Green | Risk is acceptable. Existing security controls are adequate, routine monitoring is sufficient. |
| **6 – 11** | Low to Moderate | 🟩 Dark Green | Risk requires vigilance. Periodic review and planning for additional security controls. |
| **12 – 15** | Moderate | 🟡 Yellow | Risk must be monitored. Periodic review and addition of medium-scale preventive controls, typically every **3–6 months**. |
| **16 – 19** | Moderate to High | 🟧 Orange | Risk is unacceptable. Requires comprehensive ZTA mitigation actions in the near future **(1–3 months)** to prevent critical incidents. |
| **20 – 25** | High | 🔴 Red | Top handling priority. Emergency condition requiring comprehensive network mitigation and containment to lower the risk level within **< 1 month**. |

### 3b. Risk Level Matrix

|  | **Impact 1** *(Minor)* | **Impact 2** *(Significant)* | **Impact 3** *(Serious)* | **Impact 4** *(Critical)* | **Impact 5** *(Catastrophic)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Likelihood 5** *(Almost Certain)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Likelihood 4** *(Very Likely)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Likelihood 3** *(Likely)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Likelihood 2** *(Rather Unlikely)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Likelihood 1** *(Unlikely)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`;

const id = en
  .replace('Likelihood Criteria, Impact Criteria, and Risk Level Criteria', 'Kriteria Kemungkinan, Kriteria Dampak, dan Kriteria Tingkat Risiko')
  .replace('## 1. Likelihood Scale', '## 1. Skala Kemungkinan')
  .replace('**Source:**', '**Sumber:**')
  .replace('Scale | Category | Description', 'Skala | Kategori | Deskripsi')
  .replace('Unlikely |', 'Tidak Mungkin |')
  .replace('The risk is very unlikely to occur, at most once a year', 'Risiko sangat kecil kemungkinannya untuk terjadi, paling banyak setahun sekali')
  .replace('Occurrence frequency < 0.1% per year', 'Frekuensi kejadian < 0.1% per tahun')
  .replace('Probability of the risk occurring between 0% and 19%', 'Probabilitas risiko terjadi antara 0% dan 19%')
  .replace('Rather Unlikely |', 'Agak Tidak Mungkin |')
  .replace('The risk occurs rarely, perhaps only twice a year', 'Risiko jarang terjadi, mungkin hanya dua kali setahun')
  .replace('Occurrence frequency from 0.1% to 1% per year', 'Frekuensi kejadian dari 0.1% hingga 1% per tahun')
  .replace('Probability of the risk occurring between 20% and 39%', 'Probabilitas risiko terjadi antara 20% dan 39%')
  .replace('Likely |', 'Mungkin |')
  .replace('The risk has occurred but not frequently; it occurs three times a year', 'Risiko telah terjadi tetapi tidak sering; itu terjadi tiga kali setahun')
  .replace('Occurrence frequency is between 1% and 1.5% per year', 'Frekuensi kejadian antara 1% dan 1.5% per tahun')
  .replace('Probability of the risk occurring is between 40% and 59%', 'Probabilitas risiko terjadi antara 40% dan 59%')
  .replace('Very Likely |', 'Sangat Mungkin |')
  .replace('The risk occurs frequently, six times a year', 'Risiko sering terjadi, enam kali setahun')
  .replace('Occurrence frequency is between 1.5% and 2% per year', 'Frekuensi kejadian antara 1.5% dan 2% per tahun')
  .replace('Probability of occurrence between 60% and 79%', 'Probabilitas kejadian antara 60% dan 79%')
  .replace('Almost Certain |', 'Hampir Pasti |')
  .replace('The risk always occurs, happening twelve times a year', 'Risiko selalu terjadi, terjadi dua belas kali setahun')
  .replace('Occurrence frequency from 2% to 5% per year', 'Frekuensi kejadian dari 2% hingga 5% per tahun')
  .replace('Probability of occurrence between 80% and 100%', 'Probabilitas kejadian antara 80% dan 100%')
  .replace('## 2. Impact Scale', '## 2. Skala Dampak')
  .replace('**Asset Book Value** = Asset Acquisition Price − Accumulated Depreciation/Impairment', '**Nilai Buku Aset** = Harga Perolehan Aset − Akumulasi Penyusutan/Penurunan Nilai')
  .replace('Calculated from directly impacted assets.', 'Dihitung dari aset yang terdampak langsung.')
  .replace('Scale | Category | Infrastructure & Application Systems | Financial Impact | Operational Impact', 'Skala | Kategori | Infrastruktur & Sistem Aplikasi | Dampak Finansial | Dampak Operasional')
  .replace('Minor |', 'Minor |')
  .replace('Less critical supporting applications & infrastructure', 'Aplikasi & infrastruktur pendukung yang kurang kritis')
  .replace('not functioning for **1 day**', 'tidak berfungsi selama **1 hari**')
  .replace('*(e.g., employee attendance, website, printer, HR portal)*', '*(mis., absensi karyawan, situs web, printer, portal SDM)*')
  .replace('< 1% of asset book value', '< 1% dari nilai buku aset')
  .replace('Operations run at 97% ≤ X < 100%.', 'Operasi berjalan pada 97% ≤ X < 100%.')
  .replace('Recovers on the same day.', 'Pulih pada hari yang sama.')
  .replace('Impact consequences are negligible.', 'Konsekuensi dampak dapat diabaikan.')
  .replace('The company can overcome it without much difficulty.', 'Perusahaan dapat mengatasinya tanpa banyak kesulitan.')
  .replace('Significant |', 'Signifikan |')
  .replace('Less critical supporting applications & infrastructure', 'Aplikasi & infrastruktur pendukung yang kurang kritis')
  .replace('not functioning for **more than 1 day up to 3 days**', 'tidak berfungsi selama **lebih dari 1 hari hingga 3 hari**')
  .replace('1% to 5% of asset book value', '1% hingga 5% dari nilai buku aset')
  .replace('Operations run at 93% ≤ X < 97%.', 'Operasi berjalan pada 93% ≤ X < 97%.')
  .replace('Full recovery in maximum 2 working days.', 'Pemulihan penuh dalam maksimum 2 hari kerja.')
  .replace('Affects activity performance.', 'Mempengaruhi kinerja aktivitas.')
  .replace('The company faces some difficulties.', 'Perusahaan menghadapi beberapa kesulitan.')
  .replace('Serious |', 'Serius |')
  .replace('Important vital applications and infrastructure', 'Aplikasi dan infrastruktur vital yang penting')
  .replace('not functioning (Downtime) for **< 1 hour**', 'tidak berfungsi (Downtime) selama **< 1 jam**')
  .replace('*(e.g., electricity, water, communication networks, security systems & online systems)*', '*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)*')
  .replace('5.1% to 10% of asset book value', '5.1% hingga 10% dari nilai buku aset')
  .replace('Operations run at 90% ≤ X < 93%.', 'Operasi berjalan pada 90% ≤ X < 93%.')
  .replace('Full recovery between 2–7 working days.', 'Pemulihan penuh antara 2–7 hari kerja.')
  .replace('Major performance drop concerning important data security.', 'Penurunan kinerja utama terkait keamanan data penting.')
  .replace('The company faces manageable complications.', 'Perusahaan menghadapi komplikasi yang dapat dikelola.')
  .replace('Critical |', 'Kritis |')
  .replace('not functioning (Downtime) for **> 1 hour up to 6 hours**', 'tidak berfungsi (Downtime) selama **> 1 jam hingga 6 jam**')
  .replace('11% to 15% of asset book value', '11% hingga 15% dari nilai buku aset')
  .replace('Operations run at 80% ≤ X < 90%.', 'Operasi berjalan pada 80% ≤ X < 90%.')
  .replace('Full recovery in 8–15 working days.', 'Pemulihan penuh dalam 8–15 hari kerja.')
  .replace('Serious impact and loss of partial critical confidential data.', 'Dampak serius dan hilangnya sebagian data rahasia kritis.')
  .replace('The company experiences serious difficulties.', 'Perusahaan mengalami kesulitan serius.')
  .replace('Catastrophic |', 'Bencana |')
  .replace('Important vital infrastructure not functioning (Downtime)', 'Infrastruktur vital yang penting tidak berfungsi (Downtime)')
  .replace('for **more than 6 hours**', 'selama **lebih dari 6 jam**')
  .replace('> 15% of asset book value', '> 15% dari nilai buku aset')
  .replace('Operations run at X < 80%.', 'Operasi berjalan pada X < 80%.')
  .replace('Full recovery > 15 working days.', 'Pemulihan penuh > 15 hari kerja.')
  .replace('Extremely severe impact and loss of all critical confidential data.', 'Dampak yang sangat parah dan hilangnya semua data rahasia kritis.')
  .replace('The company experiences very severe and fatal difficulties.', 'Perusahaan mengalami kesulitan yang sangat parah dan fatal.')
  .replace('## 3. Risk Level', '## 3. Tingkat Risiko')
  .replace('**Formula:** Risk Level = Likelihood (P) × Impact (I)', '**Rumus:** Tingkat Risiko = Kemungkinan (P) × Dampak (I)')
  .replace('### 3a. Risk Level Classification', '### 3a. Klasifikasi Tingkat Risiko')
  .replace('Score Range (P × I) | Risk Level | Color Indicator | Mitigation Action', 'Rentang Skor (P × I) | Tingkat Risiko | Indikator Warna | Tindakan Mitigasi')
  .replace('Low | 🟢 Light Green | Risk is acceptable. Existing security controls are adequate, routine monitoring is sufficient.', 'Rendah | 🟢 Hijau Muda | Risiko dapat diterima. Kontrol keamanan yang ada memadai, pemantauan rutin sudah cukup.')
  .replace('Low to Moderate | 🟩 Dark Green | Risk requires vigilance. Periodic review and planning for additional security controls.', 'Rendah ke Sedang | 🟩 Hijau Tua | Risiko membutuhkan kewaspadaan. Tinjauan berkala dan perencanaan untuk kontrol keamanan tambahan.')
  .replace('Moderate | 🟡 Yellow | Risk must be monitored. Periodic review and addition of medium-scale preventive controls, typically every **3–6 months**.', 'Sedang | 🟡 Kuning | Risiko harus dipantau. Tinjauan berkala dan penambahan kontrol preventif skala menengah, biasanya setiap **3–6 bulan**.')
  .replace('Moderate to High | 🟧 Orange | Risk is unacceptable. Requires comprehensive ZTA mitigation actions in the near future **(1–3 months)** to prevent critical incidents.', 'Sedang ke Tinggi | 🟧 Oranye | Risiko tidak dapat diterima. Membutuhkan tindakan mitigasi ZTA komprehensif dalam waktu dekat **(1–3 bulan)** untuk mencegah insiden kritis.')
  .replace('High | 🔴 Red | Top handling priority. Emergency condition requiring comprehensive network mitigation and containment to lower the risk level within **< 1 month**.', 'Tinggi | 🔴 Merah | Prioritas penanganan utama. Kondisi darurat yang membutuhkan mitigasi dan penahanan jaringan komprehensif untuk menurunkan tingkat risiko dalam **< 1 bulan**.')
  .replace('### 3b. Risk Level Matrix', '### 3b. Matriks Tingkat Risiko')
  .replace('**Impact 1** *(Minor)* | **Impact 2** *(Significant)* | **Impact 3** *(Serious)* | **Impact 4** *(Critical)* | **Impact 5** *(Catastrophic)*', '**Dampak 1** *(Minor)* | **Dampak 2** *(Signifikan)* | **Dampak 3** *(Serius)* | **Dampak 4** *(Kritis)* | **Dampak 5** *(Bencana)*')
  .replace('**Likelihood 5** *(Almost Certain)*', '**Kemungkinan 5** *(Hampir Pasti)*')
  .replace('**Likelihood 4** *(Very Likely)*', '**Kemungkinan 4** *(Sangat Mungkin)*')
  .replace('**Likelihood 3** *(Likely)*', '**Kemungkinan 3** *(Mungkin)*')
  .replace('**Likelihood 2** *(Rather Unlikely)*', '**Kemungkinan 2** *(Agak Tidak Mungkin)*')
  .replace('**Likelihood 1** *(Unlikely)*', '**Kemungkinan 1** *(Tidak Mungkin)*');

// Generating simplified placeholder translations for the other 8 languages.
// We'll replace the main headers and structure.
function makeLang(title, scale, impact, riskLvl) {
  return en
    .replace('Likelihood Criteria, Impact Criteria, and Risk Level Criteria', title)
    .replace('## 1. Likelihood Scale', '## 1. ' + scale)
    .replace('## 2. Impact Scale', '## 2. ' + impact)
    .replace('## 3. Risk Level', '## 3. ' + riskLvl)
    .replace('### 3a. Risk Level Classification', '### 3a. ' + riskLvl + ' Classification')
    .replace('### 3b. Risk Level Matrix', '### 3b. ' + riskLvl + ' Matrix');
}

const criteriaObj = {
  en: en,
  id: id,
  zh: makeLang('可能性标准，影响标准和风险级别标准', '可能性等级', '影响等级', '风险级别'),
  es: makeLang('Criterios de Probabilidad, Impacto y Nivel de Riesgo', 'Escala de Probabilidad', 'Escala de Impacto', 'Nivel de Riesgo'),
  fr: makeLang("Critères de Probabilité, d'Impact et de Niveau de Risque", "Échelle de Probabilité", "Échelle d'Impact", "Niveau de Risque"),
  de: makeLang('Wahrscheinlichkeits-, Auswirkungs- und Risikostufenkriterien', 'Wahrscheinlichkeitsskala', 'Auswirkungsskala', 'Risikostufe'),
  ar: makeLang('معايير الاحتمالية والتأثير ومستوى الخطر', 'مقياس الاحتمالية', 'مقياس التأثير', 'مستوى الخطر'),
  ru: makeLang('Критерии вероятности, воздействия и уровня риска', 'Шкала вероятности', 'Шкала воздействия', 'Уровень риска'),
  ko: makeLang('발생 가능성 기준, 영향 기준 및 위험 수준 기준', '발생 가능성 척도', '영향 척도', '위험 수준'),
  ja: makeLang('可能性基準、影響基準、リスクレベル基準', '可能性スケール', '影響スケール', 'リスクレベル')
};

const criteriaStr = JSON.stringify(criteriaObj, null, 8);
const formattedCode = "criteria: " + criteriaStr + ",";
fs.writeFileSync('scratch/criteria_out.txt', formattedCode, 'utf8');
console.log("Done");
