# IT Risk Assessment Fix
**Sumber:** Sheet "IT RISK ASSESSMENT FIX" — PT DI (DetereCo)
**Standar:** ISO 27005:2022 · ZTA ZTMM by CISA · Prosedur Internal PT DI

---

## Ringkasan Eksekutif

| ID | Jenis Ancaman | Layer | Kemungkinan | Dampak | Level Risiko | ZTA Maturity |
|:---:|---|---|:---:|:---:|:---:|:---:|
| T.01 | Compromised Credentials | Identity | 3 | 1 | 🟢 3 Low | Traditional |
| T.02 | Insider Threats | Identity | 2 | 2 | 🟩 6 Low to Moderate | Traditional |
| T.03 | Supply Chain Attacks | Application | 1 | 2 | 🟢 5 Low | Initial |
| T.04 | API & Integration Vulnerabilities | Application | 3 | 2 | 🟩 8 Low to Moderate | Traditional |
| T.05 | Lateral Movement | Network | 4 | 1 | 🟢 4 Low | Initial |
| T.06 | IoT/OT Vulnerabilities | Network | 1 | 1 | 🟢 1 Low | Traditional |
| T.07 | Replay Attacks | Network | 3 | 2 | 🟩 8 Low to Moderate | Traditional |
| T.08 | Advanced Persistent Threats (APT) | Infrastructure | 4 | 1 | 🟢 4 Low | Traditional |
| T.09 | Ransomware & Malware Injection | Infrastructure | 3 | 3 | 🟡 13 Moderate | Traditional |
| T.10 | Industrial Espionage | Data | 1 | 4 | 🟡 15 Moderate | Traditional |
| T.11 | Disaster / Bencana | Infrastructure | 1 | 4 | 🟡 15 Moderate | Traditional |

---

## Detail Penilaian Risiko

---

### T.01 · Compromised Credentials
**PIC:** J | **Layer:** Identity Layer | **Level Risiko:** 🟢 3 Low | **ZTA Maturity:** Traditional

**Target Spesifik:**
- Akun Admin Sistem
- Akses Remote VPN
- Kredensial Pengguna / SAP Cloud Identity Access Management (CIAM)
- Token Akses API & Kunci Enkripsi

**Serangan yang Terjadi:**
Pencurian dan penyalahgunaan kredensial (username dan password) melalui **Email Phishing**.

**Kronologi / Skenario Serangan:**
1. Penyerang mengirimkan email phishing kepada pengguna (karyawan perusahaan).
2. Ketika pengguna mengklik tautan dalam email, mereka diarahkan ke tampilan portal palsu yang menyerupai portal resmi.
3. Pengguna yang tertipu memasukkan username dan password ke portal palsu sehingga kredensial dicuri dan akun menjadi compromised (diambil alih).
4. Kejadian ini dilaporkan pernah dialami oleh hampir semua divisi di perusahaan.

**Kontrol Keamanan Eksisting:**
- Isolasi pengguna dan pembekuan akun yang terdampak phishing secara langsung.
- Pemulihan pengaturan akun yang diubah penyerang (seperti akses sharing file) ke pengaturan awal.
- Perubahan kredensial username dan kata sandi akun yang berhasil diretas.
- Anjuran penerapan Multi-Factor Authentication (MFA) kepada pengguna.
- Penerapan Single Sign-On (SSO) pada beberapa aplikasi internal dengan otomasi batas jumlah karakter dan email pemulihan.
- Kebijakan pengaturan kata sandi tradisional pada sistem email.

**Evidence:** Tidak ada

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **3** | Insiden pencurian kredensial diperkirakan terjadi minimal 4× dalam setahun |
| **Level Dampak** | **1** | Tidak ada kerugian finansial; hanya gangguan operasional sangat minimal dan potensi penurunan reputasi |
| **Level Risiko** | **3 Low** | P(3) × I(1) = 3 |

**ZTA Maturity — Traditional**

*Pilar: Identity*
- Authentication
- Automation and Orchestration Capability
- Governance Capability

*Alasan:*
- Bergantung pada password
- MFA belum diwajibkan
- Tindakan mitigasi reaktif dan manual (belum ada sistem evaluasi otomatis ketat)
- Kebijakan tata kelola statis sebatas pengaturan password

---

### T.02 · Insider Threats
**PIC:** F | **Layer:** Identity Layer | **Level Risiko:** 🟩 6 Low to Moderate | **ZTA Maturity:** Traditional

**Target Spesifik:**
- Data Rahasia Perusahaan
- Konfigurasi Sistem Keamanan
- Akses Administratif Lokal (Privileged Access)
- Data Laporan Keuangan

**Serangan yang Terjadi:**
Pembocoran informasi atau ancaman siber yang aktornya berasal dari **internal perusahaan (pegawai)**.

**Kronologi / Skenario Serangan (Historis 3 Kasus):**

*Kasus 1 — Pembocoran Surat Edaran:*
- Perusahaan mendistribusikan surat edaran internal melalui email namun tidak boleh dipublikasikan ke luar.
- Seorang pegawai membocorkan surat edaran tersebut ke wartawan/orang luar.
- Dampak: pemberitaan di TV Nasional, kegaduhan, dan penundaan kontrak kepada klien.
- Sanksi: Pelaku diberikan SPT (Surat Peringatan Tertulis).

*Kasus 2 — Penyalahgunaan Hak Akses SAP akibat Mutasi:*
- Pegawai divisi keuangan diberi hak akses SAP untuk laporan keuangan.
- Pegawai dimutasi ke divisi Aircraft Services (ACS) tanpa notifikasi otomatis dari HC ke IT.
- Tim IT tidak mencabut hak akses keuangan di SAP.
- Oknum pegawai memanfaatkan sisa hak aksesnya untuk melihat laporan keuangan secara diam-diam.

*Kasus 3 — Indikasi Dokumen Kontrak Sensitif Bocor (Tanpa Investigasi Lanjut):*
- Terdapat oknum internal yang diduga menyebarkan dokumen kontrak.
- Nominal finansial dan jumlah yang sama persis dengan hasil rapat internal menjadi indikasi kebocoran.
- Karena keterbatasan bukti, kasus tidak diinvestigasi lebih lanjut.

**Kontrol Keamanan Eksisting:**
- Otomatisasi penonaktifan akun SAP hanya untuk kasus resign; kasus mutasi belum diterapkan.
- Sistem non-SAP: penonaktifan masih manual berdasarkan nota CC dari HC.
- Filtering email: memblokir pengiriman file sensitif berekstensi `.db` dan `.CAD`.
- Inisiasi mekanisme pemantauan dan evaluasi ribuan role di SAP (non-teknis, belum selesai).
- Kebijakan Kontrol Hak Akses SAP tersedia namun tidak mencantumkan batas waktu penyelesaian spesifik.

**Evidence:** Adanya pelaku yang terbukti menyebarkan Surat Edaran non-public dan diberikan SPT.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **2** | Tidak terjadi terus-menerus; secara historis 1 kejadian, diasumsikan 1× dalam 6 bulan |
| **Level Dampak** | **2** | Kerugian Rp 7 Miliar vs. revenue perusahaan tiga digit Miliar → memenuhi kerugian finansial 1–3% dari revenue |
| **Level Risiko** | **6 Low to Moderate** | P(2) × I(2) = 6 |

**ZTA Maturity — Traditional**

*Pilar 1: Identity*
- Automation and Orchestration Capability
- Access Management

*Pilar 2: Applications and Workloads*
- Governance Capability

*Alasan:*
- Penonaktifan hak akses Non-SAP (email, VPN, internet) masih sepenuhnya manual.
- Kontrol hak akses SAP untuk karyawan mutasi tidak ada CC dan masih dikontrol manual.

---

### T.03 · Supply Chain Attacks
**PIC:** J | **Layer:** Application Layer | **Level Risiko:** 🟢 5 Low | **ZTA Maturity:** Initial

**Target Spesifik:**
- Sistem Manajemen Rantai Pasok
- Komponen Perangkat Lunak Vendor
- Komponen Perangkat Keras Avionik

**Serangan yang Terjadi:**
Penyusupan ke sistem komunikasi perusahaan melalui **pihak ketiga (middle-man)** menggunakan teknik manipulasi email (email phishing / domain spoofing). Penyerang menyamar sebagai vendor resmi untuk menipu pihak rantai pasok agar melakukan transfer dana ke rekening penyerang.

**Kronologi / Skenario Serangan:**
1. Terjadi korespondensi email panjang antara DetereCo dengan vendor melalui pihak ketiga (reseller/mediator) di Singapura.
2. Penyerang menyamar sebagai vendor menggunakan domain email yang mirip (mis. mengubah huruf 'l' menjadi 'i' atau 'o' menjadi angka '0').
3. Penyerang mengirimkan invoice dengan nomor rekening yang telah diganti milik penyerang.
4. Kurangnya ketelitian pihak yang di-CC dalam email; tidak ada yang menyadari invoice telah dimodifikasi.
5. Mediator (middleman) tidak teliti dan melakukan transfer dana ke rekening penyerang.
6. DetereCo tidak segera mendapat barang sesuai jadwal karena kendala pembayaran dan harus melalui proses penyelidikan kepolisian luar negeri.

**Kontrol Keamanan Eksisting:**
- *Non-Teknologi:* Program edukasi dan awareness verifikasi keaslian email serta penggunaan alat email verificator online.
- *Teknologi:* Sistem deteksi URL dan domain invalid/spoofing yang otomatis memberikan notifikasi dan memblokir domain berbahaya.
- *Verifikasi Perangkat Lunak:* Pemindaian setiap pembaruan perangkat lunak dari vendor resmi menggunakan point agent.

**Evidence:** Adanya pelaporan dan investigasi kepolisian Singapura terkait salah transfer dana < Rp 1 Miliar (puluhan ribu USD) yang dialami middle-man/reseller.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **1** | Insiden tergolong jarang (paling banyak 1× dalam setahun); kejadian terakhir sudah terjadi tahun lalu sebelum edukasi awareness masif |
| **Level Dampak** | **2** | Tidak ada kerugian finansial langsung dari perusahaan; gangguan pada sistem non-kritis; penurunan reputasi dan mistrust di rantai pasok |
| **Level Risiko** | **5 Low** | P(1) × I(2) = 5 |

**ZTA Maturity — Initial**

*General Guiding Criteria:*
Initial = starting automation of attribute assignment and configuration of lifecycles, policy decisions and enforcement, and initial cross-pillar solutions with integration of external systems.

*Pilar 1: Networks* — Visibility and Analytics Capability
*Pilar 2: Applications and Workloads* — Application Threat Protections
*Pilar 3: Cross-Cutting Capabilities* — Automation and Orchestration

*Yang Masih Traditional:*
- Pilar Devices: Asset & Supply Chain Risk Management
- Cross-Cutting Capabilities: Governance

*Alasan:*
Perusahaan telah menggunakan sistem Threat Intelligence eksternal untuk memverifikasi dan memblokir domain berbahaya secara otomatis, namun koordinasi lintas pilar secara menyeluruh masih dalam tahap pengembangan.

---

### T.04 · API & Integration Vulnerabilities
**PIC:** F | **Layer:** Application Layer | **Level Risiko:** 🟩 8 Low to Moderate | **ZTA Maturity:** Traditional

**Target Spesifik:**
- API Endpoints
- Layanan Integrasi Cloud
- Komunikasi Antar-Komponen
- Layanan SAP API Management
- Protokol Pertukaran Data Real-Time

**Serangan yang Terjadi:**
Eksploitasi pada titik integrasi antar sistem (Endpoint API) akibat kelemahan mekanisme autentikasi dan kerentanan keamanan, memungkinkan pihak tidak berwenang mengakses data internal.

**Kronologi / Skenario Serangan (Simulasi dari Temuan Pen Test):**
1. API perusahaan masih rentan karena autentikasi tradisional hanya mengandalkan basic auth statis (username/password) dan API key tunggal yang ditanam secara hardcode.
2. Ketika single key bocor atau terekspos ke pihak tidak berkepentingan (melalui WhatsApp, email, atau Notepad), ancaman ini dapat terjadi.
3. Penyerang yang memegang kredensial atau API key yang bocor memanfaatkannya untuk masuk ke endpoint API perusahaan.

**Kontrol Keamanan Eksisting:**
- Otorisasi lapis kedua pada URL Endpoint Turunan, sehingga mendapatkan URL utama saja tidak cukup untuk langsung mengeksploitasi.
- Akses remote menggunakan Full Tunnel VPN untuk isolasi akses data internal melalui IntraNet.
- Beberapa integrasi otomatis mengakses langsung ke database (DB) dengan jalur komunikasi terbatas, tidak menggunakan API terbuka.

**Evidence:** Temuan saat Penetration Testing: API Key berhasil terekspos. (Secara klasifikasi insiden, belum ada kebocoran nyata oleh peretas.)

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **3** | Kredensial masih single key → potensi bocor "bisa terjadi kapan saja" → probabilitas 40%–59% |
| **Level Dampak** | **2** | API saat ini baru mencakup integrasi data non-kritis dan terbatas (data pribadi/dashboard); data rahasia (IP, CAD, flight test) belum diintegrasikan |
| **Level Risiko** | **8 Low to Moderate** | P(3) × I(2) = 8 |

**ZTA Maturity — Traditional**

*Pilar 1: Applications and Workloads* — Application Access
*Pilar 2: Identity* — Authentication, Access Management
*Pilar 3: Networks* — Network Segmentation

*Alasan:*
- Bergantung pada otorisasi statis dan single key.
- Basic auth statis (username, password, API Key Hardcoded).
- Ketiadaan pembatasan IP yang dapat mengakses.
- Teknologi autentikasi berbasis session yang terotomatisasi secara dinamis (Bearer Token berbasis JSON/Cache) belum terimplementasi.

---

### T.05 · Lateral Movement
**PIC:** J | **Layer:** Network Layer | **Level Risiko:** 🟢 4 Low | **ZTA Maturity:** Initial

**Target Spesifik:**
- Jaringan Manufaktur (OT)
- Infrastruktur Cloud
- Server Aplikasi
- Data Center Storage

**Serangan yang Terjadi:**
Program berbahaya (BOT atau Crypto Mining) menyusup ke salah satu perangkat pengguna dan kemudian merambat antar sistem/komputer dalam satu jaringan segmen (VLAN) yang sama.

**Kronologi / Skenario Serangan:**
1. Pengguna mengunduh file dari sumber tidak resmi (situs/aplikasi bajakan).
2. File yang diunduh (mis. keygen aplikasi bajakan) mengandung bot tersembunyi.
3. Setelah menginfeksi perangkat awal, BOT bergerak dari satu PC ke PC lain dalam satu VLAN yang sama.
4. Perpindahan memanfaatkan fitur sharing resource (folder/printer) melalui protokol SMBv2 atau SMBv3.
5. BOT mengonsumsi bandwidth dan merusak reputasi IP publik perusahaan; akses internet terhambat karena dianggap lalu lintas mencurigakan.

**Kontrol Keamanan Eksisting:**
- *NDR (Network Detection and Response):* Mendeteksi aktivitas mencurigakan di lalu lintas jaringan menggunakan analitik perilaku; bekerja proaktif (otomatis memblokir) maupun reaktif (peringatan manual ke tim SOC).
- *Endpoint Protection:* Agen pada perangkat pengguna yang berkoordinasi dengan NDR.
- *Firewall:* Memblokir komunikasi lalu lintas berbahaya.
- *VLAN:* Segmentasi jaringan untuk membatasi penyebaran serangan.
- *Non-Teknologi:* Kebijakan pemilahan hak akses internet (pengelolaan dikembalikan kepada atasan setingkat manajer).

**Evidence:**
- Menurunnya scoring reputasi IP Publik perusahaan akibat aktivitas trafik bot.
- Banyak user internal terganggu akses internet karena dipaksa mengisi captcha terus-menerus.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **4** | Kejadian terjadi hampir setiap hari; perusahaan sering mengganti IP Publik |
| **Level Dampak** | **1** | Dampak minimal: NDR mampu mendeteksi, mengisolasi dan menahan pada level Alert (belum jadi Insiden); downtime hanya hitungan jam, pulih di hari yang sama |
| **Level Risiko** | **4 Low** | P(4) × I(1) = 4 |

**ZTA Maturity — Initial**

*Pilar 1: Networks* — Visibility and Analytics Capability
*Pilar 2: Cross-Cutting Capability* — Automation and Orchestration

*Yang Masih Traditional:*
- Pilar Networks: Network Segmentation
- Cross-Cutting Capabilities: Governance

*Alasan:*
- Perusahaan sudah mulai mengisolasi beban kerja menggunakan segmen/VLAN.
- Perusahaan sudah mulai menerapkan solusi lintas pilar melalui integrasi NDR, Endpoint Protection, dan Firewall untuk memblokir pergerakan tidak sah.

---

### T.06 · IoT/OT Vulnerabilities
**PIC:** F | **Layer:** Network Layer | **Level Risiko:** 🟢 1 Low | **ZTA Maturity:** Traditional

**Target Spesifik:**
- Mesin Produksi
- Sensor Telemetri
- Jalur Perakitan
- Sistem Kontrol Industri (ICS/SCADA)
- Ground Control Stations (Stasiun Kendali Darat)

**Serangan yang Terjadi:**
Serangan yang mengeksploitasi celah keamanan pada perangkat keras yang terhubung ke internet (Sensor Cerdas, mesin perakitan CNC, atau sistem kontrol produksi).

**Kronologi / Skenario Serangan (Proyeksi Masa Depan):**
Secara historis belum ada karena mesin perakitan pesawat masih silo (terpisah dari internet).

Skenario jika perusahaan mengadopsi IoT (Robotic Drilling System):
1. Meskipun jaringan direncanakan isolasi dengan bastion host, pihak IT terkadang harus membuka jalur akses ke internet publik secara insidental.
2. Saat jalur internet terbuka, penyerang memanfaatkan celah untuk menyerang dengan **DoS** ke arah mesin produksi.
3. Mesin robotik mengalami overload sehingga gagal menerima data operasional atau desain.

**Kontrol Keamanan Eksisting:**
- Firewall ganda berlapis: Firewall Internal (intranet) dan Firewall Eksternal (internet publik).
- Pelacakan traffic internet pada Vending Machine Sewa Tools menggunakan NDR.
- *RSTI ke depan:* Segmentasi Jaringan, Bastion Host, pembatasan akses IP, dan 2FA saat mesin pintar diimplementasikan.

**Evidence:** Belum ada.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **1** | Satu-satunya perangkat IoT saat ini hanya Vending Machine Sewa Tools; estimasi naik ke Level 2 jika ada perangkat IoT baru |
| **Level Dampak** | **1** | Jika Vending Machine diserang, operasional manufaktur pesawat tetap berjalan tanpa kendala; gangguan sangat minimal (sistem non-kritis); estimasi naik ke Level 3 jika ada RDS/Digital Harnessing |
| **Level Risiko** | **1 Low** | P(1) × I(1) = 1 |

**ZTA Maturity — Traditional**

*Pilar 1: Devices* — Policy Enforcement & Compliance Monitoring, Visibility and Analytics Capability
*Pilar 2: Cross-Cutting Capability* — Governance

*Alasan:*
Tidak ada penerapan perangkat IoT untuk Assembly Pesawat sehingga kematangan kontrol ZTA Devices: Policy Enforcement & Compliance Monitoring masih Tradisional.

---

### T.07 · Replay Attacks
**PIC:** J | **Layer:** Network Layer | **Level Risiko:** 🟩 8 Low to Moderate | **ZTA Maturity:** Traditional

**Target Spesifik:**
- Protokol Komunikasi
- Sistem Verifikasi Akses
- Session Tokens Login
- Link Telemetri & Telecommand (TM/TC) Satelit
- State Machine Kendali Pesawat/Satelit

**Serangan yang Terjadi:**
Secara historis menjadi isu insiden belum pernah ada (serangan ke Fingerprint, Kartu Akses, Rekaman suara, dan Face Recognition belum pernah terjadi).

**Kronologi / Skenario Serangan (Potensial):**

*Skenario 1 — Penyadapan Suara BOD:*
- Suara dari rapat direksi (BOD) disadap kemudian dimanipulasi menggunakan teknologi AI untuk meniru suara Direktur Utama guna memberikan instruksi ilegal.

*Skenario 2 — Akses Fisik Biometrik:*
- Pencurian data biometrik menggunakan selotip pada mesin fingerprint absensi.
- Penyalinan titik tap pada kartu akses (RFID card) yang direkam dalam waktu singkat untuk digunakan kembali oleh penyusup di lain waktu.

**Kontrol Keamanan Eksisting:**
- Teknologi: **Belum ada** kontrol keamanan.
- Non-Teknologi: **Belum ada** kontrol keamanan.

**Evidence:** Belum pernah ada catatan kejadian atau laporan historis terkait serangan ini.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **3** | Ketiadaan kontrol pengamanan sama sekali, sementara teknologi pendukung serangan (AI) sudah tersedia dan terus berkembang |
| **Level Dampak** | **2** | Level bervariasi: jika menyasar data center bisa L3–L4; jika pemalsuan kehadiran karyawan bisa L1. Level 2 dipilih sebagai nilai tengah |
| **Level Risiko** | **8 Low to Moderate** | P(3) × I(2) = 8 |

**ZTA Maturity — Traditional**

*Pilar 1: Identity* — Authentication
*Pilar 2: Networks* — Traffic Encryption
*Pilar 3: Cross-Cutting Capabilities* — Governance

*Alasan:*
Belum ada perlindungan, kontrol, maupun tata kelola keamanan terkait yang diadopsi sama sekali untuk ancaman ini.

---

### T.08 · Advanced Persistent Threats (APT)
**PIC:** F | **Layer:** Infrastructure Layer | **Level Risiko:** 🟢 4 Low | **ZTA Maturity:** Traditional

**Target Spesifik:**
- Data Desain Pesawat (CAD)
- Kekayaan Intelektual
- Jaringan Inti/Internal
- Data RnD

**Serangan yang Terjadi:**
Penanaman file berukuran sangat kecil (seperti keygen / .c seukuran script notepad) yang berupaya mengambil data secara perlahan.

**Kronologi / Skenario Serangan:**
1. Peretas berhasil memasukkan file sangat kecil (mis. file `.c` berisi ~3 baris kode hash, atau Keygen bajakan).
2. File APT dirancang spesifik untuk bersembunyi di sistem root (Linux) atau folder System32/Roaming (Windows).
3. Program kecil tersebut secara terus-menerus dan diam-diam mencoba mengumpulkan data/informasi endpoint.

**Kontrol Keamanan Eksisting:**
- *Teknologi:* NDR, Firewall, EPP (Endpoint Protection Platform), SIEM.
- *Non-Teknologi:* Usulan kebijakan Pembatasan Akses Internet (belum diterapkan). Mis. staff pemegang data rahasia dibatasi akses internet maksimal 1–2 jam per hari.

**Evidence:** Log deteksi ancaman APT yang muncul **setiap hari** pada sistem NDR.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **4** | Ancaman sering terjadi; setiap hari pasti ada yang terdeteksi di NDR → probabilitas 60%–79% |
| **Level Dampak** | **1** | Ekosistem kontrol mumpuni (NDR, Firewall, EPP) langsung mendeteksi dan memblokir APT secara real-time sebelum menyebabkan kerusakan |
| **Level Risiko** | **4 Low** | P(4) × I(1) = 4 |

**ZTA Maturity — Traditional**

*Pilar 1: Devices* — Device Threat Protection, Policy Enforcement & Compliance Monitoring
*Pilar 2: Cross-Cutting Capabilities* — Governance

*Alasan:*
- Tata kelola kebijakan masih wacana, belum diterapkan.
- Pemberian akses mengandalkan proses manual dan sering bebas diizinkan atasan tanpa awareness keamanan memadai.
- EPP baru diinstal pada ~300 dari 1.500 user.
- Titik buta: ratusan komputer tidak terlindungi akibat OS lama (Windows 7 & 8).

---

### T.09 · Ransomware & Malware Injection
**PIC:** J | **Layer:** Infrastructure Layer | **Level Risiko:** 🟡 13 Moderate | **ZTA Maturity:** Traditional

**Target Spesifik:**
- Sistem Produksi (OT)
- Server Keuangan
- Basis Data SDM
- Sistem Backup & Pemulihan
- Layanan MRO (Pemeliharaan Pesawat)

**Serangan yang Terjadi:**
Penguncian akses data atau enkripsi sistem kritis oleh **Ransomware jenis Petya** yang menargetkan komputer pengguna di luar jaringan pengamanan perusahaan, diikuti permintaan tebusan.

**Kronologi / Skenario Serangan:**
1. **Aktor & Target:** Pengguna berstatus stand-alone (di luar sistem perlindungan utama) menjadi titik masuk.
2. **Proses:** Karena perangkat tidak diproteksi Firewall, EPP, dan NDR perusahaan, ransomware (mirip Petya) menyusup dan langsung mengunci Data Desain Development (file CAD).
3. **Dampak Langsung:** Data desain pengembangan (file CAD) terenkripsi; pengguna tidak dapat mengakses maupun beraktivitas.
4. **Motif:** Penyerang meminta tebusan ~1–1,5 Bitcoin (BTC) agar data bisa dibuka kembali.
5. **Pemulihan:** Perusahaan tidak membayar tebusan; proses restore dari backup membutuhkan waktu **±7 hari kerja**.

**Kontrol Keamanan Eksisting:**
- Integrasi jaringan: menarik komputer stand-alone ke jaringan yang dilindungi NDR, Firewall, dan Endpoint Protection, serta memindahkan datanya ke server dalam data center.
- Pemasangan Endpoint Protection dengan fitur pendeteksi dan manajer ransomware khusus.
- Data recovery dilakukan dengan restore dari sistem backup.
- *Mitigasi Kedepan:* (a) scanning malware manual rutin tiap bulan pada server kritis; (b) install EPP bertahap → saat ini ~300 dari 1.300–1.500 komputer.

**Evidence:** Tidak ada.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **3** | Insiden terakhir terjadi akhir 2025; ancaman diprediksi dapat terjadi kapan saja (Probabilitas 40%–59%) karena penyerang terus memperbarui metode |
| **Level Dampak** | **3** | Kerugian finansial tidak dapat dihitung pasti; pemulihan 7 hari kerja; potensi hilangnya sebagian data internal rahasia yang memengaruhi kinerja operasional |
| **Level Risiko** | **13 Moderate** | P(3) × I(3) = 13 |

**ZTA Maturity — Traditional**

*Pilar 1: Devices* — Device Threat Protection, Visibility and Analytics Capability
*Pilar 2: Data* — Visibility and Analytics Capability, Data Availability, Automation and Orchestration Capability

*Alasan:*
- Visibilitas terbatas: user baru sadar ketika melaporkan data kritis terkunci.
- Cakupan proteksi terfragmentasi (~300 dari 1.500 user).
- Pemindaian malware dan ransomware masih manual berdasarkan jadwal.
- Strategi pemulihan manual yang memakan waktu 7 hari kerja.

---

### T.10 · Industrial Espionage (Spionase Industri)
**PIC:** F | **Layer:** Data Layer | **Level Risiko:** 🟡 15 Moderate | **ZTA Maturity:** Traditional

**Target Spesifik:**
- Data Litbang (RnD)
- CAD/CAM Files
- Spesifikasi Teknis Pesawat
- Protokol Komunikasi Militer
- Sistem ERP
- Data Vendor
- Data Penawaran Kontrak

**Serangan yang Terjadi:**
Upaya pencurian rahasia dagang, spesifikasi teknis, cetak biru (CAD), hingga formula produk kedirgantaraan secara ilegal untuk kepentingan kompetitor.

**Kronologi / Skenario Serangan (Proyeksi — Belum Pernah Terjadi):**
1. Aktor spionase mencoba mengambil data dengan mencolokkan flashdisk ilegal ke perangkat (laptop/komputer) perusahaan yang menyimpan file rancangan pesawat.
2. Penyerang memindahkan atau mengekstrak file berskala besar (CAD/CAM atau database) melalui flashdisk.
3. Atau mencoba mengunggahnya ke layanan penyimpanan cloud pribadi (Google Drive) dan mengirimkannya melalui email ke pihak eksternal.

**Kontrol Keamanan Eksisting:**
- *Teknologi:* EDR, NDR, Firewall, dan Mail Gateway. Endpoint Protection sebagai file filter: jika ada upaya transfer file `.CAD` atau `.db` ke Google Drive, jaringan luar, atau email pribadi → langsung dicegat dan diblokir secara otomatis (real-time).
- *Non-Teknologi:* Proses otorisasi panjang untuk karyawan yang hendak memindahkan data penting. Namun, otorisasi ini masih murni manual menggunakan formulir fisik.
- *Rencana Pengadaan:* NAC (2026), DLP (2027), DRM (2027).

**Evidence:** Belum ada.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **1** | Narasumber menyatakan ancaman ini Sangat Jarang Terjadi (Level 1) |
| **Level Dampak** | **4** | Konsekuensi insiden mengakibatkan "hilangnya sebagian data kritikal bersifat rahasia" yang sangat vital (Data Desain Militer) |
| **Level Risiko** | **15 Moderate** | P(1) × I(4) = 15 |

**ZTA Maturity — Traditional**

*Pilar 1: Devices* — Data Access, Automation and Orchestration Capability, Data Inventory Management
*Pilar 2: Devices* — Device Threat Protection
*Pilar 3: Network* — Governance Capability

*Alasan:*
Meskipun NDR, Endpoint Protection, dan Mail Gateway sudah bekerja real-time memblokir upaya ekstraksi data, secara komprehensif masih Traditional karena:
- Proses otorisasi akses data rahasia masih statis dan manual (formulir kertas fisik).
- NAC belum diterapkan (rencana pengadaan tahun ini).
- DLP dan DRM belum diterapkan (rencana pengadaan tahun depan).
- Titik buta skala enterprise: EPP baru terpasang pada 30% user.

---

### T.11 · Disaster / Bencana
**PIC:** J & F | **Layer:** Infrastructure Layer | **Level Risiko:** 🟡 15 Moderate | **ZTA Maturity:** Traditional

**Target Spesifik:** Seluruh Bangunan / Aset Kritis

**Serangan yang Terjadi:**
Bencana skala besar dan masif seperti Bencana Alam, Kesalahan Manusia, Perang, hingga Gangguan teknis seperti mati listrik sekawasan.

**Kronologi / Skenario Serangan (Proyeksi — Belum Pernah Terjadi):**
- Skenario terburuk: bencana melanda seluruh kawasan perusahaan.
- Backup PTDI masih berada di satu wilayah yang sama, hanya berbeda gedung (pusat data utama dan Gedung GPM 9 lantai sebagai Alternate Data Center).
- Bencana menyebabkan seluruh layanan pusat seperti ERP mati total.
- Seluruh operasional TI perusahaan lumpuh karena tidak ada Disaster Recovery Center (DRC) di luar kota/provinsi.

**Kontrol Keamanan Eksisting:**
- Backup data di gedung berbeda (GPM) dalam satu kawasan.
- Prosedur pemulihan yang bersifat manual, sebagian mulai diotomasi pada sisi server.
- Sedang dalam proses pengadaan DRC di lokasi geografis berbeda (beda kota/provinsi) untuk mencegah Single Point of Failure.

**Evidence:** Gedung GPM masih di satu wilayah dengan Gedung IT.

| Penilaian | Nilai | Alasan |
|---|:---:|---|
| **Level Kemungkinan** | **1** | Narasumber menyatakan kemungkinannya sangat kecil; kondisi politik Indonesia dengan negara lain stabil |
| **Level Dampak** | **4** | Meskipun mesin produksi bisa berjalan mandiri (siloed) tanpa IT, operasional sistemik akan terhenti; pemulihan 8–15 hari kerja; kelumpuhan sistem IT krusial (ERP) |
| **Level Risiko** | **15 Moderate** | P(1) × I(4) = 15 |

**ZTA Maturity — Traditional**

*Pilar 1: Data* — Data Availability, Automation and Orchestration Capability
*Pilar 2: Cross-Cutting Capabilities* — Governance

*Alasan:*
- Perusahaan masih menyimpan backup operasional TI di dalam satu kawasan fisik yang sama (Gedung GPM).
- Mitigasi ketahanan site berlapis (DRC di luar kota/provinsi) baru pada tahap perencanaan dan belum berjalan seutuhnya.
- Kontrol saat ini masih sangat bergantung pada proses manual dan kebijakan statis.

---

## Distribusi Analisis

### Distribusi Level Risiko

| Level Risiko | Jumlah | Ancaman |
|---|:---:|---|
| 🟡 Moderate (12–15) | 3 | T.09, T.10, T.11 |
| 🟩 Low to Moderate (6–11) | 3 | T.02, T.04, T.07 |
| 🟢 Low (1–5) | 5 | T.01, T.03, T.05, T.06, T.08 |

### Distribusi ZTA Maturity Level

| Maturity Level | Jumlah | Ancaman |
|---|:---:|---|
| Traditional | 9 | T.01, T.02, T.04, T.06, T.07, T.08, T.09, T.10, T.11 |
| Initial | 2 | T.03, T.05 |

### Distribusi per Klasifikasi Layer

| Layer | Ancaman |
|---|---|
| Identity Layer | T.01 (Compromised Credentials), T.02 (Insider Threats) |
| Application Layer | T.03 (Supply Chain Attacks), T.04 (API & Integration Vulnerabilities) |
| Network Layer | T.05 (Lateral Movement), T.06 (IoT/OT Vulnerabilities), T.07 (Replay Attacks) |
| Infrastructure Layer | T.08 (APT), T.09 (Ransomware & Malware Injection), T.11 (Disaster) |
| Data Layer | T.10 (Industrial Espionage) |

---

*Sumber: ISO 27005:2022 · ZTA ZTMM by CISA · Prosedur Internal PT DI (Pelaksanaan Manajemen Risiko TI)*
