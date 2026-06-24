criteria: {
        "en": "# Likelihood Criteria, Impact Criteria, and Risk Level Criteria

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
\",
        \"id\": \"# Kriteria Kemungkinan, Kriteria Dampak, dan Kriteria Tingkat Risiko

## 1. Skala Kemungkinan
**Sumber:** ISO 27005:2022 & Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI)

| Skala | Kategori | Deskripsi |
|:---:|---|---|
| **1** | Tidak Mungkin | • Risiko sangat kecil kemungkinannya untuk terjadi, paling banyak setahun sekali<br>• Frekuensi kejadian < 0.1% per tahun<br>• Probabilitas risiko terjadi antara 0% dan 19% |
| **2** | Agak Tidak Mungkin | • Risiko jarang terjadi, mungkin hanya dua kali setahun<br>• Frekuensi kejadian dari 0.1% hingga 1% per tahun<br>• Probabilitas risiko terjadi antara 20% dan 39% |
| **3** | Mungkin | • Risiko telah terjadi tetapi tidak sering; itu terjadi tiga kali setahun<br>• Frekuensi kejadian antara 1% dan 1.5% per tahun<br>• Probabilitas risiko terjadi antara 40% dan 59% |
| **4** | Sangat Mungkin | • Risiko sering terjadi, enam kali setahun<br>• Frekuensi kejadian antara 1.5% dan 2% per tahun<br>• Probabilitas kejadian antara 60% dan 79% |
| **5** | Hampir Pasti | • Risiko selalu terjadi, terjadi dua belas kali setahun<br>• Frekuensi kejadian dari 2% hingga 5% per tahun<br>• Probabilitas kejadian antara 80% dan 100% |

---

## 2. Skala Dampak
**Sumber:** ISO 27005:2022; Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI); dan Templat Formulir Penilaian Aset TI DetereCo

> **Nilai Buku Aset** = Harga Perolehan Aset − Akumulasi Penyusutan/Penurunan Nilai
> Dihitung dari aset yang terdampak langsung.

| Skala | Kategori | Infrastruktur & Sistem Aplikasi | Dampak Finansial | Dampak Operasional |
|:---:|---|---|---|---|
| **1** | Minor | Aplikasi & infrastruktur pendukung yang kurang kritis<br>tidak berfungsi selama **1 hari**<br>*(mis., absensi karyawan, situs web, printer, portal SDM)* | < 1% dari nilai buku aset | Operasi berjalan pada 97% ≤ X < 100%.<br>Pulih pada hari yang sama.<br>Konsekuensi dampak dapat diabaikan.<br>Perusahaan dapat mengatasinya tanpa banyak kesulitan. |
| **2** | Signifikan | Aplikasi & infrastruktur pendukung yang kurang kritis<br>tidak berfungsi selama **lebih dari 1 hari hingga 3 hari**<br>*(mis., absensi karyawan, situs web, printer, portal SDM)* | 1% hingga 5% dari nilai buku aset | Operasi berjalan pada 93% ≤ X < 97%.<br>Pemulihan penuh dalam maksimum 2 hari kerja.<br>Mempengaruhi kinerja aktivitas.<br>Perusahaan menghadapi beberapa kesulitan. |
| **3** | Serius | Aplikasi dan infrastruktur vital yang penting<br>tidak berfungsi (Downtime) selama **< 1 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | 5.1% hingga 10% dari nilai buku aset | Operasi berjalan pada 90% ≤ X < 93%.<br>Pemulihan penuh antara 2–7 hari kerja.<br>Penurunan kinerja utama terkait keamanan data penting.<br>Perusahaan menghadapi komplikasi yang dapat dikelola. |
| **4** | Kritis | Aplikasi dan infrastruktur vital yang penting<br>tidak berfungsi (Downtime) selama **> 1 jam hingga 6 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | 11% hingga 15% dari nilai buku aset | Operasi berjalan pada 80% ≤ X < 90%.<br>Pemulihan penuh dalam 8–15 hari kerja.<br>Dampak serius dan hilangnya sebagian data rahasia kritis.<br>Perusahaan mengalami kesulitan serius. |
| **5** | Bencana | Infrastruktur vital yang penting tidak berfungsi (Downtime)<br>selama **lebih dari 6 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | > 15% dari nilai buku aset | Operasi berjalan pada X < 80%.<br>Pemulihan penuh > 15 hari kerja.<br>Dampak yang sangat parah dan hilangnya semua data rahasia kritis.<br>Perusahaan mengalami kesulitan yang sangat parah dan fatal. |

---

## 3. Tingkat Risiko
**Sumber:** ISO 27005:2022 & Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI)

> **Rumus:** Tingkat Risiko = Kemungkinan (P) × Dampak (I)

### 3a. Klasifikasi Tingkat Risiko

| Rentang Skor (P × I) | Tingkat Risiko | Indikator Warna | Tindakan Mitigasi |
|:---:|---|:---:|---|
| **1 – 5** | Rendah | 🟢 Hijau Muda | Risiko dapat diterima. Kontrol keamanan yang ada memadai, pemantauan rutin sudah cukup. |
| **6 – 11** | Rendah ke Sedang | 🟩 Hijau Tua | Risiko membutuhkan kewaspadaan. Tinjauan berkala dan perencanaan untuk kontrol keamanan tambahan. |
| **12 – 15** | Sedang | 🟡 Kuning | Risiko harus dipantau. Tinjauan berkala dan penambahan kontrol preventif skala menengah, biasanya setiap **3–6 bulan**. |
| **16 – 19** | Sedang ke Tinggi | 🟧 Oranye | Risiko tidak dapat diterima. Membutuhkan tindakan mitigasi ZTA komprehensif dalam waktu dekat **(1–3 bulan)** untuk mencegah insiden kritis. |
| **20 – 25** | Tinggi | 🔴 Merah | Prioritas penanganan utama. Kondisi darurat yang membutuhkan mitigasi dan penahanan jaringan komprehensif untuk menurunkan tingkat risiko dalam **< 1 bulan**. |

### 3b. Matriks Tingkat Risiko

|  | **Dampak 1** *(Minor)* | **Dampak 2** *(Signifikan)* | **Dampak 3** *(Serius)* | **Dampak 4** *(Kritis)* | **Dampak 5** *(Bencana)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Kemungkinan 5** *(Hampir Pasti)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Kemungkinan 4** *(Sangat Mungkin)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Kemungkinan 3** *(Mungkin)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Kemungkinan 2** *(Agak Tidak Mungkin)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Kemungkinan 1** *(Tidak Mungkin)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "id": "# Kriteria Kemungkinan, Kriteria Dampak, dan Kriteria Tingkat Risiko

## 1. Skala Kemungkinan
**Sumber:** ISO 27005:2022 & Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI)

| Skala | Kategori | Deskripsi |
|:---:|---|---|
| **1** | Tidak Mungkin | • Risiko sangat kecil kemungkinannya untuk terjadi, paling banyak setahun sekali<br>• Frekuensi kejadian < 0.1% per tahun<br>• Probabilitas risiko terjadi antara 0% dan 19% |
| **2** | Agak Tidak Mungkin | • Risiko jarang terjadi, mungkin hanya dua kali setahun<br>• Frekuensi kejadian dari 0.1% hingga 1% per tahun<br>• Probabilitas risiko terjadi antara 20% dan 39% |
| **3** | Mungkin | • Risiko telah terjadi tetapi tidak sering; itu terjadi tiga kali setahun<br>• Frekuensi kejadian antara 1% dan 1.5% per tahun<br>• Probabilitas risiko terjadi antara 40% dan 59% |
| **4** | Sangat Mungkin | • Risiko sering terjadi, enam kali setahun<br>• Frekuensi kejadian antara 1.5% dan 2% per tahun<br>• Probabilitas kejadian antara 60% dan 79% |
| **5** | Hampir Pasti | • Risiko selalu terjadi, terjadi dua belas kali setahun<br>• Frekuensi kejadian dari 2% hingga 5% per tahun<br>• Probabilitas kejadian antara 80% dan 100% |

---

## 2. Skala Dampak
**Sumber:** ISO 27005:2022; Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI); dan Templat Formulir Penilaian Aset TI DetereCo

> **Nilai Buku Aset** = Harga Perolehan Aset − Akumulasi Penyusutan/Penurunan Nilai
> Dihitung dari aset yang terdampak langsung.

| Skala | Kategori | Infrastruktur & Sistem Aplikasi | Dampak Finansial | Dampak Operasional |
|:---:|---|---|---|---|
| **1** | Minor | Aplikasi & infrastruktur pendukung yang kurang kritis<br>tidak berfungsi selama **1 hari**<br>*(mis., absensi karyawan, situs web, printer, portal SDM)* | < 1% dari nilai buku aset | Operasi berjalan pada 97% ≤ X < 100%.<br>Pulih pada hari yang sama.<br>Konsekuensi dampak dapat diabaikan.<br>Perusahaan dapat mengatasinya tanpa banyak kesulitan. |
| **2** | Signifikan | Aplikasi & infrastruktur pendukung yang kurang kritis<br>tidak berfungsi selama **lebih dari 1 hari hingga 3 hari**<br>*(mis., absensi karyawan, situs web, printer, portal SDM)* | 1% hingga 5% dari nilai buku aset | Operasi berjalan pada 93% ≤ X < 97%.<br>Pemulihan penuh dalam maksimum 2 hari kerja.<br>Mempengaruhi kinerja aktivitas.<br>Perusahaan menghadapi beberapa kesulitan. |
| **3** | Serius | Aplikasi dan infrastruktur vital yang penting<br>tidak berfungsi (Downtime) selama **< 1 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | 5.1% hingga 10% dari nilai buku aset | Operasi berjalan pada 90% ≤ X < 93%.<br>Pemulihan penuh antara 2–7 hari kerja.<br>Penurunan kinerja utama terkait keamanan data penting.<br>Perusahaan menghadapi komplikasi yang dapat dikelola. |
| **4** | Kritis | Aplikasi dan infrastruktur vital yang penting<br>tidak berfungsi (Downtime) selama **> 1 jam hingga 6 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | 11% hingga 15% dari nilai buku aset | Operasi berjalan pada 80% ≤ X < 90%.<br>Pemulihan penuh dalam 8–15 hari kerja.<br>Dampak serius dan hilangnya sebagian data rahasia kritis.<br>Perusahaan mengalami kesulitan serius. |
| **5** | Bencana | Infrastruktur vital yang penting tidak berfungsi (Downtime)<br>selama **lebih dari 6 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | > 15% dari nilai buku aset | Operasi berjalan pada X < 80%.<br>Pemulihan penuh > 15 hari kerja.<br>Dampak yang sangat parah dan hilangnya semua data rahasia kritis.<br>Perusahaan mengalami kesulitan yang sangat parah dan fatal. |

---

## 3. Tingkat Risiko
**Sumber:** ISO 27005:2022 & Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI)

> **Rumus:** Tingkat Risiko = Kemungkinan (P) × Dampak (I)

### 3a. Klasifikasi Tingkat Risiko

| Rentang Skor (P × I) | Tingkat Risiko | Indikator Warna | Tindakan Mitigasi |
|:---:|---|:---:|---|
| **1 – 5** | Rendah | 🟢 Hijau Muda | Risiko dapat diterima. Kontrol keamanan yang ada memadai, pemantauan rutin sudah cukup. |
| **6 – 11** | Rendah ke Sedang | 🟩 Hijau Tua | Risiko membutuhkan kewaspadaan. Tinjauan berkala dan perencanaan untuk kontrol keamanan tambahan. |
| **12 – 15** | Sedang | 🟡 Kuning | Risiko harus dipantau. Tinjauan berkala dan penambahan kontrol preventif skala menengah, biasanya setiap **3–6 bulan**. |
| **16 – 19** | Sedang ke Tinggi | 🟧 Oranye | Risiko tidak dapat diterima. Membutuhkan tindakan mitigasi ZTA komprehensif dalam waktu dekat **(1–3 bulan)** untuk mencegah insiden kritis. |
| **20 – 25** | Tinggi | 🔴 Merah | Prioritas penanganan utama. Kondisi darurat yang membutuhkan mitigasi dan penahanan jaringan komprehensif untuk menurunkan tingkat risiko dalam **< 1 bulan**. |

### 3b. Matriks Tingkat Risiko

|  | **Dampak 1** *(Minor)* | **Dampak 2** *(Signifikan)* | **Dampak 3** *(Serius)* | **Dampak 4** *(Kritis)* | **Dampak 5** *(Bencana)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Kemungkinan 5** *(Hampir Pasti)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Kemungkinan 4** *(Sangat Mungkin)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Kemungkinan 3** *(Mungkin)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Kemungkinan 2** *(Agak Tidak Mungkin)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Kemungkinan 1** *(Tidak Mungkin)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "zh": "## 1. 可能性等级
**来源:** ISO 27005:2022 & DetereCo 内部程序（IT 风险管理实施）

| 等级 | 类别 | 描述 |
|:---:|---|---|
| **1** | 不太可能 | • 风险发生的可能性极小，最多每年一次<br>• 发生频率 < 0.1% 每年<br>• 风险发生概率在 0% 到 19% 之间 |
| **2** | 较不可能 | • 风险很少发生，可能每年只有两次<br>• 发生频率从 0.1% 到 1% 每年<br>• 风险发生概率在 20% 到 39% 之间 |
| **3** | 可能 | • 风险已发生但不频繁；每年发生三次<br>• 发生频率在 1% 到 1.5% 每年<br>• 风险发生概率在 40% 到 59% 之间 |
| **4** | 很有可能 | • 风险经常发生，每年六次<br>• 发生频率在 1.5% 到 2% 每年<br>• 发生概率在 60% 到 79% 之间 |
| **5** | 几乎确定 | • 风险总是发生，每年发生十二次<br>• 发生频率从 2% 到 5% 每年<br>• 发生概率在 80% 到 100% 之间 |

---

---

## 2. 影响等级
**来源:** ISO 27005:2022; DetereCo 内部程序 (IT 风险管理实施); 以及 DetereCo IT 资产评估表模板

> **资产账面价值** = 资产收购价格 − 累计折旧/减值
> 根据直接受影响的资产计算。

| 等级 | 类别 | 基础设施和应用系统 | 财务影响 | 运营影响 |
|:---:|---|---|---|---|
| **1** | 轻微 | 较不关键的支持应用和基础设施<br>停止运行 **1天**<br>*(例如：员工考勤，网站，打印机，人力资源门户)* | < 资产账面价值的 1% | 运营保持在 97% ≤ X < 100%。<br>当天恢复。<br>影响后果可以忽略不计。<br>公司可以毫不费力地克服它。 |
| **2** | 显著 | 较不关键的支持应用和基础设施<br>停止运行 **1天以上至3天**<br>*(例如：员工考勤，网站，打印机，人力资源门户)* | 资产账面价值的 1% 至 5% | 运营保持在 93% ≤ X < 97%。<br>最多2个工作日内全面恢复。<br>影响活动表现。<br>公司面临一些困难。 |
| **3** | 严重 | 重要的关键应用和基础设施<br>停止运行（停机）**< 1小时**<br>*(例如：电力，水，通信网络，安全系统和在线系统)* | 资产账面价值的 5.1% 至 10% | 运营保持在 90% ≤ X < 93%。<br>在2-7个工作日内全面恢复。<br>涉及重要数据安全的性能大幅下降。<br>公司面临可控的并发症。 |
| **4** | 危急 | 重要的关键应用和基础设施<br>停止运行（停机）**> 1小时至6小时**<br>*(例如：电力，水，通信网络，安全系统和在线系统)* | 资产账面价值的 11% 至 15% | 运营保持在 80% ≤ X < 90%。<br>在8-15个工作日内全面恢复。<br>严重影响并丢失部分关键机密数据。<br>公司遇到严重困难。 |
| **5** | 灾难性 | 重要的关键基础设施停止运行（停机）<br>**超过6小时**<br>*(例如：电力，水，通信网络，安全系统和在线系统)* | > 资产账面价值的 15% | 运营保持在 X < 80%。<br>全面恢复 > 15个工作日。<br>极其严重的影响并丢失所有关键机密数据。<br>公司遇到非常严重和致命的困难。 |

---

---

## 3. 风险级别
**来源:** ISO 27005:2022 & DetereCo 内部程序（IT 风险管理实施）

> **公式:** 风险级别 = 可能性 (P) × 影响 (I)

### 3a. 风险级别分类

| 分数范围 (P × I) | 风险级别 | 颜色指示器 | 缓解措施 |
|:---:|---|:---:|---|
| **1 – 5** | 低 | 🟢 浅绿 | 风险可接受。现有安全控制充足，常规监控即可。 |
| **6 – 11** | 低到中等 | 🟩 深绿 | 风险需要警惕。定期审查并计划增加额外的安全控制。 |
| **12 – 15** | 中等 | 🟡 黄色 | 必须监控风险。定期审查并增加中等规模的预防性控制，通常每 **3-6 个月**一次。 |
| **16 – 19** | 中等到高 | 🟧 橙色 | 风险不可接受。要求在不久的将来 **(1-3 个月)** 采取全面的零信任架构 (ZTA) 缓解措施，以防止发生严重事件。 |
| **20 – 25** | 高 | 🔴 红色 | 最高处理优先级。需要采取全面网络缓解和遏制措施以在 **< 1 个月**内降低风险级别的紧急情况。 |

### 3b. 风险级别矩阵

|  | **影响 1** *(轻微)* | **影响 2** *(显著)* | **影响 3** *(严重)* | **影响 4** *(危急)* | **影响 5** *(灾难性)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **可能性 5** *(几乎确定)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **可能性 4** *(很有可能)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **可能性 3** *(可能)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **可能性 2** *(较不可能)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **可能性 1** *(不太可能)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "es": "## 1. Escala de Probabilidad
**Fuente:** ISO 27005:2022 & Procedimientos Internos de DetereCo (Implementación de Gestión de Riesgos de TI)

| Escala | Categoría | Descripción |
|:---:|---|---|
| **1** | Improbable | • El riesgo es muy improbable que ocurra, como máximo una vez al año<br>• Frecuencia de ocurrencia < 0.1% por año<br>• Probabilidad de que el riesgo ocurra entre 0% y 19% |
| **2** | Poco Probable | • El riesgo ocurre raramente, quizás solo dos veces al año<br>• Frecuencia de ocurrencia del 0.1% al 1% por año<br>• Probabilidad de que el riesgo ocurra entre 20% y 39% |
| **3** | Probable | • El riesgo ha ocurrido pero no frecuentemente; ocurre tres veces al año<br>• Frecuencia de ocurrencia entre 1% y 1.5% por año<br>• Probabilidad de que el riesgo ocurra entre 40% y 59% |
| **4** | Muy Probable | • El riesgo ocurre frecuentemente, seis veces al año<br>• Frecuencia de ocurrencia entre 1.5% y 2% por año<br>• Probabilidad de ocurrencia entre 60% y 79% |
| **5** | Casi Seguro | • El riesgo siempre ocurre, sucediendo doce veces al año<br>• Frecuencia de ocurrencia del 2% al 5% por año<br>• Probabilidad de ocurrencia entre 80% y 100% |

---

---

## 2. Escala de Impacto
**Fuente:** ISO 27005:2022; Procedimientos Internos de DetereCo (Implementación de Gestión de Riesgos de TI); y la Plantilla del Formulario de Evaluación de Activos de TI de DetereCo

> **Valor Contable del Activo** = Precio de Adquisición del Activo − Depreciación/Deterioro Acumulado
> Calculado a partir de los activos directamente afectados.

| Escala | Categoría | Infraestructura y Sistemas de Aplicaciones | Impacto Financiero | Impacto Operativo |
|:---:|---|---|---|---|
| **1** | Menor | Aplicaciones de soporte e infraestructura menos críticas<br>sin funcionar durante **1 día**<br>*(por ejemplo, asistencia de empleados, sitio web, impresora, portal de recursos humanos)* | < 1% del valor contable del activo | Las operaciones funcionan al 97% ≤ X < 100%.<br>Se recupera el mismo día.<br>Las consecuencias del impacto son insignificantes.<br>La empresa puede superarlo sin mucha dificultad. |
| **2** | Significativo | Aplicaciones de soporte e infraestructura menos críticas<br>sin funcionar durante **más de 1 día hasta 3 días**<br>*(por ejemplo, asistencia de empleados, sitio web, impresora, portal de recursos humanos)* | 1% a 5% del valor contable del activo | Las operaciones funcionan al 93% ≤ X < 97%.<br>Recuperación total en un máximo de 2 días hábiles.<br>Afecta el rendimiento de la actividad.<br>La empresa enfrenta algunas dificultades. |
| **3** | Grave | Aplicaciones e infraestructura vitales importantes<br>sin funcionar (Tiempo de inactividad) por **< 1 hora**<br>*(por ejemplo, electricidad, agua, redes de comunicación, sistemas de seguridad y sistemas en línea)* | 5.1% a 10% del valor contable del activo | Las operaciones funcionan al 90% ≤ X < 93%.<br>Recuperación total entre 2 y 7 días hábiles.<br>Fuerte caída del rendimiento en relación con la seguridad de datos importantes.<br>La empresa enfrenta complicaciones manejables. |
| **4** | Crítico | Aplicaciones e infraestructura vitales importantes<br>sin funcionar (Tiempo de inactividad) por **> 1 hora hasta 6 horas**<br>*(por ejemplo, electricidad, agua, redes de comunicación, sistemas de seguridad y sistemas en línea)* | 11% a 15% del valor contable del activo | Las operaciones funcionan al 80% ≤ X < 90%.<br>Recuperación total en 8-15 días hábiles.<br>Impacto grave y pérdida parcial de datos confidenciales críticos.<br>La empresa experimenta graves dificultades. |
| **5** | Catastrófico | Infraestructura vital importante sin funcionar (Tiempo de inactividad)<br>por **más de 6 horas**<br>*(por ejemplo, electricidad, agua, redes de comunicación, sistemas de seguridad y sistemas en línea)* | > 15% del valor contable del activo | Las operaciones funcionan a X < 80%.<br>Recuperación total > 15 días hábiles.<br>Impacto extremadamente grave y pérdida de todos los datos confidenciales críticos.<br>La empresa experimenta dificultades muy graves y fatales. |

---

---

## 3. Nivel de Riesgo
**Fuente:** ISO 27005:2022 & Procedimientos Internos de DetereCo (Implementación de Gestión de Riesgos de TI)

> **Fórmula:** Nivel de Riesgo = Probabilidad (P) × Impacto (I)

### 3a. Clasificación del Nivel de Riesgo

| Rango de Puntuación (P × I) | Nivel de Riesgo | Indicador de Color | Acción de Mitigación |
|:---:|---|:---:|---|
| **1 – 5** | Bajo | 🟢 Verde Claro | El riesgo es aceptable. Los controles de seguridad existentes son adecuados, el monitoreo de rutina es suficiente. |
| **6 – 11** | Bajo a Moderado | 🟩 Verde Oscuro | El riesgo requiere vigilancia. Revisión periódica y planificación de controles de seguridad adicionales. |
| **12 – 15** | Moderado | 🟡 Amarillo | El riesgo debe ser monitoreado. Revisión periódica y adición de controles preventivos a mediana escala, típicamente cada **3–6 meses**. |
| **16 – 19** | Moderado a Alto | 🟧 Naranja | El riesgo es inaceptable. Requiere acciones integrales de mitigación de ZTA en el futuro cercano **(1–3 meses)** para prevenir incidentes críticos. |
| **20 – 25** | Alto | 🔴 Rojo | Máxima prioridad de manejo. Condición de emergencia que requiere mitigación y contención integral de la red para reducir el nivel de riesgo en **< 1 mes**. |

### 3b. Matriz de Nivel de Riesgo

|  | **Impacto 1** *(Menor)* | **Impacto 2** *(Significativo)* | **Impacto 3** *(Grave)* | **Impacto 4** *(Crítico)* | **Impacto 5** *(Catastrófico)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Probabilidad 5** *(Casi Seguro)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Probabilidad 4** *(Muy Probable)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Probabilidad 3** *(Probable)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Probabilidad 2** *(Poco Probable)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Probabilidad 1** *(Improbable)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "fr": "## 1. Échelle de Probabilité
**Source:** ISO 27005:2022 & Procédures Internes de DetereCo (Mise en Œuvre de la Gestion des Risques Informatiques)

| Échelle | Catégorie | Description |
|:---:|---|---|
| **1** | Improbable | • Il est très peu probable que le risque se produise, au plus une fois par an<br>• Fréquence d'occurrence < 0.1% par an<br>• Probabilité d'occurrence du risque entre 0% et 19% |
| **2** | Peu Probable | • Le risque se produit rarement, peut-être seulement deux fois par an<br>• Fréquence d'occurrence de 0.1% à 1% par an<br>• Probabilité d'occurrence du risque entre 20% et 39% |
| **3** | Probable | • Le risque s'est produit mais pas fréquemment ; il se produit trois fois par an<br>• Fréquence d'occurrence entre 1% et 1.5% par an<br>• Probabilité d'occurrence du risque entre 40% et 59% |
| **4** | Très Probable | • Le risque se produit fréquemment, six fois par an<br>• Fréquence d'occurrence entre 1.5% et 2% par an<br>• Probabilité d'occurrence entre 60% et 79% |
| **5** | Presque Certain | • Le risque se produit toujours, arrivant douze fois par an<br>• Fréquence d'occurrence de 2% à 5% par an<br>• Probabilité d'occurrence entre 80% et 100% |

---

---

## 2. Échelle d'Impact
**Source :** ISO 27005:2022 ; Procédures Internes de DetereCo (Mise en Œuvre de la Gestion des Risques Informatiques) ; et le Modèle de Formulaire d'Évaluation des Actifs Informatiques de DetereCo

> **Valeur Comptable de l'Actif** = Prix d'Acquisition de l'Actif − Amortissement/Dépréciation Cumulé
> Calculé à partir des actifs directement impactés.

| Échelle | Catégorie | Infrastructure et Systèmes d'Application | Impact Financier | Impact Opérationnel |
|:---:|---|---|---|---|
| **1** | Mineur | Applications de support et infrastructure moins critiques<br>ne fonctionnant pas pendant **1 jour**<br>*(ex., présence des employés, site web, imprimante, portail RH)* | < 1% de la valeur comptable de l'actif | Les opérations fonctionnent à 97% ≤ X < 100%.<br>Récupère le même jour.<br>Les conséquences de l'impact sont négligeables.<br>L'entreprise peut le surmonter sans grande difficulté. |
| **2** | Significatif | Applications de support et infrastructure moins critiques<br>ne fonctionnant pas pendant **plus d'1 jour jusqu'à 3 jours**<br>*(ex., présence des employés, site web, imprimante, portail RH)* | 1% à 5% de la valeur comptable de l'actif | Les opérations fonctionnent à 93% ≤ X < 97%.<br>Récupération complète en 2 jours ouvrables maximum.<br>Affecte les performances des activités.<br>L'entreprise fait face à certaines difficultés. |
| **3** | Grave | Applications et infrastructures vitales importantes<br>ne fonctionnant pas (Temps d'arrêt) pendant **< 1 heure**<br>*(ex., électricité, eau, réseaux de communication, systèmes de sécurité & systèmes en ligne)* | 5.1% à 10% de la valeur comptable de l'actif | Les opérations fonctionnent à 90% ≤ X < 93%.<br>Récupération complète entre 2 et 7 jours ouvrables.<br>Baisse majeure des performances concernant la sécurité des données importantes.<br>L'entreprise fait face à des complications gérables. |
| **4** | Critique | Applications et infrastructures vitales importantes<br>ne fonctionnant pas (Temps d'arrêt) pendant **> 1 heure jusqu'à 6 heures**<br>*(ex., électricité, eau, réseaux de communication, systèmes de sécurité & systèmes en ligne)* | 11% à 15% de la valeur comptable de l'actif | Les opérations fonctionnent à 80% ≤ X < 90%.<br>Récupération complète en 8 à 15 jours ouvrables.<br>Impact grave et perte partielle de données confidentielles critiques.<br>L'entreprise connaît de graves difficultés. |
| **5** | Catastrophique | Infrastructure vitale importante ne fonctionnant pas (Temps d'arrêt)<br>pendant **plus de 6 heures**<br>*(ex., électricité, eau, réseaux de communication, systèmes de sécurité & systèmes en ligne)* | > 15% de la valeur comptable de l'actif | Les opérations fonctionnent à X < 80%.<br>Récupération complète > 15 jours ouvrables.<br>Impact extrêmement sévère et perte de toutes les données confidentielles critiques.<br>L'entreprise connaît des difficultés très graves et fatales. |

---

---

## 3. Niveau de Risque
**Source:** ISO 27005:2022 & Procédures Internes de DetereCo (Mise en Œuvre de la Gestion des Risques Informatiques)

> **Formule:** Niveau de Risque = Probabilité (P) × Impact (I)

### 3a. Classification du Niveau de Risque

| Plage de Score (P × I) | Niveau de Risque | Indicateur de Couleur | Action d'Atténuation |
|:---:|---|:---:|---|
| **1 – 5** | Faible | 🟢 Vert Clair | Le risque est acceptable. Les contrôles de sécurité existants sont adéquats, une surveillance de routine est suffisante. |
| **6 – 11** | Faible à Modéré | 🟩 Vert Foncé | Le risque nécessite de la vigilance. Examen périodique et planification de contrôles de sécurité supplémentaires. |
| **12 – 15** | Modéré | 🟡 Jaune | Le risque doit être surveillé. Examen périodique et ajout de contrôles préventifs à moyenne échelle, typiquement tous les **3 à 6 mois**. |
| **16 – 19** | Modéré à Élevé | 🟧 Orange | Le risque est inacceptable. Nécessite des actions globales d'atténuation ZTA dans un avenir proche **(1 à 3 mois)** pour prévenir les incidents critiques. |
| **20 – 25** | Élevé | 🔴 Rouge | Priorité de traitement absolue. Condition d'urgence nécessitant une atténuation et un confinement complets du réseau pour abaisser le niveau de risque dans les **< 1 mois**. |

### 3b. Matrice du Niveau de Risque

|  | **Impact 1** *(Mineur)* | **Impact 2** *(Significatif)* | **Impact 3** *(Grave)* | **Impact 4** *(Critique)* | **Impact 5** *(Catastrophique)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Probabilité 5** *(Presque Certain)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Probabilité 4** *(Très Probable)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Probabilité 3** *(Probable)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Probabilité 2** *(Peu Probable)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Probabilité 1** *(Improbable)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "de": "## 1. Wahrscheinlichkeitsskala
**Quelle:** ISO 27005:2022 & Interne Verfahren von DetereCo (Implementierung des IT-Risikomanagements)

| Skala | Kategorie | Beschreibung |
|:---:|---|---|
| **1** | Unwahrscheinlich | • Das Risiko tritt sehr unwahrscheinlich ein, höchstens einmal im Jahr<br>• Eintrittshäufigkeit < 0.1% pro Jahr<br>• Eintrittswahrscheinlichkeit des Risikos zwischen 0% und 19% |
| **2** | Eher Unwahrscheinlich | • Das Risiko tritt selten auf, vielleicht nur zweimal im Jahr<br>• Eintrittshäufigkeit von 0.1% bis 1% pro Jahr<br>• Eintrittswahrscheinlichkeit des Risikos zwischen 20% und 39% |
| **3** | Wahrscheinlich | • Das Risiko ist aufgetreten, aber nicht häufig; es tritt dreimal im Jahr auf<br>• Eintrittshäufigkeit liegt zwischen 1% und 1.5% pro Jahr<br>• Eintrittswahrscheinlichkeit des Risikos liegt zwischen 40% und 59% |
| **4** | Sehr Wahrscheinlich | • Das Risiko tritt häufig auf, sechsmal im Jahr<br>• Eintrittshäufigkeit liegt zwischen 1.5% und 2% pro Jahr<br>• Eintrittswahrscheinlichkeit zwischen 60% und 79% |
| **5** | Fast Sicher | • Das Risiko tritt immer auf, zwölfmal im Jahr<br>• Eintrittshäufigkeit von 2% bis 5% pro Jahr<br>• Eintrittswahrscheinlichkeit zwischen 80% und 100% |

---

---

## 2. Auswirkungsskala
**Quelle:** ISO 27005:2022; Interne Verfahren von DetereCo (Implementierung des IT-Risikomanagements); und die Vorlage für das IT-Asset-Bewertungsformular von DetereCo

> **Buchwert der Anlage** = Anschaffungspreis der Anlage − Kumulierte Abschreibung/Wertminderung
> Berechnet aus direkt betroffenen Anlagen.

| Skala | Kategorie | Infrastruktur & Anwendungssysteme | Finanzielle Auswirkung | Betriebliche Auswirkung |
|:---:|---|---|---|---|
| **1** | Gering | Weniger kritische unterstützende Anwendungen und Infrastruktur<br>funktionieren für **1 Tag** nicht<br>*(z. B. Mitarbeiteranwesenheit, Website, Drucker, HR-Portal)* | < 1% des Buchwerts der Anlage | Betrieb läuft bei 97% ≤ X < 100%.<br>Erholt sich noch am selben Tag.<br>Auswirkungsfolgen sind vernachlässigbar.<br>Das Unternehmen kann dies ohne große Schwierigkeiten bewältigen. |
| **2** | Erheblich | Weniger kritische unterstützende Anwendungen und Infrastruktur<br>funktionieren für **mehr als 1 Tag bis zu 3 Tagen** nicht<br>*(z. B. Mitarbeiteranwesenheit, Website, Drucker, HR-Portal)* | 1% bis 5% des Buchwerts der Anlage | Betrieb läuft bei 93% ≤ X < 97%.<br>Vollständige Wiederherstellung in maximal 2 Werktagen.<br>Beeinflusst die Aktivitätsleistung.<br>Das Unternehmen hat einige Schwierigkeiten. |
| **3** | Ernsthaft | Wichtige vitale Anwendungen und Infrastruktur<br>funktionieren (Ausfallzeit) für **< 1 Stunde** nicht<br>*(z. B. Strom, Wasser, Kommunikationsnetze, Sicherheitssysteme & Online-Systeme)* | 5.1% bis 10% des Buchwerts der Anlage | Betrieb läuft bei 90% ≤ X < 93%.<br>Vollständige Wiederherstellung zwischen 2–7 Werktagen.<br>Erheblicher Leistungsabfall in Bezug auf wichtige Datensicherheit.<br>Das Unternehmen steht vor überschaubaren Komplikationen. |
| **4** | Kritisch | Wichtige vitale Anwendungen und Infrastruktur<br>funktionieren (Ausfallzeit) für **> 1 Stunde bis zu 6 Stunden** nicht<br>*(z. B. Strom, Wasser, Kommunikationsnetze, Sicherheitssysteme & Online-Systeme)* | 11% bis 15% des Buchwerts der Anlage | Betrieb läuft bei 80% ≤ X < 90%.<br>Vollständige Wiederherstellung in 8–15 Werktagen.<br>Schwerwiegende Auswirkung und Verlust eines Teils kritischer vertraulicher Daten.<br>Das Unternehmen hat ernsthafte Schwierigkeiten. |
| **5** | Katastrophal | Wichtige vitale Infrastruktur funktioniert (Ausfallzeit)<br>für **mehr als 6 Stunden** nicht<br>*(z. B. Strom, Wasser, Kommunikationsnetze, Sicherheitssysteme & Online-Systeme)* | > 15% des Buchwerts der Anlage | Betrieb läuft bei X < 80%.<br>Vollständige Wiederherstellung > 15 Werktage.<br>Extrem schwere Auswirkung und Verlust aller kritischer vertraulicher Daten.<br>Das Unternehmen erlebt sehr schwere und fatale Schwierigkeiten. |

---

---

## 3. Risikostufe
**Quelle:** ISO 27005:2022 & Interne Verfahren von DetereCo (Implementierung des IT-Risikomanagements)

> **Formel:** Risikostufe = Wahrscheinlichkeit (P) × Auswirkung (I)

### 3a. Risikostufenklassifizierung

| Punktebereich (P × I) | Risikostufe | Farbindikator | Minderungsmaßnahme |
|:---:|---|:---:|---|
| **1 – 5** | Niedrig | 🟢 Hellgrün | Risiko ist akzeptabel. Bestehende Sicherheitskontrollen sind angemessen, routinemäßige Überwachung ist ausreichend. |
| **6 – 11** | Niedrig bis Mittel | 🟩 Dunkelgrün | Risiko erfordert Wachsamkeit. Regelmäßige Überprüfung und Planung für zusätzliche Sicherheitskontrollen. |
| **12 – 15** | Mittel | 🟡 Gelb | Risiko muss überwacht werden. Regelmäßige Überprüfung und Hinzufügung mittelgroßer präventiver Kontrollen, typischerweise alle **3–6 Monate**. |
| **16 – 19** | Mittel bis Hoch | 🟧 Orange | Risiko ist inakzeptabel. Erfordert in naher Zukunft **(1–3 Monate)** umfassende ZTA-Minderungsmaßnahmen, um kritische Vorfälle zu verhindern. |
| **20 – 25** | Hoch | 🔴 Rot | Höchste Priorität bei der Bearbeitung. Notfallzustand, der eine umfassende Netzwerk-Minderung und Eindämmung erfordert, um die Risikostufe innerhalb von **< 1 Monat** zu senken. |

### 3b. Risikostufenmatrix

|  | **Auswirkung 1** *(Gering)* | **Auswirkung 2** *(Erheblich)* | **Auswirkung 3** *(Ernsthaft)* | **Auswirkung 4** *(Kritisch)* | **Auswirkung 5** *(Katastrophal)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Wahrscheinlichkeit 5** *(Fast Sicher)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Wahrscheinlichkeit 4** *(Sehr Wahrscheinlich)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Wahrscheinlichkeit 3** *(Wahrscheinlich)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Wahrscheinlichkeit 2** *(Eher Unwahrscheinlich)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Wahrscheinlichkeit 1** *(Unwahrscheinlich)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "ar": "## 1. مقياس الاحتمالية
**المصدر:** ISO 27005:2022 & الإجراءات الداخلية لشركة DetereCo (تنفيذ إدارة مخاطر تكنولوجيا المعلومات)

| المقياس | الفئة | الوصف |
|:---:|---|---|
| **1** | غير محتمل | • من غير المحتمل جدا أن يحدث الخطر، على الأكثر مرة واحدة في السنة<br>• وتيرة الحدوث < 0.1% سنويا<br>• احتمالية حدوث الخطر بين 0% و 19% |
| **2** | غير محتمل نوعا ما | • يحدث الخطر نادرا، ربما مرتين فقط في السنة<br>• وتيرة الحدوث من 0.1% إلى 1% سنويا<br>• احتمالية حدوث الخطر بين 20% و 39% |
| **3** | محتمل | • حدث الخطر ولكن ليس بشكل متكرر؛ يحدث ثلاث مرات في السنة<br>• وتيرة الحدوث بين 1% و 1.5% سنويا<br>• احتمالية حدوث الخطر بين 40% و 59% |
| **4** | محتمل جدا | • يحدث الخطر بشكل متكرر، ست مرات في السنة<br>• وتيرة الحدوث بين 1.5% و 2% سنويا<br>• احتمالية الحدوث بين 60% و 79% |
| **5** | شبه مؤكد | • يحدث الخطر دائما، بواقع اثنتي عشرة مرة في السنة<br>• وتيرة الحدوث من 2% إلى 5% سنويا<br>• احتمالية الحدوث بين 80% و 100% |

---

---

## 2. مقياس التأثير
**المصدر:** ISO 27005:2022؛ الإجراءات الداخلية لشركة DetereCo (تنفيذ إدارة مخاطر تكنولوجيا المعلومات)؛ ونموذج تقييم أصول تكنولوجيا المعلومات لشركة DetereCo

> **القيمة الدفترية للأصل** = سعر اقتناء الأصل − الاستهلاك المتراكم/انخفاض القيمة
> تُحسب من الأصول المتأثرة بشكل مباشر.

| المقياس | الفئة | أنظمة البنية التحتية والتطبيقات | التأثير المالي | التأثير التشغيلي |
|:---:|---|---|---|---|
| **1** | طفيف | التطبيقات الداعمة والبنية التحتية الأقل أهمية<br>لا تعمل لمدة **يوم واحد**<br>*(على سبيل المثال، حضور الموظفين، موقع الويب، الطابعة، بوابة الموارد البشرية)* | < 1% من القيمة الدفترية للأصل | تسير العمليات بنسبة 97% ≤ X < 100%.<br>تتعافى في نفس اليوم.<br>عواقب التأثير ضئيلة.<br>يمكن للشركة التغلب عليها دون صعوبة كبيرة. |
| **2** | كبير | التطبيقات الداعمة والبنية التحتية الأقل أهمية<br>لا تعمل لمدة **أكثر من يوم واحد حتى 3 أيام**<br>*(على سبيل المثال، حضور الموظفين، موقع الويب، الطابعة، بوابة الموارد البشرية)* | 1% إلى 5% من القيمة الدفترية للأصل | تسير العمليات بنسبة 93% ≤ X < 97%.<br>تعافي كامل خلال يومي عمل كحد أقصى.<br>يؤثر على أداء النشاط.<br>تواجه الشركة بعض الصعوبات. |
| **3** | خطير | التطبيقات والبنية التحتية الحيوية الهامة<br>لا تعمل (فترة التوقف) لمدة **< 1 ساعة**<br>*(على سبيل المثال، الكهرباء، المياه، شبكات الاتصالات، أنظمة الأمان والأنظمة عبر الإنترنت)* | 5.1% إلى 10% من القيمة الدفترية للأصل | تسير العمليات بنسبة 90% ≤ X < 93%.<br>تعافي كامل بين 2–7 أيام عمل.<br>انخفاض كبير في الأداء فيما يتعلق بأمن البيانات المهمة.<br>تواجه الشركة مضاعفات يمكن إدارتها. |
| **4** | حرج | التطبيقات والبنية التحتية الحيوية الهامة<br>لا تعمل (فترة التوقف) لمدة **> 1 ساعة حتى 6 ساعات**<br>*(على سبيل المثال، الكهرباء، المياه، شبكات الاتصالات، أنظمة الأمان والأنظمة عبر الإنترنت)* | 11% إلى 15% من القيمة الدفترية للأصل | تسير العمليات بنسبة 80% ≤ X < 90%.<br>تعافي كامل خلال 8–15 يوم عمل.<br>تأثير خطير وفقدان جزئي للبيانات السرية الحرجة.<br>تواجه الشركة صعوبات بالغة. |
| **5** | كارثي | البنية التحتية الحيوية الهامة لا تعمل (فترة التوقف)<br>لمدة **أكثر من 6 ساعات**<br>*(على سبيل المثال، الكهرباء، المياه، شبكات الاتصالات، أنظمة الأمان والأنظمة عبر الإنترنت)* | > 15% من القيمة الدفترية للأصل | تسير العمليات بنسبة X < 80%.<br>تعافي كامل > 15 يوم عمل.<br>تأثير شديد للغاية وفقدان كامل للبيانات السرية الحرجة.<br>تواجه الشركة صعوبات شديدة ومميتة. |

---

---

## 3. مستوى الخطر
**المصدر:** ISO 27005:2022 & الإجراءات الداخلية لشركة DetereCo (تنفيذ إدارة مخاطر تكنولوجيا المعلومات)

> **الصيغة:** مستوى الخطر = الاحتمالية (P) × التأثير (I)

### 3a. تصنيف مستوى الخطر

| نطاق النتيجة (P × I) | مستوى الخطر | مؤشر اللون | إجراء التخفيف |
|:---:|---|:---:|---|
| **1 – 5** | منخفض | 🟢 أخضر فاتح | الخطر مقبول. الضوابط الأمنية الحالية كافية، والمراقبة الروتينية كافية. |
| **6 – 11** | منخفض إلى متوسط | 🟩 أخضر غامق | الخطر يتطلب اليقظة. المراجعة الدورية والتخطيط لضوابط أمنية إضافية. |
| **12 – 15** | متوسط | 🟡 أصفر | يجب مراقبة الخطر. المراجعة الدورية وإضافة ضوابط وقائية متوسطة الحجم، عادة كل **3-6 أشهر**. |
| **16 – 19** | متوسط إلى مرتفع | 🟧 برتقالي | الخطر غير مقبول. يتطلب إجراءات تخفيف شاملة لـ ZTA في المستقبل القريب **(1-3 أشهر)** لمنع الحوادث الحرجة. |
| **20 – 25** | مرتفع | 🔴 أحمر | أولوية التعامل القصوى. حالة طوارئ تتطلب تخفيف وتأمين شبكة شامل لخفض مستوى الخطر في غضون **< 1 شهر**. |

### 3b. مصفوفة مستوى الخطر

|  | **التأثير 1** *(طفيف)* | **التأثير 2** *(كبير)* | **التأثير 3** *(خطير)* | **التأثير 4** *(حرج)* | **التأثير 5** *(كارثي)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **الاحتمالية 5** *(شبه مؤكد)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **الاحتمالية 4** *(محتمل جدا)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **الاحتمالية 3** *(محتمل)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **الاحتمالية 2** *(غير محتمل نوعا ما)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **الاحتمالية 1** *(غير محتمل)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "ru": "## 1. Шкала вероятности
**Источник:** ISO 27005:2022 & Внутренние процедуры DetereCo (Внедрение управления ИТ-рисками)

| Шкала | Категория | Описание |
|:---:|---|---|
| **1** | Маловероятно | • Риск очень маловероятен, не чаще одного раза в год<br>• Частота возникновения < 0.1% в год<br>• Вероятность возникновения риска от 0% до 19% |
| **2** | Скорее маловероятно | • Риск возникает редко, возможно, только два раза в год<br>• Частота возникновения от 0.1% до 1% в год<br>• Вероятность возникновения риска от 20% до 39% |
| **3** | Вероятно | • Риск возникал, но не часто; он возникает три раза в год<br>• Частота возникновения от 1% до 1.5% в год<br>• Вероятность возникновения риска от 40% до 59% |
| **4** | Весьма вероятно | • Риск возникает часто, шесть раз в год<br>• Частота возникновения от 1.5% до 2% в год<br>• Вероятность возникновения от 60% до 79% |
| **5** | Почти наверняка | • Риск возникает всегда, случаясь двенадцать раз в год<br>• Частота возникновения от 2% до 5% в год<br>• Вероятность возникновения от 80% до 100% |

---

---

## 2. Шкала воздействия
**Источник:** ISO 27005:2022; Внутренние процедуры DetereCo (Внедрение управления ИТ-рисками); и Шаблон формы оценки ИТ-активов DetereCo

> **Балансовая стоимость актива** = Цена приобретения актива − Накопленная амортизация/Обесценение
> Рассчитывается на основе непосредственно затронутых активов.

| Шкала | Категория | Инфраструктура и прикладные системы | Финансовое воздействие | Эксплуатационное воздействие |
|:---:|---|---|---|---|
| **1** | Незначительное | Менее критически важные вспомогательные приложения и инфраструктура<br>не функционируют в течение **1 дня**<br>*(например, посещаемость сотрудников, веб-сайт, принтер, кадровый портал)* | < 1% от балансовой стоимости актива | Операции выполняются на 97% ≤ X < 100%.<br>Восстанавливается в тот же день.<br>Последствия воздействия незначительны.<br>Компания может преодолеть это без особых трудностей. |
| **2** | Существенное | Менее критически важные вспомогательные приложения и инфраструктура<br>не функционируют в течение **более 1 дня и до 3 дней**<br>*(например, посещаемость сотрудников, веб-сайт, принтер, кадровый портал)* | от 1% до 5% от балансовой стоимости актива | Операции выполняются на 93% ≤ X < 97%.<br>Полное восстановление максимум за 2 рабочих дня.<br>Влияет на эффективность деятельности.<br>Компания сталкивается с некоторыми трудностями. |
| **3** | Серьезное | Важные жизненно важные приложения и инфраструктура<br>не функционируют (время простоя) в течение **< 1 часа**<br>*(например, электричество, вода, сети связи, системы безопасности и онлайн-системы)* | от 5.1% до 10% от балансовой стоимости актива | Операции выполняются на 90% ≤ X < 93%.<br>Полное восстановление от 2 до 7 рабочих дней.<br>Значительное снижение производительности, касающееся безопасности важных данных.<br>Компания сталкивается с управляемыми осложнениями. |
| **4** | Критическое | Важные жизненно важные приложения и инфраструктура<br>не функционируют (время простоя) в течение **> 1 часа и до 6 часов**<br>*(например, электричество, вода, сети связи, системы безопасности и онлайн-системы)* | от 11% до 15% от балансовой стоимости актива | Операции выполняются на 80% ≤ X < 90%.<br>Полное восстановление от 8 до 15 рабочих дней.<br>Серьезное воздействие и потеря части критических конфиденциальных данных.<br>Компания испытывает серьезные трудности. |
| **5** | Катастрофическое | Важная жизненно важная инфраструктура не функционирует (время простоя)<br>в течение **более 6 часов**<br>*(например, электричество, вода, сети связи, системы безопасности и онлайн-системы)* | > 15% от балансовой стоимости актива | Операции выполняются при X < 80%.<br>Полное восстановление > 15 рабочих дней.<br>Крайне тяжелые последствия и потеря всех критически важных конфиденциальных данных.<br>Компания испытывает очень серьезные и фатальные трудности. |

---

---

## 3. Уровень риска
**Источник:** ISO 27005:2022 & Внутренние процедуры DetereCo (Внедрение управления ИТ-рисками)

> **Формула:** Уровень риска = Вероятность (P) × Воздействие (I)

### 3a. Классификация уровня риска

| Диапазон баллов (P × I) | Уровень риска | Цветовой индикатор | Действия по снижению риска |
|:---:|---|:---:|---|
| **1 – 5** | Низкий | 🟢 Светло-зеленый | Риск приемлем. Существующих средств контроля безопасности достаточно, достаточно регулярного мониторинга. |
| **6 – 11** | От низкого до среднего | 🟩 Темно-зеленый | Риск требует бдительности. Периодический анализ и планирование дополнительных средств контроля безопасности. |
| **12 – 15** | Средний | 🟡 Желтый | Риск необходимо контролировать. Периодический анализ и добавление профилактических мер среднего масштаба, обычно каждые **3–6 месяцев**. |
| **16 – 19** | От среднего до высокого | 🟧 Оранжевый | Риск неприемлем. Требует комплексных мер по снижению рисков архитектуры нулевого доверия (ZTA) в ближайшем будущем **(1–3 месяца)** для предотвращения критических инцидентов. |
| **20 – 25** | Высокий | 🔴 Красный | Наивысший приоритет обработки. Чрезвычайная ситуация, требующая комплексного снижения рисков сети и локализации для снижения уровня риска в течение **< 1 месяца**. |

### 3b. Матрица уровня риска

|  | **Воздействие 1** *(Незначительное)* | **Воздействие 2** *(Существенное)* | **Воздействие 3** *(Серьезное)* | **Воздействие 4** *(Критическое)* | **Воздействие 5** *(Катастрофическое)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Вероятность 5** *(Почти наверняка)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Вероятность 4** *(Весьма вероятно)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Вероятность 3** *(Вероятно)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Вероятность 2** *(Скорее маловероятно)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Вероятность 1** *(Маловероятно)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "ko": "## 1. 발생 가능성 척도
**출처:** ISO 27005:2022 & DetereCo 내부 절차 (IT 위험 관리 구현)

| 척도 | 범주 | 설명 |
|:---:|---|---|
| **1** | 희박함 | • 위험이 발생할 가능성이 매우 희박하며, 기껏해야 1년에 한 번 발생<br>• 발생 빈도 연간 < 0.1%<br>• 위험 발생 확률 0% ~ 19% |
| **2** | 다소 희박함 | • 위험이 드물게 발생하며, 아마도 1년에 두 번 정도 발생<br>• 발생 빈도 연간 0.1% ~ 1%<br>• 위험 발생 확률 20% ~ 39% |
| **3** | 가능성 있음 | • 위험이 발생한 적이 있지만 자주 발생하지는 않음; 1년에 세 번 발생<br>• 발생 빈도는 연간 1% ~ 1.5% 사이<br>• 위험 발생 확률 40% ~ 59% |
| **4** | 가능성 높음 | • 위험이 자주 발생하며, 1년에 여섯 번 발생<br>• 발생 빈도는 연간 1.5% ~ 2% 사이<br>• 발생 확률 60% ~ 79% |
| **5** | 거의 확실함 | • 위험이 항상 발생하며, 1년에 열두 번 발생<br>• 발생 빈도 연간 2% ~ 5%<br>• 발생 확률 80% ~ 100% |

---

---

## 2. 영향 척도
**출처:** ISO 27005:2022; DetereCo 내부 절차 (IT 위험 관리 구현); 및 DetereCo IT 자산 평가 양식 템플릿

> **자산 장부 금액** = 자산 취득 가격 − 감가상각누계액/손상차손
> 직접적인 영향을 받는 자산을 기준으로 계산합니다.

| 척도 | 범주 | 인프라 및 애플리케이션 시스템 | 재무적 영향 | 운영적 영향 |
|:---:|---|---|---|---|
| **1** | 미미함 | 덜 중요한 지원 애플리케이션 및 인프라가<br>**1일 동안** 작동하지 않음<br>*(예: 직원 근태 관리, 웹사이트, 프린터, HR 포털)* | 자산 장부 금액의 < 1% | 운영이 97% ≤ X < 100% 수준으로 실행됨.<br>당일 복구됨.<br>영향의 결과는 무시할 수 있음.<br>회사는 큰 어려움 없이 이를 극복할 수 있음. |
| **2** | 중요함 | 덜 중요한 지원 애플리케이션 및 인프라가<br>**1일 초과 3일 이하 동안** 작동하지 않음<br>*(예: 직원 근태 관리, 웹사이트, 프린터, HR 포털)* | 자산 장부 금액의 1% ~ 5% | 운영이 93% ≤ X < 97% 수준으로 실행됨.<br>최대 2영업일 이내에 완전히 복구됨.<br>활동 수행에 영향을 미침.<br>회사는 몇 가지 어려움에 직면함. |
| **3** | 심각함 | 중요하고 핵심적인 애플리케이션 및 인프라가<br>**< 1시간 동안** 작동하지 않음(다운타임)<br>*(예: 전기, 수도, 통신 네트워크, 보안 시스템 및 온라인 시스템)* | 자산 장부 금액의 5.1% ~ 10% | 운영이 90% ≤ X < 93% 수준으로 실행됨.<br>2~7영업일 이내에 완전히 복구됨.<br>중요한 데이터 보안과 관련된 주요 성능 저하.<br>회사는 관리 가능한 합병증에 직면함. |
| **4** | 치명적 | 중요하고 핵심적인 애플리케이션 및 인프라가<br>**> 1시간 초과 6시간 이하 동안** 작동하지 않음(다운타임)<br>*(예: 전기, 수도, 통신 네트워크, 보안 시스템 및 온라인 시스템)* | 자산 장부 금액의 11% ~ 15% | 운영이 80% ≤ X < 90% 수준으로 실행됨.<br>8~15영업일 이내에 완전히 복구됨.<br>심각한 영향 및 일부 핵심 기밀 데이터 손실.<br>회사는 심각한 어려움을 겪음. |
| **5** | 재앙적 | 중요하고 핵심적인 인프라가 **6시간 초과 동안**<br>작동하지 않음(다운타임)<br>*(예: 전기, 수도, 통신 네트워크, 보안 시스템 및 온라인 시스템)* | 자산 장부 금액의 > 15% | 운영이 X < 80% 수준으로 실행됨.<br>완전 복구 > 15영업일.<br>극도로 심각한 영향 및 모든 핵심 기밀 데이터 손실.<br>회사는 매우 심각하고 치명적인 어려움을 겪음. |

---

---

## 3. 위험 수준
**출처:** ISO 27005:2022 & DetereCo 내부 절차 (IT 위험 관리 구현)

> **공식:** 위험 수준 = 발생 가능성 (P) × 영향 (I)

### 3a. 위험 수준 분류

| 점수 범위 (P × I) | 위험 수준 | 색상 표시기 | 완화 조치 |
|:---:|---|:---:|---|
| **1 – 5** | 낮음 | 🟢 연두색 | 위험 수용 가능. 기존 보안 통제가 적절하며 정기적인 모니터링으로 충분함. |
| **6 – 11** | 낮음에서 보통 | 🟩 짙은 녹색 | 위험에 대한 경계 필요. 추가 보안 통제에 대한 주기적인 검토 및 계획. |
| **12 – 15** | 보통 | 🟡 노란색 | 위험을 모니터링해야 함. 일반적으로 **3~6개월**마다 중규모 예방 통제의 주기적인 검토 및 추가. |
| **16 – 19** | 보통에서 높음 | 🟧 주황색 | 위험 수용 불가. 심각한 사고를 예방하기 위해 가까운 시일 내에 **(1~3개월)** 포괄적인 ZTA 완화 조치가 필요함. |
| **20 – 25** | 높음 | 🔴 빨간색 | 처리 우선순위 최상. **< 1개월** 이내에 위험 수준을 낮추기 위해 포괄적인 네트워크 완화 및 억제가 필요한 비상 상황. |

### 3b. 위험 수준 매트릭스

|  | **영향 1** *(미미함)* | **영향 2** *(중요함)* | **영향 3** *(심각함)* | **영향 4** *(치명적)* | **영향 5** *(재앙적)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **발생 가능성 5** *(거의 확실함)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **발생 가능성 4** *(가능성 높음)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **발생 가능성 3** *(가능성 있음)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **발생 가능성 2** *(다소 희박함)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **발생 가능성 1** *(희박함)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
",
        "ja": "## 1. 可能性スケール
**出典:** ISO 27005:2022 & DetereCo 内部手順 (ITリスク管理の実装)

| スケール | カテゴリ | 説明 |
|:---:|---|---|
| **1** | 起こりそうにない | • リスクが発生する可能性は非常に低く、多くても年に1回<br>• 発生頻度 年間 < 0.1%<br>• リスクの発生確率 0% ～ 19% |
| **2** | あまり起こりそうにない | • リスクはまれに発生し、おそらく年に2回程度<br>• 発生頻度 年間 0.1% ～ 1%<br>• リスクの発生確率 20% ～ 39% |
| **3** | 起こり得る | • リスクは発生したことがあるが頻繁ではない。年に3回発生する<br>• 発生頻度は年間 1% ～ 1.5%<br>• リスクの発生確率は 40% ～ 59% |
| **4** | 可能性が高い | • リスクは頻繁に発生し、年に6回発生する<br>• 発生頻度は年間 1.5% ～ 2%<br>• 発生確率は 60% ～ 79% |
| **5** | ほぼ確実 | • リスクは常に発生し、年に12回発生する<br>• 発生頻度 年間 2% ～ 5%<br>• 発生確率 80% ～ 100% |

---

---

## 2. 影響スケール
**出典:** ISO 27005:2022。DetereCo 内部手順 (ITリスク管理の実装)。および DetereCo IT資産評価フォームテンプレート

> **資産帳簿価額** = 資産取得価格 − 減価償却累計額/減損損失
> 直接影響を受ける資産から計算されます。

| スケール | カテゴリ | インフラストラクチャおよびアプリケーションシステム | 財務的影響 | 運用的影響 |
|:---:|---|---|---|---|
| **1** | 軽微 | 重要度の低いサポートアプリケーションとインフラストラクチャが<br>**1日間**機能しない<br>*(例: 従業員の勤怠管理、ウェブサイト、プリンター、HRポータル)* | 資産帳簿価額の < 1% | オペレーションは 97% ≤ X < 100% で実行されます。<br>同日中に回復します。<br>影響の結果は無視できます。<br>会社は大きな困難なくこれを克服できます。 |
| **2** | 著しい | 重要度の低いサポートアプリケーションとインフラストラクチャが<br>**1日を超え3日間**機能しない<br>*(例: 従業員の勤怠管理、ウェブサイト、プリンター、HRポータル)* | 資産帳簿価額の 1% ～ 5% | オペレーションは 93% ≤ X < 97% で実行されます。<br>最大2営業日以内に完全に回復します。<br>活動パフォーマンスに影響を与えます。<br>会社はいくつかの困難に直面します。 |
| **3** | 深刻 | 重要な不可欠なアプリケーションとインフラストラクチャが<br>**< 1時間**機能しない（ダウンタイム）<br>*(例: 電気、水道、通信ネットワーク、セキュリティシステム、オンラインシステム)* | 資産帳簿価額の 5.1% ～ 10% | オペレーションは 90% ≤ X < 93% で実行されます。<br>2～7営業日以内に完全に回復します。<br>重要なデータセキュリティに関する大幅なパフォーマンス低下。<br>会社は管理可能な複雑さに直面します。 |
| **4** | 致命的 | 重要な不可欠なアプリケーションとインフラストラクチャが<br>**> 1時間を超え6時間まで**機能しない（ダウンタイム）<br>*(例: 電気、水道、通信ネットワーク、セキュリティシステム、オンラインシステム)* | 資産帳簿価額の 11% ～ 15% | オペレーションは 80% ≤ X < 90% で実行されます。<br>8～15営業日以内に完全に回復します。<br>深刻な影響と一部の重要な機密データの損失。<br>会社は深刻な困難を経験します。 |
| **5** | 壊滅的 | 重要な不可欠なインフラストラクチャが<br>**6時間を超えて**機能しない（ダウンタイム）<br>*(例: 電気、水道、通信ネットワーク、セキュリティシステム、オンラインシステム)* | 資産帳簿価額の > 15% | オペレーションは X < 80% で実行されます。<br>完全な回復 > 15営業日。<br>極めて深刻な影響とすべての重要な機密データの損失。<br>会社は非常に深刻で致命的な困難を経験します。 |

---

---

## 3. リスクレベル
**出典:** ISO 27005:2022 & DetereCo 内部手順 (ITリスク管理の実装)

> **公式:** リスクレベル = 可能性 (P) × 影響 (I)

### 3a. リスクレベルの分類

| スコア範囲 (P × I) | リスクレベル | カラーインジケーター | 緩和アクション |
|:---:|---|:---:|---|
| **1 – 5** | 低 | 🟢 薄緑 | リスクは許容範囲内です。既存のセキュリティコントロールは適切であり、定期的な監視で十分です。 |
| **6 – 11** | 低から中 | 🟩 濃緑 | リスクには警戒が必要です。追加のセキュリティコントロールの定期的なレビューと計画。 |
| **12 – 15** | 中 | 🟡 黄色 | リスクを監視する必要があります。定期的なレビューと、中規模の予防的コントロールの追加（通常は **3～6 か月** ごと）。 |
| **16 – 19** | 中から高 | 🟧 オレンジ | リスクは許容できません。重大なインシデントを防ぐために、近い将来 **(1～3 か月)** に包括的なZTA緩和アクションが必要です。 |
| **20 – 25** | 高 | 🔴 赤 | 最優先の対応が必要です。**1 か月未満** でリスクレベルを下げるために、包括的なネットワーク緩和と封じ込めを必要とする緊急事態。 |

### 3b. リスクレベルマトリックス

|  | **影響 1** *(軽微)* | **影響 2** *(著しい)* | **影響 3** *(深刻)* | **影響 4** *(致命的)* | **影響 5** *(壊滅的)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **可能性 5** *(ほぼ確実)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **可能性 4** *(可能性が高い)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **可能性 3** *(起こり得る)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **可能性 2** *(あまり起こりそうにない)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **可能性 1** *(起こりそうにない)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
"
      },
      