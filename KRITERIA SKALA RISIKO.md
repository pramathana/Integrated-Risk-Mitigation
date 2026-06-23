# Kriteria Skala & Level Risiko IT
**Sumber:** ISO 27005:2022 & Prosedur Internal PT DI (Pelaksanaan Manajemen Risiko TI)

---

## 1. Skala Kemungkinan (Likelihood)

| Skala | Kategori | Frekuensi | Probabilitas |
|:---:|---|---|---|
| **1** | Hampir Tidak Pernah Terjadi *(Unlikely)* | Paling banyak 1× dalam setahun | 0% – 19% |
| **2** | Jarang Terjadi *(Rather Unlikely)* | Hanya 2× dalam setahun | 20% – 39% |
| **3** | Bisa / Mungkin Terjadi *(Likely)* | Terjadi 3× dalam setahun | 40% – 59% |
| **4** | Sering Terjadi *(Very Likely)* | Terjadi 6× dalam setahun | 60% – 79% |
| **5** | Hampir Pasti Terjadi *(Almost Certain)* | Terjadi 12× dalam setahun | 80% – 100% |

### Detail Deskripsi Kriteria Kemungkinan

| Skala | Kategori | Deskripsi |
|:---:|---|---|
| 1 | Hampir Tidak Pernah Terjadi | Risiko mungkin terjadi sangat jarang, paling banyak satu kali dalam setahun. Frekuensi kejadian < 0,1% dalam setahun. |
| 2 | Jarang Terjadi | Risiko jarang terjadi, mungkin terjadi hanya dua kali dalam setahun. Frekuensi kejadian dari 0,1% s/d 1% dalam setahun. |
| 3 | Bisa / Mungkin Terjadi | Risiko pernah terjadi namun tidak sering, terjadi tiga kali dalam setahun. Frekuensi kejadian di atas 1% s/d 1,5% dalam setahun. |
| 4 | Sering Terjadi | Risiko sering terjadi, terjadi enam kali dalam setahun. Frekuensi kejadian di atas 1,5% s/d 2% dalam setahun. |
| 5 | Hampir Pasti Terjadi | Risiko selalu terjadi, terjadi dua belas kali dalam setahun. Frekuensi kejadian dari 2% s/d 5% dalam setahun. |

---

## 2. Skala Dampak (Impact)

> **Nilai Buku Asset** = Harga Perolehan Aset − Akumulasi Penyusutan/Impairment
> Dihitung dari aset yang terdampak langsung.

### 2a. Dampak terhadap Sistem Infrastruktur & Aplikasi

| Skala | Kategori | Deskripsi Sistem |
|:---:|---|---|
| **1** | Sangat Rendah *(Minor)* | Aplikasi & infrastruktur pendukung yang kurang penting tidak berfungsi selama **1 hari** *(mis. absen karyawan, website, printer, portal HR)* |
| **2** | Rendah *(Significant)* | Aplikasi dan infrastruktur pendukung yang kurang penting tidak berfungsi selama **lebih dari 1 hari s/d 3 hari** *(mis. absen karyawan, website, printer, portal HR)* |
| **3** | Sedang *(Serious)* | Aplikasi dan infrastruktur vital yang penting tidak berfungsi (Downtime) selama **< 1 jam** *(mis. listrik, air, jaringan komunikasi, sistem keamanan & online system)* |
| **4** | Tinggi *(Critical)* | Aplikasi dan infrastruktur vital yang penting tidak berfungsi (Downtime) selama **> 1 jam s/d 6 jam** *(mis. listrik, air, jaringan komunikasi, sistem keamanan & online system)* |
| **5** | Sangat Tinggi *(Catastrophic)* | Infrastruktur vital yang penting tidak berfungsi (Downtime) selama **lebih dari 6 jam** *(mis. listrik, air, jaringan komunikasi, sistem keamanan & online system)* |

### 2b. Dampak Keuangan

| Skala | Kategori | Kerugian Finansial |
|:---:|---|---|
| 1 | Sangat Rendah | < 1% dari nilai buku aset |
| 2 | Rendah | 1% s/d 5% dari nilai buku aset |
| 3 | Sedang | 5,1% s/d 10% dari nilai buku aset |
| 4 | Tinggi | 11% s/d 15% dari nilai buku aset |
| 5 | Sangat Tinggi | > 15% dari nilai buku aset |

### 2c. Dampak Operasional

| Skala | Kategori | Deskripsi Operasional |
|:---:|---|---|
| **1** | Sangat Rendah | Operasional berjalan 97% ≤ X < 100%. Pulih di hari yang sama. Konsekuensi dampak dapat diabaikan. Perusahaan mampu mengatasi tanpa banyak kesulitan. |
| **2** | Rendah | Operasional berjalan 93% ≤ X < 97%. Pulih total maksimum 2 hari kerja. Berpengaruh pada kinerja aktivitas. Perusahaan menghadapi beberapa kesulitan. |
| **3** | Sedang | Operasional berjalan 90% ≤ X < 93%. Pulih total antara 2–7 hari kerja. Penurunan besar kinerja terhadap keamanan data penting. Perusahaan menghadapi komplikasi yang dapat ditangani. |
| **4** | Tinggi | Operasional berjalan 80% ≤ X < 90%. Pulih total 8–15 hari kerja. Dampak serius dan hilangnya sebagian data kritikal rahasia. Perusahaan mengalami kesulitan serius. |
| **5** | Sangat Tinggi | Operasional berjalan X < 80%. Pulih total > 15 hari kerja. Dampak sangat ekstrim dan hilangnya seluruh data kritikal rahasia. Perusahaan mengalami kesulitan sangat parah dan fatal. |

---

## 3. Level Risiko (Risk Level)

> **Formula:** Level Risiko = Kemungkinan (P) × Dampak (I)

### 3a. Klasifikasi Level Risiko

| Rentang Nilai (P × I) | Tingkat Risiko | Indikator Warna | Tindakan Mitigasi |
|:---:|---|:---:|---|
| **1 – 5** | Rendah *(Low)* | 🟢 Hijau Muda | Risiko dapat diterima *(Acceptable)*. Kontrol keamanan yang ada sudah memadai, cukup lakukan pemantauan rutin. |
| **6 – 11** | Rendah–Menengah *(Low to Moderate)* | 🟩 Hijau Gelap | Risiko memerlukan kewaspadaan. Tinjauan berkala dan perencanaan penambahan kontrol keamanan. |
| **12 – 15** | Menengah *(Moderate)* | 🟡 Kuning | Risiko wajib diwaspadai. Tinjauan berkala dan penambahan kontrol preventif berskala menengah, biasanya setiap **3–6 bulan**. |
| **16 – 19** | Menengah–Tinggi *(Moderate to High)* | 🟠 Orange | Risiko tidak dapat diterima. Membutuhkan tindakan mitigasi ZTA yang komprehensif dalam waktu dekat **(1–3 bulan)** untuk mencegah insiden kritis. |
| **20 – 25** | Tinggi *(High)* | 🔴 Merah | Prioritas penanganan utama. Kondisi darurat yang mewajibkan mitigasi dan penyekatan jaringan secara menyeluruh guna menurunkan level risiko dalam waktu **< 1 bulan**. |

### 3b. Matriks Level Risiko

|  | **Dampak 1** *(Minor)* | **Dampak 2** *(Significant)* | **Dampak 3** *(Serious)* | **Dampak 4** *(Critical)* | **Dampak 5** *(Catastrophic)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Kemungkinan 5** *(Almost Certain)* | 🟩 7 | 🟡 12 | 🟠 17 | 🔴 22 | 🔴 25 |
| **Kemungkinan 4** *(Very Likely)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟠 19 | 🔴 24 |
| **Kemungkinan 3** *(Likely)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟠 18 | 🔴 23 |
| **Kemungkinan 2** *(Rather Unlikely)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟠 16 | 🔴 21 |
| **Kemungkinan 1** *(Unlikely)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |

### 3c. Legenda Matriks

| Simbol | Level | Rentang |
|:---:|---|---|
| 🟢 | Low | 1 – 5 |
| 🟩 | Low to Moderate | 6 – 11 |
| 🟡 | Moderate | 12 – 15 |
| 🟠 | Moderate to High | 16 – 19 |
| 🔴 | High | 20 – 25 |

---

*Sumber: ISO 27005:2022 & Prosedur Internal PT DI (Pelaksanaan Manajemen Risiko TI)*
