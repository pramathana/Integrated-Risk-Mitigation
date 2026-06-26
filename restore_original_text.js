const fs = require('fs');

function cleanText(text) {
    if (!text) return text;
    return text.replace(/\+'/g, '->')
               .replace(/\?o/g, '"')
               .replace(/\?\?/g, '"')
               .replace(/\?T/g, "'")
               .replace(/A/g, '|')
               .replace(/"/g, '\\"')
               .replace(/\n/g, '<br>');
}

// Write the clean english translations based on the raw text from the transcript
const englishTranslations = `
    translations.en.t10_notes = "Cisometric Consulting Manager -> add 8.1 User endpoint devices (prevent access to or theft of information from employee laptops or lab workstations)";
    translations.en.t10_fgd = "The forum agreed to add 8.1 because industrial espionage often occurs through physical endpoints";
    
    translations.en.t11_notes = "No additional notes from experts";
    translations.en.t11_fgd = "No changes";
    
    translations.en.t09_notes = "IT Security Supervisor -> add 8.15 Logging (logs to support 8.16 Monitoring Activity)";
    translations.en.t09_fgd = "The forum agreed because logging provides a trail for early detection and root cause analysis after an incident";
    
    translations.en.t04_notes = "Cisometric + Planning Manager -> add 8.27 Secure Architecture (pen tests show exposed API keys; \\"secure by design\\" is not yet optimal) + 5.12 Classification (categorize data that may or may not be exposed via API)";
    translations.en.t04_fgd = "The forum agreed that 8.27 aligns with Tenet 3 per session; 5.12 should ensure the API automatically blocks \\"Confidential\\" data";
    
    translations.en.t07_notes = "No additional notes";
    translations.en.t07_fgd = "No changes";
    
    translations.en.t02_notes = "5 experts from Citilink, Cisometric, Telkom University, IT Supervisor, IT Manager -> add 6.2 Terms of Employment + 5.32 IP Rights + 7.2 Physical Entry | rejected: 6.4 Disciplinary Process | 6.3 Security Awareness";
    translations.en.t02_fgd = "GMO retained. 6.2 legal basis for employees; 5.32 prevent replication of former employees' IP; 7.2 automation of ID card deactivation upon transfer. 6.4 rejected because SPT already exists; 6.3 rejected because we will focus on T.01 first";
    
    translations.en.t03_notes = "Sr. GRC Consultant + 3 other experts -> add 5.20 Supplier agreements (VSAR/vendor due diligence) + 6.7 Remote Working (BYOD for sales roles) | Rejected: 5.21 ICT supply chain | 8.3 Access restriction";
    translations.en.t03_fgd = "5.20 for VSAR validation of vendor ISMS; 6.7 for security of sales employees' BYOD devices. 5.21 is irrelevant to resolving the issue; 8.3 is irrelevant because the issue involves external spoofing, not an internal breach";
    
    translations.en.t05_notes = "Cisometric + IT Supervisor -> add 8.16 Monitoring (detection of abnormal access patterns) + 8.7 Anti-malware (address the primary cause of lateral movement)";
    translations.en.t05_fgd = "8.16 for detecting anomalous internal traffic; 8.7 because endpoint anti-malware eliminates the capability for proximal infection (worm propagation)";
    
    translations.en.t08_notes = "Cisometric Consulting Manager -> add 5.7 Threat intelligence (provides the latest IoC and TTP indicators to security tools to recognize APT signatures)";
    translations.en.t08_fgd = "The forum agreed because 5.7 serves as proactive intelligence to update existing SIEM/EDR rules with APT behaviors";
    
    translations.en.t01_notes = "No additional notes";
    translations.en.t01_fgd = "No changes";
    
    translations.en.t06_notes = "IT Security Supervisor -> add 5.14 Information transfer + 5.15 Access control + 8.22 Segregation";
    translations.en.t06_fgd = "5.14 for secure sensor data delivery; 5.15 so unauthorized personnel cannot log into the OT console; 8.22 to separate the factory VLAN from the corporate network, minimizing collateral damage";
`;

const idTranslations = `
    translations.id.t10_notes = "Cisometric Consulting Manager -> tambahkan 8.1 User endpoint devices (mencegah akses atau pencurian informasi dari laptop karyawan atau workstation lab)";
    translations.id.t10_fgd = "Forum sepakat menambahkan 8.1 karena spionase industri sering terjadi melalui endpoint fisik";
    
    translations.id.t11_notes = "Tidak ada catatan tambahan dari para ahli";
    translations.id.t11_fgd = "Tidak ada perubahan";
    
    translations.id.t09_notes = "IT Security Supervisor -> tambahkan 8.15 Logging (log untuk mendukung 8.16 Monitoring Activity)";
    translations.id.t09_fgd = "Forum sepakat karena logging memberikan jejak untuk deteksi dini dan analisis akar penyebab pasca-insiden";
    
    translations.id.t04_notes = "Cisometric + Planning Manager -> tambahkan 8.27 Secure Architecture (uji penetrasi menunjukkan kunci API terekspos; \\"secure by design\\" belum optimal) + 5.12 Classification (kategorikan data yang boleh atau tidak diekspos melalui API)";
    translations.id.t04_fgd = "Forum sepakat bahwa 8.27 sejalan dengan Tenet 3 per sesi; 5.12 harus memastikan API secara otomatis memblokir data \\"Rahasia\\"";
    
    translations.id.t07_notes = "Tidak ada catatan tambahan";
    translations.id.t07_fgd = "Tidak ada perubahan";
    
    translations.id.t02_notes = "5 ahli dari Citilink, Cisometric, Telkom University, IT Supervisor, IT Manager -> tambahkan 6.2 Terms of Employment + 5.32 IP Rights + 7.2 Physical Entry | ditolak: 6.4 Disciplinary Process | 6.3 Security Awareness";
    translations.id.t02_fgd = "GMO dipertahankan. 6.2 dasar hukum karyawan; 5.32 mencegah replikasi IP oleh mantan karyawan; 7.2 otomatisasi penonaktifan kartu ID saat mutasi. 6.4 ditolak karena SPT sudah ada; 6.3 ditolak karena fokus ke T.01 terlebih dahulu";
    
    translations.id.t03_notes = "Sr. GRC Consultant + 3 ahli lainnya -> tambahkan 5.20 Supplier agreements (VSAR/vendor due diligence) + 6.7 Remote Working (BYOD untuk peran sales) | Ditolak: 5.21 ICT supply chain | 8.3 Access restriction";
    translations.id.t03_fgd = "5.20 untuk validasi VSAR terhadap ISMS vendor; 6.7 untuk keamanan perangkat BYOD karyawan sales. 5.21 tidak relevan dengan masalah; 8.3 tidak relevan karena masalah melibatkan spoofing eksternal, bukan pelanggaran internal";
    
    translations.id.t05_notes = "Cisometric + IT Supervisor -> tambahkan 8.16 Monitoring (deteksi pola akses tidak wajar) + 8.7 Anti-malware (mengatasi penyebab utama pergerakan lateral)";
    translations.id.t05_fgd = "8.16 untuk mendeteksi lalu lintas internal anomali; 8.7 karena anti-malware endpoint menghilangkan kemampuan infeksi proksimal (penyebaran worm)";
    
    translations.id.t08_notes = "Cisometric Consulting Manager -> tambahkan 5.7 Threat intelligence (memberikan indikator IoC dan TTP terbaru ke alat keamanan untuk mengenali signature APT)";
    translations.id.t08_fgd = "Forum sepakat karena 5.7 berfungsi sebagai intelijen proaktif untuk memperbarui aturan SIEM/EDR yang ada dengan perilaku APT";
    
    translations.id.t01_notes = "Tidak ada catatan tambahan";
    translations.id.t01_fgd = "Tidak ada perubahan";
    
    translations.id.t06_notes = "IT Security Supervisor -> tambahkan 5.14 Information transfer + 5.15 Access control + 8.22 Segregation";
    translations.id.t06_fgd = "5.14 untuk pengiriman data sensor yang aman; 5.15 agar personel tidak sah tidak bisa login ke konsol OT; 8.22 untuk memisahkan VLAN pabrik dari jaringan korporat guna meminimalkan kerusakan kolateral";
`;

let content = fs.readFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', 'utf8');

// Replace everything between translations.en.t10_notes and translations.en.t06_fgd with the exact new text
content = content.replace(/translations\.en\.t10_notes = [\s\S]*?translations\.id\.t06_fgd = ".*?";/, englishTranslations.trim() + "\n\n" + idTranslations.trim());

fs.writeFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', content, 'utf8');
console.log('Restored original expert notes and FGD results!');
