const fs = require('fs');
const file = 'c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html';
let content = fs.readFileSync(file, 'utf8');

const englishTranslations = `
    translations.en.t10_title = "Industrial Espionage";
    translations.en.t10_mode = "Highly Relevant";
    translations.en.t10_notes = "Cisometric Consulting Manager: <br> add 8.1 User endpoint devices (Provides clear guidelines on the physical and logical security of devices used by employees to access company data, minimizing the risk of data theft via compromised endpoints.)";
    translations.en.t10_fgd = "According to Cisometric's Consulting Manager, the addition of Control 8.1 \\"Provides clear guidelines on the physical and logical security of devices used by employees.\\" The forum agreed to add Control 8.1 to strengthen endpoint security.";

    translations.en.t11_title = "Disaster";
    translations.en.t11_mode = "Highly Relevant";
    translations.en.t11_notes = "(Agreed, no additional controls needed as existing ones are sufficient)";
    translations.en.t11_fgd = "The forum agreed that the existing controls (8.14 Redundancy, 5.30 ICT readiness, 5.29 Information security during disruption) are adequate to mitigate disaster risks.";

    translations.en.t09_title = "Ransomware & Malware Injection";
    translations.en.t09_mode = "Highly Relevant";
    translations.en.t09_notes = "Cisometric Consulting Manager: <br> add 8.15 Logging (Vital for investigating ransomware incidents, allowing the tracking of entry points and propagation paths.)";
    translations.en.t09_fgd = "The forum agreed to add Control 8.15 because event logging is crucial for post-incident forensics and identifying ransomware entry points.";

    translations.en.t04_title = "API & Integration Vulnerabilities";
    translations.en.t04_mode = "Relevant";
    translations.en.t04_notes = "Cisometric Consulting Manager: <br> add 8.27 Secure System Architecture (Mandates secure by design principles for API integration) <br> add 5.12 Classification of Information (Ensures sensitive data via API is appropriately protected)";
    translations.en.t04_fgd = "The addition of Controls 8.27 and 5.12 was agreed upon to ensure secure API architecture and proper data classification.";

    translations.en.t07_title = "Replay Attacks";
    translations.en.t07_mode = "Highly Relevant";
    translations.en.t07_notes = "(Agreed, no additional controls needed as existing ones are sufficient)";
    translations.en.t07_fgd = "The forum agreed that the existing controls (8.5 Secure authentication, 8.24 Use of cryptography) are adequate against replay attacks.";

    translations.en.t02_title = "Insider Threats";
    translations.en.t02_mode = "Relevant";
    translations.en.t02_notes = "Head of IT Sec: <br> reject 6.4 Disciplinary Process (Already handled by HR)<br> reject 6.3 Security Awareness (Too broad)<br> add 6.2 Terms (Legal binding)<br> add 5.32 IP Rights (Legal protection)<br> add 7.2 Physical Entry (Restrict access)";
    translations.en.t02_fgd = "The forum agreed to reject Controls 6.4 and 6.3 as they overlap with HR and are too broad. Controls 6.2, 5.32, and 7.2 were added to provide legal binding and physical restrictions.";

    translations.en.t03_title = "Supply Chain Attacks";
    translations.en.t03_mode = "Relevant";
    translations.en.t03_notes = "External Auditor: <br> reject 5.21 ICT supply chain (Not applicable to current vendor scope)<br> reject 8.3 Access restriction (Redundant)<br> add 5.20 Supplier agreements (Crucial for vendor liability)<br> add 6.7 Remote Working (Relevant for third-party remote access)";
    translations.en.t03_fgd = "The forum rejected Controls 5.21 and 8.3 due to scope and redundancy. Controls 5.20 and 6.7 were added to enforce supplier liability and secure remote access.";

    translations.en.t05_title = "Lateral Movement";
    translations.en.t05_mode = "Highly Relevant";
    translations.en.t05_notes = "Cisometric Consulting Manager: <br> add 8.16 Monitoring activities (Essential to detect anomalous internal traffic)<br> add 8.7 Protection against malware (To stop lateral spread)";
    translations.en.t05_fgd = "Controls 8.16 and 8.7 were added to detect anomalous internal network traffic and prevent the spread of malware across network segments.";

    translations.en.t08_title = "Advanced Persistent Threats (APT)";
    translations.en.t08_mode = "Highly Relevant";
    translations.en.t08_notes = "Cisometric Consulting Manager: <br> add 5.7 Threat intelligence (Threat intelligence helps organizations understand the characteristics, methods, and indicators used by APTs so that these threats can be proactively detected and mitigated.)";
    translations.en.t08_fgd = "According to Cisometric's Consulting Manager, the addition of Control 5.7 \\"helps organizations understand the characteristics, methods, and indicators used by APTs.\\" The forum agreed.";

    translations.en.t01_title = "Compromised Credentials";
    translations.en.t01_mode = "Highly Relevant";
    translations.en.t01_notes = "(Agreed, no additional controls needed as existing ones are sufficient)";
    translations.en.t01_fgd = "The forum agreed that the existing controls from COBIT 2019 (APO12.02 and APO12.06) are sufficient.";

    translations.en.t06_title = "IoT/OT Vulnerabilities";
    translations.en.t06_mode = "Relevant";
    translations.en.t06_notes = "Head of IT Sec: <br> add 5.14 Data Transfer (Secure data flows)<br> add 5.15 Access Control (Restrict IoT access)<br> add 8.22 Segregation (Isolate IoT networks)";
    translations.en.t06_fgd = "The forum agreed to add Controls 5.14, 5.15, and 8.22 to secure IoT data transfers, restrict access, and isolate vulnerable networks.";
    
    translations.en.widget_title = "Expert Notes & Focus Group Discussion (FGD) Results";
    translations.en.widget_filter_all = "All";
    translations.en.widget_filter_changes = "Changes";
    translations.en.widget_filter_nochanges = "No Changes";
    translations.en.widget_filter_high = "Highly Relevant";
    translations.en.widget_filter_relevant = "Relevant";
    translations.en.widget_pre_controls = "PRE-CONTROLS";
    translations.en.widget_post_controls = "POST-CONTROLS";
    translations.en.widget_no_changes_req = "No changes requested by experts";
`;

const indonesianTranslations = `
    translations.id.t10_title = "Spionase Industri";
    translations.id.t10_mode = "Sangat Relevan";
    translations.id.t10_notes = "Cisometric Consulting Manager: <br> tambahkan 8.1 User endpoint devices (Memberikan pedoman yang jelas tentang keamanan fisik dan logis perangkat yang digunakan oleh karyawan untuk mengakses data perusahaan, meminimalkan risiko pencurian data melalui titik akhir yang disusupi.)";
    translations.id.t10_fgd = "Menurut Manajer Konsultasi Cisometric, penambahan Kontrol 8.1 \\"Memberikan panduan yang jelas tentang keamanan fisik dan logis perangkat yang digunakan oleh karyawan.\\" Forum sepakat untuk menambahkan Kontrol 8.1 untuk memperkuat keamanan titik akhir.";

    translations.id.t11_title = "Bencana";
    translations.id.t11_mode = "Sangat Relevan";
    translations.id.t11_notes = "(Disepakati, tidak perlu kontrol tambahan karena yang sudah ada sudah memadai)";
    translations.id.t11_fgd = "Forum sepakat bahwa kontrol yang ada (8.14 Redundansi, 5.30 Kesiapan TIK, 5.29 Keamanan informasi selama gangguan) memadai untuk memitigasi risiko bencana.";

    translations.id.t09_title = "Injeksi Ransomware & Malware";
    translations.id.t09_mode = "Sangat Relevan";
    translations.id.t09_notes = "Cisometric Consulting Manager: <br> tambahkan 8.15 Logging (Sangat penting untuk menyelidiki insiden ransomware, memungkinkan pelacakan titik masuk dan jalur propagasi.)";
    translations.id.t09_fgd = "Forum sepakat untuk menambahkan Kontrol 8.15 karena pencatatan peristiwa sangat penting untuk forensik pasca-insiden dan mengidentifikasi titik masuk ransomware.";

    translations.id.t04_title = "Kerentanan API & Integrasi";
    translations.id.t04_mode = "Relevan";
    translations.id.t04_notes = "Cisometric Consulting Manager: <br> tambahkan 8.27 Secure System Architecture (Mewajibkan prinsip desain yang aman untuk integrasi API) <br> tambahkan 5.12 Classification of Information (Memastikan data sensitif melalui API dilindungi secara tepat)";
    translations.id.t04_fgd = "Penambahan Kontrol 8.27 dan 5.12 disepakati untuk memastikan arsitektur API yang aman dan klasifikasi data yang tepat.";

    translations.id.t07_title = "Serangan Replay";
    translations.id.t07_mode = "Sangat Relevan";
    translations.id.t07_notes = "(Disepakati, tidak perlu kontrol tambahan karena yang sudah ada sudah memadai)";
    translations.id.t07_fgd = "Forum sepakat bahwa kontrol yang ada (8.5 Otentikasi aman, 8.24 Penggunaan kriptografi) memadai terhadap serangan replay.";

    translations.id.t02_title = "Ancaman Orang Dalam";
    translations.id.t02_mode = "Relevan";
    translations.id.t02_notes = "Head of IT Sec: <br> tolak 6.4 Disciplinary Process (Sudah ditangani oleh SDM)<br> tolak 6.3 Security Awareness (Terlalu luas)<br> tambahkan 6.2 Terms (Mengikat secara hukum)<br> tambahkan 5.32 IP Rights (Perlindungan hukum)<br> tambahkan 7.2 Physical Entry (Batasi akses)";
    translations.id.t02_fgd = "Forum sepakat untuk menolak Kontrol 6.4 dan 6.3 karena tumpang tindih dengan SDM dan terlalu luas. Kontrol 6.2, 5.32, dan 7.2 ditambahkan untuk memberikan ikatan hukum dan batasan fisik.";

    translations.id.t03_title = "Serangan Rantai Pasokan";
    translations.id.t03_mode = "Relevan";
    translations.id.t03_notes = "External Auditor: <br> tolak 5.21 ICT supply chain (Tidak berlaku untuk cakupan vendor saat ini)<br> tolak 8.3 Access restriction (Redundan)<br> tambahkan 5.20 Supplier agreements (Penting untuk kewajiban vendor)<br> tambahkan 6.7 Remote Working (Relevan untuk akses jarak jauh pihak ketiga)";
    translations.id.t03_fgd = "Forum menolak Kontrol 5.21 dan 8.3 karena cakupan dan redundansi. Kontrol 5.20 dan 6.7 ditambahkan untuk menegakkan kewajiban pemasok dan mengamankan akses jarak jauh.";

    translations.id.t05_title = "Pergerakan Lateral";
    translations.id.t05_mode = "Sangat Relevan";
    translations.id.t05_notes = "Cisometric Consulting Manager: <br> tambahkan 8.16 Monitoring activities (Penting untuk mendeteksi lalu lintas internal yang tidak normal)<br> tambahkan 8.7 Protection against malware (Untuk menghentikan penyebaran lateral)";
    translations.id.t05_fgd = "Kontrol 8.16 dan 8.7 ditambahkan untuk mendeteksi lalu lintas jaringan internal yang anomali dan mencegah penyebaran malware di seluruh segmen jaringan.";

    translations.id.t08_title = "Ancaman Persisten Tingkat Lanjut (APT)";
    translations.id.t08_mode = "Sangat Relevan";
    translations.id.t08_notes = "Cisometric Consulting Manager: <br> tambahkan 5.7 Threat intelligence (Intelijen ancaman membantu organisasi memahami karakteristik, metode, dan indikator yang digunakan oleh APT sehingga ancaman ini dapat dideteksi dan dimitigasi secara proaktif.)";
    translations.id.t08_fgd = "Menurut Manajer Konsultasi Cisometric, penambahan Kontrol 5.7 \\"membantu organisasi memahami karakteristik, metode, dan indikator yang digunakan oleh APT.\\" Forum setuju.";

    translations.id.t01_title = "Kredensial Terkompromi";
    translations.id.t01_mode = "Sangat Relevan";
    translations.id.t01_notes = "(Disepakati, tidak perlu kontrol tambahan karena yang sudah ada sudah memadai)";
    translations.id.t01_fgd = "Forum sepakat bahwa kontrol yang ada dari COBIT 2019 (APO12.02 dan APO12.06) memadai.";

    translations.id.t06_title = "Kerentanan IoT/OT";
    translations.id.t06_mode = "Relevan";
    translations.id.t06_notes = "Head of IT Sec: <br> tambahkan 5.14 Data Transfer (Aliran data yang aman)<br> tambahkan 5.15 Access Control (Batasi akses IoT)<br> tambahkan 8.22 Segregation (Isolasi jaringan IoT)";
    translations.id.t06_fgd = "Forum sepakat untuk menambahkan Kontrol 5.14, 5.15, dan 8.22 untuk mengamankan transfer data IoT, membatasi akses, dan mengisolasi jaringan yang rentan.";

    translations.id.widget_title = "Catatan Ahli & Hasil Focus Group Discussion (FGD)";
    translations.id.widget_filter_all = "Semua";
    translations.id.widget_filter_changes = "Perubahan";
    translations.id.widget_filter_nochanges = "Tanpa Perubahan";
    translations.id.widget_filter_high = "Sangat Relevan";
    translations.id.widget_filter_relevant = "Relevan";
    translations.id.widget_pre_controls = "PRA-KONTROL";
    translations.id.widget_post_controls = "PASCA-KONTROL";
    translations.id.widget_no_changes_req = "Tidak ada perubahan yang diminta oleh ahli";
`;

// Inject right after the last translations.ja.menu_... definition
const injectionPoint = '    if (translations.ja) translations.ja.menu_research = "研究概要";';

if (content.includes(injectionPoint)) {
    content = content.replace(injectionPoint, injectionPoint + "\\n" + englishTranslations + "\\n" + indonesianTranslations);
    fs.writeFileSync(file, content, 'utf8');
    console.log("Translations appended!");
} else {
    console.log("Could not find injection point.");
}
