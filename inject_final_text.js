const fs = require('fs');

let englishTranslations = `
    translations.en.t10_notes = "Cisometric Consulting Manager: <br> add 8.1 User endpoint devices (prevent access to or theft of information from employee laptops or lab workstations)";
    translations.en.t10_fgd = "According to the Consulting Manager at Cisometric, Control 8.1 User Endpoint Devices, can be added with the statement: \\"Can prevent unauthorized access, disclosure, or theft of information.\\" The forum agreed to add this control because industrial espionage often occurs via employees' laptops or lab workstations.";
    
    translations.en.t11_notes = "No additional notes from experts";
    translations.en.t11_fgd = "No changes";
    
    translations.en.t09_notes = "IT Security Supervisor: <br> add 8.15 Logging (logs to support 8.16 Monitoring Activity)";
    translations.en.t09_fgd = "According to experts, DetereCo's IT Security Supervisor can add Control 8.15 (Logging) with the statement: \\"Capable of logging all intrusion attempts and supporting Control 8.16 (Activity Monitoring).\\" The forum agreed to add the control because it provides an audit trail for early threat detection and post-incident root cause analysis.";
    
    translations.en.t04_notes = "Cisometric Consulting Manager: <br> add 8.27 Secure Architecture (pen tests show exposed API keys; \\"secure by design\\" is not yet optimal) <br><br> IT Planning & Strategy Manager at DetereCo: <br> add 5.12 Classification (categorize data that may or may not be exposed via API)";
    translations.en.t04_fgd = "According to the expert, Cisometric's Consulting Manager, Control 8.27 should be added, stating, \\"The results of penetration testing indicate that the 'secure by design' principle has not been optimally implemented.\\" The forum agreed to add the control because it aligns with Tenet 3, which applies on a per-session basis. <br><br> According to the IT Planning & Strategy Manager at DetereCo, control 5.12 should be added, stating: \\"Data must be categorized into those that may and may not be transmitted via the API.\\" The forum agreed to add this control because it ensures the API automatically blocks data classified as \\"Confidential\\".";
    
    translations.en.t07_notes = "No additional notes";
    translations.en.t07_fgd = "No changes";
    
    translations.en.t02_notes = "IT Security Risk at PT. Citilink Indonesia: <br> Experts noted, \\"Please clarify again in accordance with GMO COBIT 2019 regarding items that are 'Implemented but Not Documented,' as there are changes that have not been properly documented, particularly in the SLA documents.\\" <br><br> Consulting Manager at Cisometric: <br> add 6.2. Terms and conditions of employment. (To establish the basis for employee consent to maintain information security.) <br> add 6.4. Disciplinary process. (Historically, there have been incidents requiring a formal disciplinary action mechanism.) <br><br> Researcher at Telkom University: <br> add 6.3 Information Security Awareness, Education, and Training. (Equipping employees to consciously protect the company's critical data.) <br><br> IT Security Supervisor & IT Planning & Strategy Manager: <br> add 5.32 Intellectual Property Rights (To ensure the company's IP is not replicated from scratch, even if it is not direct theft) <br> add 7.2 Physical Entry (Employee access is via ID card, so the access of transferred employees should be deactivated immediately)";
    translations.en.t02_fgd = "A joint forum with IT Security Risk experts from PT. Citilink Indonesia agreed to maintain the GMO practice because APO12.03 Levels 2 and 3 are already fully implemented, so the focus should be on maximizing APO12.03 Level 4 to ensure that changes and updates are properly documented, particularly in the SLA documents. <br><br> According to the Consulting Manager at Cisometric, control 6.2 should be added, stating \\"the basis for employee consent to maintain information security,\\" as this can raise awareness regarding the prevention of confidential information leaks. <br><br> According to the IT Security Supervisor and IT Planning & Strategy Manager at DetereCo, control 5.32 should be added to prevent the theft or replication of intellectual property by former employees, even if it is not direct theft and control 7.2 should be implemented to automate the deactivation of employee ID cards for transferred employees. <br><br> The discussion forum agreed not to add control 6.4 because a follow-up process in the form of a Written Warning (SPT) already exists for past offenders, and also not to add control 6.3 because this control will first focus on threat T.01 (Compromised Credentials) to specifically address human negligence regarding credentials.";
    
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

let indonesianTranslations = `
    translations.id.t10_notes = "Cisometric Consulting Manager: <br> tambahkan 8.1 User endpoint devices (mencegah akses ke atau pencurian informasi dari laptop karyawan atau workstation lab)";
    translations.id.t10_fgd = "Menurut Consulting Manager di Cisometric, Kontrol 8.1 User Endpoint Devices, dapat ditambahkan dengan pernyataan: \\"Dapat mencegah akses, pengungkapan, atau pencurian informasi yang tidak sah.\\" Forum sepakat untuk menambahkan kontrol ini karena spionase industri sering terjadi melalui laptop atau workstation karyawan.";
    
    translations.id.t11_notes = "Tidak ada catatan tambahan dari pakar";
    translations.id.t11_fgd = "Tidak ada perubahan";
    
    translations.id.t09_notes = "IT Security Supervisor: <br> tambahkan 8.15 Logging (log untuk mendukung 8.16 Monitoring Activity)";
    translations.id.t09_fgd = "Menurut para ahli, IT Security Supervisor DetereCo dapat menambahkan Kontrol 8.15 (Logging) dengan pernyataan: \\"Mampu mencatat semua upaya intrusi dan mendukung Kontrol 8.16 (Activity Monitoring).\\" Forum sepakat untuk menambahkan kontrol tersebut karena menyediakan jejak audit untuk deteksi ancaman dini dan analisis akar penyebab pasca-insiden.";
    
    translations.id.t04_notes = "Cisometric Consulting Manager: <br> tambahkan 8.27 Secure Architecture (uji penetrasi menunjukkan kunci API terekspos; \\"secure by design\\" belum optimal) <br><br> IT Planning & Strategy Manager at DetereCo: <br> tambahkan 5.12 Classification (kategorikan data yang boleh dan tidak boleh terekspos melalui API)";
    translations.id.t04_fgd = "Menurut pakar, Consulting Manager Cisometric, Kontrol 8.27 harus ditambahkan, dengan menyatakan, \\"Hasil uji penetrasi menunjukkan bahwa prinsip 'secure by design' belum diterapkan secara optimal.\\" Forum sepakat untuk menambahkan kontrol ini karena sejalan dengan Tenet 3, yang berlaku berbasis per-sesi. <br><br> Menurut IT Planning & Strategy Manager di DetereCo, kontrol 5.12 harus ditambahkan, dengan menyatakan: \\"Data harus dikategorikan menjadi data yang boleh dan tidak boleh dikirim melalui API.\\" Forum sepakat untuk menambahkan kontrol ini karena memastikan API memblokir otomatis data yang diklasifikasikan sebagai \\"Rahasia\\".";
    
    translations.id.t07_notes = "Tidak ada catatan tambahan";
    translations.id.t07_fgd = "Tidak ada perubahan";
    
    translations.id.t02_notes = "IT Security Risk at PT. Citilink Indonesia: <br> Pakar mencatat, \\"Harap perjelas lagi sesuai dengan GMO COBIT 2019 terkait item yang 'Implemented but Not Documented,' karena ada perubahan yang tidak didokumentasikan dengan baik, terutama di dokumen SLA.\\" <br><br> Consulting Manager at Cisometric: <br> tambahkan 6.2. Terms and conditions of employment. (Untuk menetapkan dasar persetujuan karyawan guna menjaga keamanan informasi.) <br> tambahkan 6.4. Disciplinary process. (Secara historis, ada insiden yang memerlukan mekanisme tindakan disipliner resmi.) <br><br> Researcher at Telkom University: <br> tambahkan 6.3 Information Security Awareness, Education, and Training. (Membekali karyawan untuk secara sadar melindungi data kritis perusahaan.) <br><br> IT Security Supervisor & IT Planning & Strategy Manager: <br> tambahkan 5.32 Intellectual Property Rights (Untuk memastikan IP perusahaan tidak direplikasi dari awal, meskipun bukan pencurian langsung) <br> tambahkan 7.2 Physical Entry (Akses karyawan menggunakan kartu ID, sehingga akses karyawan yang dimutasi harus segera dinonaktifkan)";
    translations.id.t02_fgd = "Forum bersama pakar IT Security Risk dari PT. Citilink Indonesia sepakat untuk mempertahankan praktik GMO karena APO12.03 Level 2 dan 3 sudah diterapkan sepenuhnya, sehingga fokusnya harus pada memaksimalkan APO12.03 Level 4 guna memastikan perubahan dan pembaruan didokumentasikan dengan baik, terutama di dokumen SLA. <br><br> Menurut Consulting Manager di Cisometric, kontrol 6.2 harus ditambahkan, yang menyatakan \\"dasar persetujuan karyawan untuk menjaga keamanan informasi,\\" karena hal ini dapat meningkatkan kesadaran terkait pencegahan kebocoran informasi rahasia. <br><br> Menurut IT Security Supervisor dan IT Planning & Strategy Manager di DetereCo, kontrol 5.32 harus ditambahkan untuk mencegah pencurian atau replikasi kekayaan intelektual oleh mantan karyawan, meskipun bukan pencurian langsung dan kontrol 7.2 harus diterapkan untuk otomatisasi penonaktifan kartu ID bagi karyawan yang dimutasi. <br><br> Forum diskusi sepakat untuk tidak menambahkan kontrol 6.4 karena proses tindak lanjut berupa Surat Peringatan (SPT) sudah ada untuk pelanggar sebelumnya, dan juga tidak menambahkan kontrol 6.3 karena kontrol ini akan difokuskan terlebih dahulu pada ancaman T.01 (Compromised Credentials) guna mengatasi kelalaian manusia terkait kredensial secara spesifik.";
    
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

content = content.replace(/translations\.en\.t10_notes = [\s\S]*?translations\.id\.t06_fgd = ".*?";/, englishTranslations.trim() + "\n\n" + indonesianTranslations.trim());

fs.writeFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', content, 'utf8');
console.log('Final text restored!');
