# Artifact Evaluation
**Dokumen:** Evaluasi Artefak Model Mitigasi Risiko Terintegrasi — DetereCo
**Standar:** ISO 27005:2022 · COBIT 2019 · NIST SP 800-207 · ISO 27002:2022

---

## Metodologi Evaluasi

Tahap Evaluasi dilakukan melalui serangkaian aktivitas terstruktur yang melibatkan evaluasi dari Para Ahli (Internal dan Eksternal) dengan rincian tahapan sebagai berikut:

**1. Expert Judgement (Skala Likert)**
Langkah pertama adalah menyajikan artefak konseptual kepada para ahli (Experts). Para ahli diminta memberikan penilaian kuantitatif deskriptif terhadap relevansi model menggunakan kuesioner Skala Likert dengan rentang 4 Poin untuk menghindari bias ketidaktegasan (mid point). Skala yang digunakan terdiri dari:
- **(1)** Sangat Tidak Relevan
- **(2)** Tidak Relevan
- **(3)** Relevan
- **(4)** Sangat Relevan

**2. Focus Group Discussion (FGD)**
Hasil penilaian kuantitatif deskriptif yang dinilai sangat tidak relevan dan tidak relevan oleh expert kemudian dibahas lebih dalam melalui diskusi terarah. Diskusi ini bertujuan untuk menggali alasan mendasar di balik penilaian tersebut, seperti *"mengapa komponen tersebut dianggap tidak relevan?"* atau *"Di mana letak kekurangan model tersebut?"*, sehingga diperoleh masukan kualitatif naratif yang konkret.

**3. Participant Validation**
Tahap akhir validasi adalah melakukan tinjauan ulang terhadap artefak yang telah direvisi. Aktivitas ini melibatkan para ahli (Expert) yang sama untuk meninjau hasil perbaikan dan mencapai kesepakatan (final agreement) bahwa artefak yang telah direvisi sudah relevan untuk digunakan sebagai panduan manajemen risiko keamanan siber di lingkungan DetereCo. Setelah kesepakatan tercapai, penelitian dilanjutkan ke penarikan Kesimpulan dan Saran.

---

## Hasil Kuesioner Expert Judgement

| Jenis Ancaman | Skala 1 | Skala 2 | Skala 3 | Skala 4 | Skala Modus | Interpretasi |
|---|:---:|:---:|:---:|:---:|:---:|---|
| T.10 Industrial Espionage (Spionase Industri) | 0 | 0 | 3 | 6 | **4** | ✅ Sangat Relevan |
| T.11 Disaster / Bencana | 0 | 0 | 4 | 5 | **4** | ✅ Sangat Relevan |
| T.09 Ransomware & Malware Injection | 0 | 0 | 4 | 5 | **4** | ✅ Sangat Relevan |
| T.04 API & Integration Vulnerabilities | 0 | 0 | 5 | 4 | **3** | ✅ Relevan |
| T.07 Replay Attacks | 0 | 0 | 2 | 7 | **4** | ✅ Sangat Relevan |
| T.02 Insider Threats | 0 | 1 | 6 | 2 | **3** | ✅ Relevan |
| T.03 Supply Chain Attacks | 0 | 0 | 5 | 4 | **3** | ✅ Relevan |
| T.05 Lateral Movement | 0 | 0 | 4 | 5 | **4** | ✅ Sangat Relevan |
| T.08 Advanced Persistent Threats (APT) | 0 | 0 | 4 | 5 | **4** | ✅ Sangat Relevan |
| T.01 Compromised Credentials | 0 | 0 | 3 | 6 | **4** | ✅ Sangat Relevan |
| T.06 IoT/OT Vulnerabilities | 0 | 0 | 5 | 4 | **3** | ✅ Relevan |

---

## Catatan Ahli & Hasil Focus Group Discussion (FGD)

---

### T.10 · Industrial Espionage (Spionase Industri)

**Catatan Ahli:**
> Saran Tambahan Kontrol: **8.1 User endpoint devices** — Informasi yang tersimpan atau diakses melalui user endpoint devices dapat mencakup rahasia dagang, intellectual property, dan informasi bisnis strategis. Kontrol ini diperlukan untuk mencegah akses, pengungkapan, atau pencurian informasi oleh pihak yang tidak berwenang.

*— Consulting Manager PT. Perisai Digital Indonesia (Cisometric)*

**Rancangan Awal Kontrol:**
- 8.12 Data leakage prevention
- 8.3 Information access restriction
- 5.12 Classification of information
- 8.15 Logging

**Isi Diskusi FGD:**
Menurut ahli Consulting Manager PT. Perisai Digital Indonesia (Cisometric) dapat ditambahkan kontrol 8.1 User endpoint devices dengan pernyataan *"Dapat mencegah akses, pengungkapan atau pencurian informasi oleh pihak tidak berwenang"*. Forum sepakat menambah kontrol karena spionase industri sering melalui laptop karyawan atau workstation lab.

**Hasil Perubahan:**
- 8.12 Data leakage prevention
- 8.3 Information access restriction
- 5.12 Classification of information
- 8.15 Logging
- **8.1 User endpoint devices** *(tambahan)*

---

### T.09 · Ransomware & Malware Injection

**Catatan Ahli:**
> Saran Tambahan Kontrol: **8.15 Logging** — Sebagai bentuk pencatatan yang akan dilihat dan mendukung kontrol 8.16 Monitoring Activity.

*— Supervisor Keamanan TI*

**Rancangan Awal Kontrol:**
- 8.8 Technical Vulnerability Management
- 8.7 Protection against malware
- 8.16 Monitoring activities
- 5.26 Response to information security incidents
- 8.13 Information backup

**Isi Diskusi FGD:**
Menurut ahli Supervisor Keamanan TI DetereCo dapat menambahkan kontrol 8.15 Logging dengan pernyataan *"Mampu mencatat seluruh percobaan penyusupan dan mendukung kontrol 8.16 Monitoring Activity"*. Forum sepakat menambah kontrol karena menyediakan rekam jejak untuk deteksi ancaman sedini mungkin dan menganalisis akar masalah pasca insiden.

**Hasil Perubahan:**
- 8.8 Technical Vulnerability Management
- 8.7 Protection against malware
- 8.16 Monitoring activities
- 5.26 Response to information security incidents
- 8.13 Information backup
- **8.15 Logging** *(tambahan)*

---

### T.04 · API & Integration Vulnerabilities

**Catatan Ahli:**
> Saran Tambahan Kontrol:
> - **8.27 Secure System Architecture and Engineering Principles** — Hasil penetration testing menunjukkan bahwa API Key dapat terekspos. Hal ini mengindikasikan bahwa prinsip secure by design belum diterapkan secara optimal.
> - **5.12 Classification of Information** — Mengkategorikan data keluar melalui API dan data yang tidak boleh.

*— Consulting Manager PT. Perisai Digital Indonesia (Cisometric) & Manager Perencanaan & Strategi TI*

**Rancangan Awal Kontrol:**
- 8.5 Secure authentication
- 8.26 Application security requirements
- 8.22 Segregation of networks

**Isi Diskusi FGD:**
Menurut ahli Consulting Manager Cisometric dapat menambahkan kontrol 8.27 menyatakan *"Hasil Penetration testing mengindikasikan prinsip secure by design belum diterapkan secara optimal."* Forum sepakat menambahkan kontrol karena selaras dengan prinsip Tenet 3 yaitu per sesi.

Menurut ahli Manager Perencanaan & Strategi TI DetereCo perlu menambahkan kontrol 5.12 menyatakan *"Diperlukan pengkategorian data boleh dan tidak keluar melalui API"*. Forum sepakat menambahkan kontrol karena memastikan API memblokir otomatis data berklasifikasi "Rahasia".

**Hasil Perubahan:**
- 8.5 Secure authentication
- 8.26 Application security requirements
- 8.22 Segregation of networks
- **8.27 Secure System Architecture and Engineering Principles** *(tambahan)*
- **5.12 Classification of Information** *(tambahan)*

---

### T.07 · Replay Attacks

**Catatan Ahli:** *(Tidak ada catatan tambahan dari ahli)*

**Rancangan Awal Kontrol:**
- 8.5 Secure authentication
- 8.24 Use of cryptography

**Hasil Perubahan:** Tidak ada perubahan.

---

### T.02 · Insider Threats

**Catatan Ahli:**
> **Masukan GMO:** Ahli memberi catatan *"Klarifikasi kembali pada GMO COBIT 2019 adanya sesuatu yang Implemented but Not Documented"* karena ada perubahan Mutasi yang tidak tercatat dengan baik terutama di Dokumen SLA.
>
> Saran Tambahan Kontrol:
> - **6.2 Terms and conditions of employment** — Dasar adanya persetujuan karyawan menjaga keamanan informasi.
> - **6.4 Disciplinary process** — Secara historis ada kejadian sehingga memerlukan mekanisme formal aksi pendisiplinan.
> - **6.3 Information Security Awareness, Education, and Training** — Membekali karyawan agar dengan sadar menjaga data penting perusahaan.
> - **5.32 Intellectual Property Rights** — Agar mengunci IP perusahaan tidak ditiru dari scratch meskipun bukan bentuk pencurian langsung.
> - **7.2 Physical Entry** — Akses masuk karyawan pakai IDCard jadi yang dimutasi harusnya langsung dinonaktifkan.

*— IT Security Risk PT. Citilink Indonesia · Consulting Manager PT. Perisai Digital Indonesia (Cisometric) · Researcher Telkom University · Supervisor Keamanan TI · Manager Perencanaan & Strategi TI*

**Rancangan Awal:**
- GMO: APO12.04 (Level 4 - 50%) · APO12.03 (Level 4 - 75%)
- Kontrol: 5.18 Access rights · 8.3 Information access restriction · 6.5 Termination/change of employment · 8.16 Monitoring activities

**Isi Diskusi FGD:**
Forum bersama ahli IT Security Risk PT. Citilink Indonesia sepakat untuk mempertahankan Practice GMO dikarenakan APO12.03 Level 2 dan Level 3 sudah Fully sehingga hanya perlu memaksimalkan APO12.03 Level 4 agar dapat mendokumentasikan perubahan Mutasi tercatat dengan baik terutama pada Dokumen SLA.

Menurut ahli Consulting Manager Cisometric perlu menambahkan kontrol 6.2 menyatakan *"dasar adanya persetujuan karyawan menjaga keamanan informasi"* karena dapat meningkatkan kesadaran untuk melakukan aksi pembocoran informasi rahasia.

Menurut ahli Supervisor Keamanan TI dan Manager Perencanaan & Strategi TI DetereCo menambahkan kontrol 5.32 karena mencegah pencurian atau replikasi Kekayaan Intelektual oleh mantan pegawai meskipun bukan pencurian langsung, dan kontrol 7.2 sebagai bentuk penguatan akses IDCard bagi karyawan yang dimutasi perlu dilakukan otomatisasi nonaktif.

Forum diskusi sepakat **tidak** menambahkan kontrol 6.4 karena telah adanya proses tindak lanjut berupa SPT (Surat Peringatan Tertulis) bagi pelaku di masa lalu. Forum juga **tidak** menambahkan kontrol 6.3 karena kontrol ini akan difokuskan terlebih dahulu ke ancaman T.01 Compromised Credentials.

**Hasil Perubahan:**
- GMO: **Tidak ada perubahan**
- Kontrol ISO (diperbarui):
  - 5.18 Access rights
  - 8.3 Information access restriction
  - 6.5 Termination/change of employment
  - 8.16 Monitoring activities
  - **6.2 Terms and conditions of employment** *(tambahan)*
  - **5.32 Intellectual Property Rights** *(tambahan)*
  - **7.2 Physical Entry** *(tambahan)*

---

### T.03 · Supply Chain Attacks

**Catatan Ahli:**
> Saran Tambahan Kontrol:
> - **5.20 Addressing information security within supplier agreements** — Perlu membuat VSAR (Vendor Security Assessment Risk) sebagai bentuk Due Diligent agar mengetahui sejauh mana Vendor mengaplikasikan ISMS-nya.
> - **5.21 Managing information security in the ICT supply chain** *(tidak dimasukkan ke revisi — fokus kontrol tidak relevan menyelesaikan masalah T.03)*
> - **8.3 Information Access Restriction** *(tidak dimasukkan — bersifat opsional)*
> - **6.7 Remote Working** — Menegakkan aturan menggunakan Perangkat Pribadi BYOD saat di luar perusahaan ketika terhubung ke Jaringan Luar; berguna untuk pegawai role Sales.

*— Sr. IT GRC Consultant PT. Perisai Digital Indonesia (Cisometric) · Researcher Telkom University · Supervisor Keamanan TI · Manager Perencanaan & Strategi TI*

**Rancangan Awal Kontrol:**
- 5.14 Information transfer
- 5.19 Information security in supplier relationships
- 8.24 Use of cryptography

**Isi Diskusi FGD:**
Menurut ahli Sr. IT GRC Consultant Cisometric menambahkan kontrol 5.20 menyatakan *"Dengan kontrol ini dapat membuat VSAR sebagai bentuk Due Diligent perusahaan agar mengetahui sejauh mana Vendor mengaplikasikan ISMS"*.

Menurut Manager Perencanaan & Strategi TI DetereCo menambahkan kontrol 6.7 menyatakan *"Demi menegakkan aturan menggunakan Perangkat Pribadi BYOD saat di luar perusahaan ketika terhubung ke Jaringan Luar seperti kasus pegawai dengan role sales"*.

Forum diskusi sepakat tidak menambahkan kontrol 5.21 karena fokus kontrol tidak relevan dalam menyelesaikan masalah serangan dan juga tidak menambahkan kontrol 8.3 karena kurangnya kemampuan sistem untuk memvalidasi keabsahan pengirim pesan dari luar jaringan (external spoofing).

**Hasil Perubahan:**
- 5.14 Information transfer
- 5.19 Information security in supplier relationships
- 8.24 Use of cryptography
- **5.20 Addressing information security within supplier agreements** *(tambahan)*
- **6.7 Remote Working** *(tambahan)*

---

### T.05 · Lateral Movement

**Catatan Ahli:**
> Saran Tambahan Kontrol:
> - **8.16 Monitoring activities** — Monitoring aktivitas secara berkelanjutan dapat membantu mendeteksi pola akses dan komunikasi internal yang tidak normal yang mengindikasikan upaya lateral movement.
> - **8.7 Protection against malware** — Karena ancaman ini biasanya berjalan di atas malware sehingga dengan adanya kontrol ini mengurangi salah satu penyebab terjadinya Lateral Movement.

*— Consulting Manager PT. Perisai Digital Indonesia (Cisometric) · Supervisor Keamanan TI*

**Rancangan Awal Kontrol:**
- 8.22 Segregation of networks
- 5.15 Access control
- 8.23 Web filtering

**Isi Diskusi FGD:**
Menurut Consulting Manager Cisometric menambahkan kontrol 8.16 menyatakan *"Membantu mendeteksi pola akses dan komunikasi internal yang tidak normal"*. Forum sepakat menambahkan kontrol ini karena sebagai bentuk pendeteksi anomalous internal traffic.

Menurut Supervisor Keamanan TI DetereCo menambahkan kontrol 8.7 menyatakan *"Membantu menutup satu penyebab terjadinya ancaman ini"*. Forum sepakat menambahkan kontrol 8.7 karena penerapan anti-malware pada level endpoint akan membunuh kapabilitas proksimal dari infeksi malware (seperti penyebaran worm).

**Hasil Perubahan:**
- 8.22 Segregation of networks
- 5.15 Access control
- 8.23 Web filtering
- **8.16 Monitoring activities** *(tambahan)*
- **8.7 Protection against malware** *(tambahan)*

---

### T.08 · Advanced Persistent Threats (APT)

**Catatan Ahli:**
> Saran Tambahan Kontrol: **5.7 Threat intelligence** — Threat intelligence membantu organisasi memahami karakteristik, metode, dan indikator yang digunakan oleh APT sehingga ancaman tersebut dapat dideteksi dan dimitigasi secara proaktif.

*— Consulting Manager PT. Perisai Digital Indonesia (Cisometric)*

**Rancangan Awal Kontrol:**
- 8.8 Management of technical vulnerabilities
- 8.7 Protection against malware

**Isi Diskusi FGD:**
Menurut Consulting Manager Cisometric menambahkan kontrol 5.7 menyatakan *"membantu organisasi memahami karakteristik, metode, dan indikator yang digunakan oleh APT sehingga ancaman tersebut dapat dideteksi dan dimitigasi secara proaktif"*. Forum sepakat menambahkan kontrol 5.7 karena mampu memberikan Indicator of Compromise (IoC) dan TTPs (Tactics, Techniques, and Procedures) terbaru ke dalam perangkat keamanan yang dimiliki perusahaan.

**Hasil Perubahan:**
- 8.8 Management of technical vulnerabilities
- 8.7 Protection against malware
- **5.7 Threat intelligence** *(tambahan)*

---

### T.01 · Compromised Credentials

**Catatan Ahli:**
> **Masukan GMO:** APO12.06 Level 4 — perhatikan.

*— IT Security Risk PT. Citilink Indonesia*

**Rancangan Awal:**
- GMO: APO12.02 Menganalisis Risiko (Level 3 - 83%) · APO12.06 Menanggapi Risiko (Level 5 - 0%)

**Isi Diskusi FGD:**
Forum diskusi sepakat mempertahankan APO12.06 Level 5 karena poin pengisian praktik ini mensyaratkan menyampaikan perbaikan proses kepada pemangku kepentingan yang relevan. Oleh karena itu apabila praktik ini dijalankan sesuai best practice maka solusi kewajiban MFA bagi satu perusahaan dapat terlaksana untuk mengurangi risiko ancaman kebocoran kredensial.

**Hasil Perubahan:** Tidak ada perubahan.

---

### T.06 · IoT/OT Vulnerabilities

**Catatan Ahli:**
> Saran Tambahan Kontrol:
> - **5.14 Information Transfer** — Karena IoT datanya ditarik keluar melalui jaringan yang terpisah sehingga perlu kontrol ini untuk memastikan proses pemindahan informasi berjalan sesuai Best Practice.
> - **5.15 Access Control** — Untuk menegakkan hak akses minimum dalam menjalankan tugas setiap karyawan.
> - **8.22 Segregation of Networks** — Perlu adanya pemisahan antara lalu lintas jaringan OT dan IT.

*— Manager Infrastruktur & Keamanan TI · Manager Perencanaan & Strategi TI · Supervisor Keamanan TI*

**Rancangan Awal Kontrol:**
- 5.9 Inventory of information and other associated assets
- 8.16 Monitoring activities

**Isi Diskusi FGD:**
Menurut Manager Infrastruktur & Keamanan TI DetereCo menambahkan kontrol 5.14 menyatakan *"Perangkat IoT yang diambil datanya perlu adanya kontrol yang mengawasi pemindahan informasi berjalan sesuai best practice"*. Forum sepakat menambahkan kontrol 5.14 karena perlu dipastikan jalur pengiriman konten data tersebut aman dari intersepsi/penyadapan.

Menurut Manager Perencanaan & Strategi TI DetereCo menambahkan kontrol 5.15 menyatakan *"Mendukung penegakan hak akses minimum (least privilege) dalam menjalankan peran setiap karyawan"*. Forum sepakat menambahkan kontrol 5.15 karena diperlukan aturan otorisasi ketat siapa yang boleh memberikan instruksi kerja perangkat IoT.

Menurut Supervisor Keamanan TI DetereCo menambahkan kontrol 8.22 menyatakan *"Sebagai penegak pemisahan lalu lintas jaringan antara OT dan IT"*. Forum sepakat menambahkan kontrol 8.22 karena mampu mencegah lalu lintas anomali yang mampu melumpuhkan salah satu mesin produksi IoT (DoS).

**Hasil Perubahan:**
- 5.9 Inventory of information and other associated assets
- 8.16 Monitoring activities
- **5.14 Information Transfer** *(tambahan)*
- **5.15 Access Control** *(tambahan)*
- **8.22 Segregation of Networks** *(tambahan)*

---

## Hasil Participant Validation

| Jenis Ancaman | Hasil Validasi |
|---|:---:|
| T.10 Industrial Espionage (Spionase Industri) | ✅ Disepakati |
| T.11 Disaster / Bencana | ✅ Disepakati |
| T.09 Ransomware & Malware Injection | ✅ Disepakati |
| T.04 API & Integration Vulnerabilities | ✅ Disepakati |
| T.07 Replay Attacks | ✅ Disepakati |
| T.02 Insider Threats | ✅ Disepakati |
| T.03 Supply Chain Attacks | ✅ Disepakati |
| T.05 Lateral Movement | ✅ Disepakati |
| T.08 Advanced Persistent Threats (APT) | ✅ Disepakati |
| T.01 Compromised Credentials | ✅ Disepakati |
| T.06 IoT/OT Vulnerabilities | ✅ Disepakati |

> **Seluruh 11 ancaman dinyatakan DISEPAKATI** oleh para ahli setelah melalui proses Expert Judgement, FGD, dan Participant Validation.

---

## Ringkasan Perubahan Kontrol ISO 27002:2022

| ID | Jenis Ancaman | Kontrol Ditambahkan |
|---|---|---|
| T.10 | Industrial Espionage | 8.1 User endpoint devices |
| T.09 | Ransomware & Malware Injection | 8.15 Logging |
| T.04 | API & Integration Vulnerabilities | 8.27 Secure System Architecture · 5.12 Classification of Information |
| T.02 | Insider Threats | 6.2 Terms and conditions of employment · 5.32 Intellectual Property Rights · 7.2 Physical Entry |
| T.03 | Supply Chain Attacks | 5.20 Supplier agreements · 6.7 Remote Working |
| T.05 | Lateral Movement | 8.16 Monitoring activities · 8.7 Protection against malware |
| T.08 | APT | 5.7 Threat intelligence |
| T.06 | IoT/OT Vulnerabilities | 5.14 Information Transfer · 5.15 Access Control · 8.22 Segregation of Networks |
| T.11 | Disaster / Bencana | *(tidak ada perubahan)* |
| T.07 | Replay Attacks | *(tidak ada perubahan)* |
| T.01 | Compromised Credentials | *(tidak ada perubahan)* |

---

*Sumber: Artifact Evaluation — IT Risk Assessment PT DI (DetereCo)*
