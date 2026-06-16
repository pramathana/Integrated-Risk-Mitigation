# Daftar Risiko Prioritas
**Sumber:** IT Risk Assessment — Model Mitigasi Risiko Terintegrasi
**Standar:** ISO 27005:2022 & Prosedur Internal PT DI

---

## Skala Level Risiko

| Rentang Nilai (P × I) | Tingkat Risiko | Tindakan |
|---|---|---|
| 1 – 5 | 🟢 Low | Risiko dapat diterima. Pemantauan rutin. |
| 6 – 11 | 🟩 Low to Moderate | Tinjauan berkala & rencana penambahan kontrol. |
| 12 – 15 | 🟡 Moderate | Tinjauan berkala & kontrol preventif setiap 3–6 bulan. |
| 16 – 19 | 🟠 Moderate to High | Mitigasi ZTA komprehensif dalam 1–3 bulan. |
| 20 – 25 | 🔴 High | Penanganan darurat, mitigasi & penyekatan jaringan < 1 bulan. |

---

## Tabel Prioritas Risiko

| Prioritas | ID | Jenis Ancaman | Klasifikasi Layer | Level Risiko |
|:---:|:---:|---|---|:---:|
| 1 | T.10 | Industrial Espionage (Spionase Industri) | Data Layer | 🟡 **15 Moderate** |
| 2 | T.11 | Disaster / Bencana | Infrastructure Layer | 🟡 **15 Moderate** |
| 3 | T.09 | Ransomware & Malware Injection | Infrastructure Layer | 🟡 **13 Moderate** |
| 4 | T.04 | API & Integration Vulnerabilities | Application Layer | 🟩 **8 Low to Moderate** |
| 5 | T.07 | Replay Attacks | Network Layer | 🟩 **8 Low to Moderate** |
| 6 | T.02 | Insider Threats | Identity Layer | 🟩 **6 Low to Moderate** |
| 7 | T.03 | Supply Chain Attacks | Application Layer | 🟢 **5 Low** |
| 8 | T.05 | Lateral Movement | Network Layer | 🟢 **4 Low** |
| 9 | T.08 | Advanced Persistent Threats (APT) | Infrastructure Layer | 🟢 **4 Low** |
| 10 | T.01 | Compromised Credentials | Identity Layer | 🟢 **3 Low** |
| 11 | T.06 | IoT/OT Vulnerabilities | Network Layer | 🟢 **1 Low** |

---

## Ringkasan per Level Risiko

### 🟡 Moderate (12–15) — Perlu Diwaspadai

**T.10 · Industrial Espionage** `Data Layer`
Upaya pencurian rahasia dagang, spesifikasi teknis, cetak biru (CAD/CAM), hingga formula produk kedirgantaraan secara ilegal oleh kompetitor.

**T.11 · Disaster / Bencana** `Infrastructure Layer`
Bencana skala besar (alam, perang, mati listrik kawasan) yang dapat melumpuhkan seluruh sistem IT termasuk ERP, dengan backup masih berada dalam satu kawasan geografis.

**T.09 · Ransomware & Malware Injection** `Infrastructure Layer`
Penguncian data kritis (seperti file CAD) oleh ransomware jenis Petya yang menyasar perangkat stand-alone di luar jaringan pengamanan perusahaan.

---

### 🟩 Low to Moderate (6–11) — Perlu Kewaspadaan

**T.04 · API & Integration Vulnerabilities** `Application Layer`
Eksploitasi endpoint API akibat penggunaan kunci statis (hardcoded) yang rentan bocor melalui WhatsApp, email, atau notepad.

**T.07 · Replay Attacks** `Network Layer`
Eksploitasi ulang data autentikasi statis (biometrik, RFID) dengan teknologi AI untuk meniru suara/akses pejabat perusahaan. Belum ada kontrol keamanan sama sekali.

**T.02 · Insider Threats** `Identity Layer`
Pembocoran informasi dan penyalahgunaan hak akses SAP oleh pegawai internal, terutama kasus mutasi tanpa pencabutan hak akses tepat waktu.

---

### 🟢 Low (1–5) — Dapat Diterima, Pemantauan Rutin

**T.03 · Supply Chain Attacks** `Application Layer`
Manipulasi invoice oleh penyerang yang menyamar sebagai vendor melalui domain email spoofing (Business Email Compromise).

**T.05 · Lateral Movement** `Network Layer`
Program berbahaya (BOT/Crypto Mining) yang menyusup melalui unduhan tidak resmi dan menyebar antar perangkat dalam satu VLAN.

**T.08 · Advanced Persistent Threats (APT)** `Infrastructure Layer`
Penanaman file kecil (keygen/.c) yang bersembunyi di sistem root untuk mencuri data endpoint secara diam-diam. Terdeteksi setiap hari di NDR.

**T.01 · Compromised Credentials** `Identity Layer`
Pencurian username dan password melalui email phishing yang mengarahkan pengguna ke portal palsu. Terjadi di hampir semua divisi.

**T.06 · IoT/OT Vulnerabilities** `Network Layer`
Eksploitasi celah keamanan perangkat IoT (saat ini hanya vending machine). Risiko akan meningkat seiring rencana adopsi Robotic Drilling System.

---

## Distribusi Risiko per Layer

| Layer | Jumlah Ancaman | ID |
|---|:---:|---|
| Infrastructure Layer | 3 | T.09, T.08, T.11 |
| Network Layer | 3 | T.05, T.06, T.07 |
| Identity Layer | 2 | T.01, T.02 |
| Application Layer | 2 | T.03, T.04 |
| Data Layer | 1 | T.10 |

---

*Sumber: ISO 27005:2022 & Prosedur Internal PT DI (Pelaksanaan Manajemen Risiko TI)*
