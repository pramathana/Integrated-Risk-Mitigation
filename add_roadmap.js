const fs = require('fs');

let content = fs.readFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', 'utf8');

const id_eval = `        "id": \`# Peta Jalan Validasi 3 Tahap
## Metodologi Evaluasi

Fase Evaluasi dilakukan melalui serangkaian aktivitas terstruktur yang melibatkan evaluasi dari Pakar (Internal dan Eksternal) dengan tahapan detail sebagai berikut:

**1. Penilaian Pakar (Skala Likert)**
: Langkah pertama adalah menyajikan artefak konseptual kepada para pakar. Para pakar diminta untuk memberikan penilaian kuantitatif deskriptif terkait relevansi model menggunakan kuesioner Skala Likert dengan rentang 4 poin untuk menghindari bias ambivalensi nilai tengah. Skala yang digunakan terdiri dari:
- **(1)** Sangat Tidak Relevan
- **(2)** Tidak Relevan
- **(3)** Relevan
- **(4)** Sangat Relevan

**2. Focus Group Discussion (FGD)**
: Hasil penilaian kuantitatif deskriptif yang dianggap sangat tidak relevan dan tidak relevan oleh pakar kemudian didiskusikan lebih mendalam melalui diskusi terarah. Diskusi ini bertujuan untuk menggali alasan yang mendasari penilaian tersebut, seperti *"mengapa komponen tersebut dianggap tidak relevan?"* atau *"Di mana letak kekurangan model tersebut?"*, guna memperoleh umpan balik kualitatif naratif yang konkret.

**3. Validasi Partisipan**
: Tahap validasi akhir adalah meninjau artefak yang telah direvisi. Aktivitas ini melibatkan pakar yang sama untuk meninjau perbaikan dan mencapai kesepakatan akhir bahwa artefak yang direvisi relevan digunakan sebagai pedoman manajemen risiko keamanan siber di lingkungan DetereCo. Setelah kesepakatan tercapai, penelitian dilanjutkan dengan menarik Kesimpulan dan Rekomendasi.

---

## Hasil Kuesioner Penilaian Pakar

| Jenis Ancaman | Skala 1 | Skala 2 | Skala 3 | Skala 4 | Modus Skala | Interpretasi |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T.10 Industrial Espionage | 0 | 0 | 3 | 6 | **4** | ? Sangat Relevan |
| T.11 Disaster | 0 | 0 | 4 | 5 | **4** | ? Sangat Relevan |
| T.09 Ransomware & Malware Injection | 0 | 0 | 4 | 5 | **4** | ? Sangat Relevan |
| T.04 API & Integration Vulnerabilities | 0 | 0 | 5 | 4 | **3** | ? Relevan |
| T.07 Replay Attacks | 0 | 0 | 2 | 7 | **4** | ? Sangat Relevan |
| T.02 Insider Threats | 0 | 1 | 6 | 2 | **3** | ? Relevan |
| T.03 Supply Chain Attacks | 0 | 0 | 5 | 4 | **3** | ? Relevan |
| T.05 Lateral Movement | 0 | 0 | 1 | 8 | **4** | ? Sangat Relevan |
| T.08 Advanced Persistent Threats (APT) | 0 | 0 | 4 | 5 | **4** | ? Sangat Relevan |
| T.01 Compromised Credentials | 0 | 0 | 4 | 5 | **4** | ? Sangat Relevan |
| T.06 IoT/OT Vulnerabilities | 0 | 0 | 5 | 4 | **3** | ? Relevan |
\`,`

const targetStr = "| T.06 IoT/OT Vulnerabilities | 0 | 0 | 5 | 4 | **3** | ? Relevant |\n`";

if (content.includes(targetStr)) {
    content = content.replace(targetStr, targetStr + ",\n" + id_eval);
    fs.writeFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', content, 'utf8');
    console.log("Success");
} else {
    console.log("Could not find target string.");
}
