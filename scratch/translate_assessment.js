const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// 1. Prepare translations for the Assessment Markdown
const assessmentEn = '# IT Risk Assessment\n\n| ID | Threat Type | Layer | Attacks | Likelihood | Impact | Risk Level |\n|:---:|---|---|---|:---:|:---:|:---:|\n| T.01 | Compromised Credentials | Identity | Theft and misuse of credentials (username and password)<br>via **Email Phishing**. | 3 | 1 | 🟢 3 Low |\n| T.02 | Insider Threats | Identity | Information leakage or cyber threats originating from<br>**internal company sources (employees)**. | 2 | 2 | 🟩 6 Low to Moderate |\n| T.03 | Supply Chain Attacks | Application | Infiltration into company communication systems via **third parties (middle-man)**<br>using email manipulation techniques (email phishing / domain spoofing).<br>Attackers impersonate official vendors to deceive the supply chain<br>into transferring funds to the attacker\'s account. | 1 | 2 | 🟢 5 Low |\n| T.04 | API & Integration Vulnerabilities | Application | Exploitation of integration points between systems (API Endpoints)<br>due to weak authentication mechanisms and security vulnerabilities,<br>allowing unauthorized parties to access internal data. | 3 | 2 | 🟩 8 Low to Moderate |\n| T.05 | Lateral Movement | Network | Malicious programs (BOT or Crypto Mining) infiltrate a user\'s device<br>and then spread across systems/computers within the<br>same network segment (VLAN). | 4 | 1 | 🟢 4 Low |\n| T.06 | IoT/OT Vulnerabilities | Network | Attacks exploiting security vulnerabilities in internet-connected hardware<br>(Smart Sensors, CNC assembly machines, or production control systems). | 1 | 1 | 🟢 1 Low |\n| T.07 | Replay Attacks | Network | Historically an unprecedented incident issue (attacks on Fingerprint,<br>Access Cards, Voice Recordings, and Face Recognition<br>have never occurred). | 3 | 2 | 🟩 8 Low to Moderate |\n| T.08 | Advanced Persistent Threats (APT) | Infrastructure | Implanting extremely small files (such as keygens / .c files<br>the size of a notepad script) that attempt to extract data slowly. | 4 | 1 | 🟢 4 Low |\n| T.09 | Ransomware & Malware Injection | Infrastructure | Locking data access or encrypting critical systems by **Petya-type Ransomware**<br>targeting user computers outside the company\'s secure network,<br>followed by a ransom demand. | 3 | 3 | 🟡 13 Moderate |\n| T.10 | Industrial Espionage | Data | Illegal attempts to steal trade secrets, technical specifications,<br>blueprints (CAD), and aerospace product formulas<br>for the benefit of competitors. | 1 | 4 | 🟡 15 Moderate |\n| T.11 | Disaster | Infrastructure | Large-scale and massive disasters such as Natural Disasters,<br>Human Errors, War, and technical disruptions<br>like regional power outages. | 1 | 4 | 🟡 15 Moderate |\n';

const dict = {
  id: {
    title: "# Penilaian Risiko TI",
    header: "| ID | Jenis Ancaman | Lapisan | Serangan | Kemungkinan | Dampak | Tingkat Risiko |",
    t01_type: "Kredensial Terkompromi", t01_layer: "Identitas", t01_atk: "Pencurian dan penyalahgunaan kredensial (nama pengguna dan kata sandi)<br>melalui **Phishing Email**.", t01_rl: "🟢 3 Rendah",
    t02_type: "Ancaman Orang Dalam", t02_layer: "Identitas", t02_atk: "Kebocoran informasi atau ancaman siber yang berasal dari<br>**sumber internal perusahaan (karyawan)**.", t02_rl: "🟩 6 Rendah ke Sedang",
    t03_type: "Serangan Rantai Pasokan", t03_layer: "Aplikasi", t03_atk: "Penyusupan ke sistem komunikasi perusahaan melalui **pihak ketiga (perantara)**<br>menggunakan teknik manipulasi email (phishing / spoofing domain).<br>Penyerang menyamar sebagai vendor resmi untuk menipu rantai pasokan<br>agar mentransfer dana ke akun penyerang.", t03_rl: "🟢 5 Rendah",
    t04_type: "Kerentanan API & Integrasi", t04_layer: "Aplikasi", t04_atk: "Eksploitasi titik integrasi antar sistem (Endpoint API)<br>karena mekanisme autentikasi yang lemah dan kerentanan keamanan,<br>memungkinkan pihak yang tidak berwenang mengakses data internal.", t04_rl: "🟩 8 Rendah ke Sedang",
    t05_type: "Pergerakan Lateral", t05_layer: "Jaringan", t05_atk: "Program berbahaya (BOT atau Crypto Mining) menyusup ke perangkat pengguna<br>lalu menyebar ke sistem/komputer dalam<br>segmen jaringan yang sama (VLAN).", t05_rl: "🟢 4 Rendah",
    t06_type: "Kerentanan IoT/OT", t06_layer: "Jaringan", t06_atk: "Serangan yang mengeksploitasi kerentanan keamanan pada perangkat yang terhubung ke internet<br>(Sensor Pintar, mesin perakitan CNC, atau sistem kontrol produksi).", t06_rl: "🟢 1 Rendah",
    t07_type: "Serangan Replay", t07_layer: "Jaringan", t07_atk: "Secara historis masalah insiden yang belum pernah terjadi sebelumnya (serangan pada Sidik Jari,<br>Kartu Akses, Rekaman Suara, dan Pengenalan Wajah<br>tidak pernah terjadi).", t07_rl: "🟩 8 Rendah ke Sedang",
    t08_type: "Ancaman Persisten Tingkat Lanjut (APT)", t08_layer: "Infrastruktur", t08_atk: "Menanamkan file yang sangat kecil (seperti keygen / file .c<br>seukuran skrip notepad) yang mencoba mengekstrak data secara perlahan.", t08_rl: "🟢 4 Rendah",
    t09_type: "Injeksi Ransomware & Malware", t09_layer: "Infrastruktur", t09_atk: "Mengunci akses data atau mengenkripsi sistem kritis oleh **Ransomware tipe Petya**<br>yang menargetkan komputer pengguna di luar jaringan aman perusahaan,<br>diikuti dengan permintaan tebusan.", t09_rl: "🟡 13 Sedang",
    t10_type: "Spionase Industri", t10_layer: "Data", t10_atk: "Upaya ilegal untuk mencuri rahasia dagang, spesifikasi teknis,<br>cetak biru (CAD), dan formula produk kedirgantaraan<br>untuk keuntungan pesaing.", t10_rl: "🟡 15 Sedang",
    t11_type: "Bencana", t11_layer: "Infrastruktur", t11_atk: "Bencana berskala besar dan masif seperti Bencana Alam,<br>Kesalahan Manusia, Perang, dan gangguan teknis<br>seperti pemadaman listrik regional.", t11_rl: "🟡 15 Sedang"
  },
  zh: {
    title: "# IT 风险评估",
    header: "| ID | 威胁类型 | 层级 | 攻击 | 可能性 | 影响 | 风险级别 |",
    t01_type: "凭证泄露", t01_layer: "身份", t01_atk: "通过 **电子邮件钓鱼**<br>窃取和滥用凭证（用户名和密码）。", t01_rl: "🟢 3 低",
    t02_type: "内部威胁", t02_layer: "身份", t02_atk: "源自<br>**公司内部（员工）** 的信息泄露或网络威胁。", t02_rl: "🟩 6 低到中等",
    t03_type: "供应链攻击", t03_layer: "应用程序", t03_atk: "通过 **第三方（中间人）**<br>使用电子邮件操纵技术（网络钓鱼/域欺骗）渗透公司通信系统。<br>攻击者冒充官方供应商欺骗供应链，<br>将资金转移到攻击者的账户。", t03_rl: "🟢 5 低",
    t04_type: "API与集成漏洞", t04_layer: "应用程序", t04_atk: "由于身份验证机制薄弱和安全漏洞，<br>利用系统之间的集成点（API 端点），<br>允许未经授权的各方访问内部数据。", t04_rl: "🟩 8 低到中等",
    t05_type: "横向移动", t05_layer: "网络", t05_atk: "恶意程序（BOT 或加密挖矿）渗透用户设备，<br>然后在<br>同一网段（VLAN）内的系统/计算机之间传播。", t05_rl: "🟢 4 低",
    t06_type: "IoT/OT漏洞", t06_layer: "网络", t06_atk: "利用连接互联网的硬件（智能传感器、CNC组装机或生产控制系统）<br>中的安全漏洞进行攻击。", t06_rl: "🟢 1 低",
    t07_type: "重放攻击", t07_layer: "网络", t07_atk: "历史上史无前例的事件（从未发生过针对指纹、<br>门禁卡、录音和面部识别的攻击）。", t07_rl: "🟩 8 低到中等",
    t08_type: "高级持续性威胁 (APT)", t08_layer: "基础设施", t08_atk: "植入极小的文件（如记事本脚本大小的<br>注册机 / .c 文件），试图缓慢提取数据。", t08_rl: "🟢 4 低",
    t09_type: "勒索软件和恶意软件注入", t09_layer: "基础设施", t09_atk: "通过 **Petya 型勒索软件** 锁定数据访问或加密关键系统，<br>目标是公司安全网络外部的用户计算机，<br>然后勒索赎金。", t09_rl: "🟡 13 中等",
    t10_type: "工业间谍", t10_layer: "数据", t10_atk: "为了竞争对手的利益，<br>非法企图窃取商业机密、技术规范、<br>蓝图（CAD）和航空航天产品配方。", t10_rl: "🟡 15 中等",
    t11_type: "灾难", t11_layer: "基础设施", t11_atk: "大规模严重灾难，例如自然灾害、<br>人为错误、战争和<br>区域停电等技术中断。", t11_rl: "🟡 15 中等"
  },
  es: {
    title: "# Evaluación de Riesgos de TI",
    header: "| ID | Tipo de Amenaza | Capa | Ataques | Probabilidad | Impacto | Nivel de Riesgo |",
    t01_type: "Credenciales Comprometidas", t01_layer: "Identidad", t01_atk: "Robo y uso indebido de credenciales (nombre de usuario y contraseña)<br>a través de **Phishing por correo electrónico**.", t01_rl: "🟢 3 Bajo",
    t02_type: "Amenazas Internas", t02_layer: "Identidad", t02_atk: "Fuga de información o amenazas cibernéticas originadas por<br>**fuentes internas de la empresa (empleados)**.", t02_rl: "🟩 6 Bajo a Moderado",
    t03_type: "Ataques a la Cadena de Suministro", t03_layer: "Aplicación", t03_atk: "Infiltración en los sistemas de comunicación de la empresa a través de **terceros (intermediarios)**<br>utilizando técnicas de manipulación de correo (phishing/suplantación de dominio).<br>Los atacantes se hacen pasar por proveedores para engañar a la cadena de suministro<br>y transferir fondos a la cuenta del atacante.", t03_rl: "🟢 5 Bajo",
    t04_type: "Vulnerabilidades de API e Integración", t04_layer: "Aplicación", t04_atk: "Explotación de puntos de integración entre sistemas (Endpoints de API)<br>debido a mecanismos de autenticación débiles y vulnerabilidades de seguridad,<br>permitiendo el acceso no autorizado a datos internos.", t04_rl: "🟩 8 Bajo a Moderado",
    t05_type: "Movimiento Lateral", t05_layer: "Red", t05_atk: "Programas maliciosos (BOT o minería de criptomonedas) se infiltran en el dispositivo<br>de un usuario y luego se propagan a través de sistemas/computadoras<br>dentro del mismo segmento de red (VLAN).", t05_rl: "🟢 4 Bajo",
    t06_type: "Vulnerabilidades IoT/OT", t06_layer: "Red", t06_atk: "Ataques que explotan vulnerabilidades de seguridad en hardware conectado a internet<br>(sensores inteligentes, máquinas CNC o sistemas de control de producción).", t06_rl: "🟢 1 Bajo",
    t07_type: "Ataques de Replay", t07_layer: "Red", t07_atk: "Históricamente un problema sin precedentes (nunca han ocurrido<br>ataques a huellas dactilares, tarjetas de acceso, grabaciones de voz y reconocimiento facial).", t07_rl: "🟩 8 Bajo a Moderado",
    t08_type: "Amenazas Persistentes Avanzadas (APT)", t08_layer: "Infraestructura", t08_atk: "Implantación de archivos extremadamente pequeños (como keygens / archivos .c<br>del tamaño de un script de bloc de notas) que intentan extraer datos lentamente.", t08_rl: "🟢 4 Bajo",
    t09_type: "Inyección de Ransomware y Malware", t09_layer: "Infraestructura", t09_atk: "Bloqueo de acceso a datos o cifrado de sistemas críticos por **Ransomware tipo Petya**<br>dirigido a computadoras de usuarios fuera de la red segura de la empresa,<br>seguido de una demanda de rescate.", t09_rl: "🟡 13 Moderado",
    t10_type: "Espionaje Industrial", t10_layer: "Datos", t10_atk: "Intentos ilegales de robar secretos comerciales, especificaciones técnicas,<br>planos (CAD) y fórmulas de productos aeroespaciales<br>para el beneficio de los competidores.", t10_rl: "🟡 15 Moderado",
    t11_type: "Desastre", t11_layer: "Infraestructura", t11_atk: "Desastres masivos a gran escala como desastres naturales,<br>errores humanos, guerras e interrupciones técnicas<br>como cortes de energía regionales.", t11_rl: "🟡 15 Moderado"
  },
  fr: {
    title: "# Évaluation des Risques Informatiques",
    header: "| ID | Type de Menace | Couche | Attaques | Probabilité | Impact | Niveau de Risque |",
    t01_type: "Identifiants Compromis", t01_layer: "Identité", t01_atk: "Vol et utilisation abusive des identifiants (nom d'utilisateur et mot de passe)<br>via **Hameçonnage par E-mail**.", t01_rl: "🟢 3 Faible",
    t02_type: "Menaces Internes", t02_layer: "Identité", t02_atk: "Fuite d'informations ou cybermenaces provenant de<br>**sources internes de l'entreprise (employés)**.", t02_rl: "🟩 6 Faible à Modéré",
    t03_type: "Attaques de la Chaîne d'Approvisionnement", t03_layer: "Application", t03_atk: "Infiltration dans les systèmes de communication de l'entreprise via **des tiers (intermédiaires)**<br>à l'aide de techniques de manipulation d'e-mails (hameçonnage / usurpation de domaine).<br>Les attaquants se font passer pour des fournisseurs officiels pour tromper la chaîne<br>d'approvisionnement afin de transférer des fonds vers le compte de l'attaquant.", t03_rl: "🟢 5 Faible",
    t04_type: "Vulnérabilités API et Intégration", t04_layer: "Application", t04_atk: "Exploitation des points d'intégration entre les systèmes (Endpoints API)<br>en raison de mécanismes d'authentification faibles et de vulnérabilités de sécurité,<br>permettant à des parties non autorisées d'accéder aux données internes.", t04_rl: "🟩 8 Faible à Modéré",
    t05_type: "Mouvement Latéral", t05_layer: "Réseau", t05_atk: "Des programmes malveillants (BOT ou minage de cryptomonnaie) s'infiltrent dans<br>l'appareil d'un utilisateur puis se propagent à travers les systèmes/ordinateurs<br>du même segment de réseau (VLAN).", t05_rl: "🟢 4 Faible",
    t06_type: "Vulnérabilités IoT/OT", t06_layer: "Réseau", t06_atk: "Attaques exploitant les vulnérabilités de sécurité du matériel connecté à Internet<br>(capteurs intelligents, machines CNC ou systèmes de contrôle de production).", t06_rl: "🟢 1 Faible",
    t07_type: "Attaques par Jeu", t07_layer: "Réseau", t07_atk: "Historiquement un problème sans précédent (les attaques sur les empreintes digitales,<br>les cartes d'accès, les enregistrements vocaux et la reconnaissance faciale<br>ne se sont jamais produites).", t07_rl: "🟩 8 Faible à Modéré",
    t08_type: "Menaces Persistantes Avancées (APT)", t08_layer: "Infrastructure", t08_atk: "Implantation de fichiers extrêmement petits (tels que des keygens / fichiers .c<br>de la taille d'un script de bloc-notes) qui tentent d'extraire des données lentement.", t08_rl: "🟢 4 Faible",
    t09_type: "Injection de Ransomware et Malware", t09_layer: "Infrastructure", t09_atk: "Blocage de l'accès aux données ou cryptage des systèmes critiques par un **Ransomware de type Petya**<br>ciblant les ordinateurs des utilisateurs en dehors du réseau sécurisé de l'entreprise,<br>suivi d'une demande de rançon.", t09_rl: "🟡 13 Modéré",
    t10_type: "Espionnage Industriel", t10_layer: "Données", t10_atk: "Tentatives illégales de voler des secrets commerciaux, des spécifications techniques,<br>des plans (CAD) et des formules de produits aérospatiaux<br>au profit des concurrents.", t10_rl: "🟡 15 Modéré",
    t11_type: "Catastrophe", t11_layer: "Infrastructure", t11_atk: "Catastrophes massives à grande échelle telles que les catastrophes naturelles,<br>les erreurs humaines, les guerres et les perturbations techniques<br>comme les pannes de courant régionales.", t11_rl: "🟡 15 Modéré"
  },
  de: {
    title: "# IT-Risikobewertung",
    header: "| ID | Bedrohungsart | Schicht | Angriffe | Wahrscheinlichkeit | Auswirkung | Risikostufe |",
    t01_type: "Kompromittierte Anmeldeinformationen", t01_layer: "Identität", t01_atk: "Diebstahl und Missbrauch von Anmeldeinformationen (Benutzername und Passwort)<br>über **E-Mail-Phishing**.", t01_rl: "🟢 3 Niedrig",
    t02_type: "Insider-Bedrohungen", t02_layer: "Identität", t02_atk: "Informationsabfluss oder Cyberbedrohungen, die von<br>**unternehmensinternen Quellen (Mitarbeitern)** ausgehen.", t02_rl: "🟩 6 Niedrig bis Mittel",
    t03_type: "Lieferkettenangriffe", t03_layer: "Anwendung", t03_atk: "Eindringen in die Kommunikationssysteme des Unternehmens über **Dritte (Mittelsmänner)**<br>unter Verwendung von E-Mail-Manipulationstechniken (E-Mail-Phishing / Domain-Spoofing).<br>Angreifer geben sich als offizielle Lieferanten aus, um die Lieferkette zu täuschen,<br>damit Gelder auf das Konto des Angreifers überwiesen werden.", t03_rl: "🟢 5 Niedrig",
    t04_type: "API- und Integrationsschwachstellen", t04_layer: "Anwendung", t04_atk: "Ausnutzung von Integrationspunkten zwischen Systemen (API-Endpunkten)<br>aufgrund schwacher Authentifizierungsmechanismen und Sicherheitslücken,<br>wodurch unbefugten Parteien der Zugriff auf interne Daten ermöglicht wird.", t04_rl: "🟩 8 Niedrig bis Mittel",
    t05_type: "Laterale Bewegung", t05_layer: "Netzwerk", t05_atk: "Bösartige Programme (BOT oder Krypto-Mining) infiltrieren das Gerät<br>eines Benutzers und breiten sich dann über Systeme/Computer innerhalb<br>desselben Netzwerksegments (VLAN) aus.", t05_rl: "🟢 4 Niedrig",
    t06_type: "IoT/OT-Schwachstellen", t06_layer: "Netzwerk", t06_atk: "Angriffe, die Sicherheitslücken in mit dem Internet verbundener Hardware ausnutzen<br>(intelligente Sensoren, CNC-Montagemaschinen oder Produktionskontrollsysteme).", t06_rl: "🟢 1 Niedrig",
    t07_type: "Replay-Angriffe", t07_layer: "Netzwerk", t07_atk: "Historisch gesehen ein beispielloses Vorfallsproblem (Angriffe auf Fingerabdrücke,<br>Zugangskarten, Sprachaufzeichnungen und Gesichtserkennung<br>sind noch nie aufgetreten).", t07_rl: "🟩 8 Niedrig bis Mittel",
    t08_type: "Fortgeschrittene anhaltende Bedrohungen (APT)", t08_layer: "Infrastruktur", t08_atk: "Einpflanzen extrem kleiner Dateien (z. B. Keygens / .c-Dateien<br>in der Größe eines Notepad-Skripts), die versuchen, Daten langsam zu extrahieren.", t08_rl: "🟢 4 Niedrig",
    t09_type: "Ransomware- und Malware-Injektion", t09_layer: "Infrastruktur", t09_atk: "Sperrung des Datenzugriffs oder Verschlüsselung kritischer Systeme durch **Ransomware vom Typ Petya**,<br>die auf Computer von Benutzern außerhalb des sicheren Unternehmensnetzwerks abzielt,<br>gefolgt von einer Lösegeldforderung.", t09_rl: "🟡 13 Mittel",
    t10_type: "Industriespionage", t10_layer: "Daten", t10_atk: "Illegale Versuche, Geschäftsgeheimnisse, technische Spezifikationen,<br>Baupläne (CAD) und Formeln für Luft- und Raumfahrtprodukte<br>zum Vorteil von Wettbewerbern zu stehlen.", t10_rl: "🟡 15 Mittel",
    t11_type: "Katastrophe", t11_layer: "Infrastruktur", t11_atk: "Großflächige und massive Katastrophen wie Naturkatastrophen,<br>menschliches Versagen, Krieg und technische Störungen<br>wie regionale Stromausfälle.", t11_rl: "🟡 15 Mittel"
  },
  ar: {
    title: "# تقييم مخاطر تكنولوجيا المعلومات",
    header: "| ID | نوع التهديد | الطبقة | الهجمات | الاحتمالية | التأثير | مستوى الخطر |",
    t01_type: "بيانات الاعتماد المخترقة", t01_layer: "الهوية", t01_atk: "سرقة وإساءة استخدام بيانات الاعتماد (اسم المستخدم وكلمة المرور)<br>عبر **التصيد الاحتيالي عبر البريد الإلكتروني**.", t01_rl: "🟢 3 منخفض",
    t02_type: "التهديدات الداخلية", t02_layer: "الهوية", t02_atk: "تسرب المعلومات أو التهديدات السيبرانية الناشئة عن<br>**مصادر الشركة الداخلية (الموظفين)**.", t02_rl: "🟩 6 منخفض إلى متوسط",
    t03_type: "هجمات سلسلة التوريد", t03_layer: "التطبيق", t03_atk: "التسلل إلى أنظمة اتصالات الشركة عبر **جهات خارجية (وسطاء)**<br>باستخدام تقنيات التلاعب بالبريد الإلكتروني (التصيد الاحتيالي/انتحال المجال).<br>ينتحل المهاجمون صفة البائعين الرسميين لخداع سلسلة التوريد<br>لتحويل الأموال إلى حساب المهاجم.", t03_rl: "🟢 5 منخفض",
    t04_type: "ثغرات واجهة برمجة التطبيقات والتكامل", t04_layer: "التطبيق", t04_atk: "استغلال نقاط التكامل بين الأنظمة (نقاط نهاية API)<br>بسبب ضعف آليات المصادقة والثغرات الأمنية،<br>مما يسمح للأطراف غير المصرح لها بالوصول إلى البيانات الداخلية.", t04_rl: "🟩 8 منخفض إلى متوسط",
    t05_type: "الحركة الجانبية", t05_layer: "الشبكة", t05_atk: "تتسلل البرامج الضارة (BOT أو Crypto Mining) إلى جهاز المستخدم<br>ثم تنتشر عبر الأنظمة/أجهزة الكمبيوتر داخل<br>نفس مقطع الشبكة (VLAN).", t05_rl: "🟢 4 منخفض",
    t06_type: "ثغرات IoT/OT", t06_layer: "الشبكة", t06_atk: "هجمات تستغل الثغرات الأمنية في الأجهزة المتصلة بالإنترنت<br>(أجهزة الاستشعار الذكية أو آلات تجميع CNC أو أنظمة التحكم في الإنتاج).", t06_rl: "🟢 1 منخفض",
    t07_type: "هجمات إعادة الإرسال", t07_layer: "الشبكة", t07_atk: "تاريخيا مشكلة حادث غير مسبوق (الهجمات على بصمات الأصابع،<br>وبطاقات الوصول، والتسجيلات الصوتية، والتعرف على الوجه<br>لم تحدث قط).", t07_rl: "🟩 8 منخفض إلى متوسط",
    t08_type: "التهديدات المستمرة المتقدمة (APT)", t08_layer: "البنية التحتية", t08_atk: "زرع ملفات صغيرة جدًا (مثل keygens / ملفات .c<br>بحجم برنامج نصي المفكرة) تحاول استخراج البيانات ببطء.", t08_rl: "🟢 4 منخفض",
    t09_type: "حقن برامج الفدية والبرامج الضارة", t09_layer: "البنية التحتية", t09_atk: "قفل الوصول إلى البيانات أو تشفير الأنظمة الحرجة بواسطة **برامج الفدية من نوع Petya**<br>التي تستهدف أجهزة كمبيوتر المستخدمين خارج شبكة الشركة الآمنة،<br>يليها طلب فدية.", t09_rl: "🟡 13 متوسط",
    t10_type: "التجسس الصناعي", t10_layer: "البيانات", t10_atk: "المحاولات غير القانونية لسرقة الأسرار التجارية والمواصفات الفنية<br>والمخططات (CAD) وصيغ منتجات الطيران<br>لصالح المنافسين.", t10_rl: "🟡 15 متوسط",
    t11_type: "الكوارث", t11_layer: "البنية التحتية", t11_atk: "الكوارث واسعة النطاق والهائلة مثل الكوارث الطبيعية<br>والأخطاء البشرية والحروب والاضطرابات الفنية<br>مثل انقطاع التيار الكهربائي الإقليمي.", t11_rl: "🟡 15 متوسط"
  },
  ru: {
    title: "# Оценка ИТ-рисков",
    header: "| ID | Тип угрозы | Уровень | Атаки | Вероятность | Влияние | Уровень риска |",
    t01_type: "Скомпрометированные учетные данные", t01_layer: "Идентичность", t01_atk: "Кража и неправомерное использование учетных данных (имя пользователя и пароль)<br>через **фишинг по электронной почте**.", t01_rl: "🟢 3 Низкий",
    t02_type: "Внутренние угрозы", t02_layer: "Идентичность", t02_atk: "Утечка информации или киберугрозы, исходящие из<br>**внутренних источников компании (сотрудников)**.", t02_rl: "🟩 6 От низкого до среднего",
    t03_type: "Атаки на цепочку поставок", t03_layer: "Приложение", t03_atk: "Проникновение в системы связи компании через **третьих лиц (посредников)**<br>с использованием методов манипулирования электронной почтой (фишинг/подмена домена).<br>Злоумышленники выдают себя за официальных поставщиков, чтобы обмануть цепочку поставок<br>и заставить перевести средства на счет злоумышленника.", t03_rl: "🟢 5 Низкий",
    t04_type: "Уязвимости API и интеграции", t04_layer: "Приложение", t04_atk: "Эксплуатация точек интеграции между системами (конечных точек API)<br>из-за слабых механизмов аутентификации и уязвимостей безопасности,<br>что позволяет неавторизованным сторонам получать доступ к внутренним данным.", t04_rl: "🟩 8 От низкого до среднего",
    t05_type: "Латеральное движение", t05_layer: "Сеть", t05_atk: "Вредоносные программы (бот-сети или майнинг криптовалют) проникают на устройство пользователя,<br>а затем распространяются по системам/компьютерам внутри<br>одного сетевого сегмента (VLAN).", t05_rl: "🟢 4 Низкий",
    t06_type: "Уязвимости IoT/OT", t06_layer: "Сеть", t06_atk: "Атаки, использующие уязвимости безопасности в оборудовании, подключенном к Интернету<br>(умные датчики, сборочные машины с ЧПУ или системы управления производством).", t06_rl: "🟢 1 Низкий",
    t07_type: "Атаки повторного воспроизведения", t07_layer: "Сеть", t07_atk: "Исторически беспрецедентная проблема (атак на отпечатки пальцев,<br>карты доступа, голосовые записи и распознавание лиц<br>никогда не было).", t07_rl: "🟩 8 От низкого до среднего",
    t08_type: "Целевые атаки (APT)", t08_layer: "Инфраструктура", t08_atk: "Внедрение чрезвычайно мелких файлов (таких как генераторы ключей / файлы .c<br>размером со скрипт блокнота), которые пытаются медленно извлекать данные.", t08_rl: "🟢 4 Низкий",
    t09_type: "Внедрение программ-вымогателей и вредоносного ПО", t09_layer: "Инфраструктура", t09_atk: "Блокировка доступа к данным или шифрование критических систем **программами-вымогателями типа Petya**,<br>нацеленными на компьютеры пользователей за пределами защищенной сети компании,<br>с последующим требованием выкупа.", t09_rl: "🟡 13 Средний",
    t10_type: "Промышленный шпионаж", t10_layer: "Данные", t10_atk: "Незаконные попытки кражи коммерческой тайны, технических спецификаций,<br>чертежей (САПР) и формул аэрокосмической продукции<br>в интересах конкурентов.", t10_rl: "🟡 15 Средний",
    t11_type: "Катастрофа", t11_layer: "Инфраструктура", t11_atk: "Крупномасштабные и массовые бедствия, такие как стихийные бедствия,<br>человеческие ошибки, войны и технические сбои,<br>такие как региональные отключения электроэнергии.", t11_rl: "🟡 15 Средний"
  },
  ko: {
    title: "# IT 위험 평가",
    header: "| ID | 위협 유형 | 계층 | 공격 | 발생 가능성 | 영향 | 위험 수준 |",
    t01_type: "손상된 자격 증명", t01_layer: "신원", t01_atk: "**이메일 피싱**을 통한<br>자격 증명(사용자 이름 및 비밀번호)의 도용 및 오용.", t01_rl: "🟢 3 낮음",
    t02_type: "내부자 위협", t02_layer: "신원", t02_atk: "**회사 내부 소스(직원)** 에서 발생하는<br>정보 유출 또는 사이버 위협.", t02_rl: "🟩 6 낮음에서 보통",
    t03_type: "공급망 공격", t03_layer: "애플리케이션", t03_atk: "이메일 조작 기술(이메일 피싱/도메인 스푸핑)을 사용하여<br>**제3자(중개인)** 를 통해 회사 통신 시스템에 침투합니다.<br>공격자는 공식 공급업체를 사칭하여 공급망을 속여<br>공격자의 계정으로 자금을 이체하도록 합니다.", t03_rl: "🟢 5 낮음",
    t04_type: "API 및 통합 취약점", t04_layer: "애플리케이션", t04_atk: "약한 인증 메커니즘 및 보안 취약점으로 인해<br>시스템 간의 통합 지점(API 엔드포인트)을 악용하여<br>권한이 없는 당사자가 내부 데이터에 접근하도록 허용합니다.", t04_rl: "🟩 8 낮음에서 보통",
    t05_type: "내부 이동", t05_layer: "네트워크", t05_atk: "악성 프로그램(BOT 또는 암호화폐 채굴)이 사용자 기기에 침투한 다음<br>동일한 네트워크 세그먼트(VLAN) 내의<br>시스템/컴퓨터로 확산됩니다.", t05_rl: "🟢 4 낮음",
    t06_type: "IoT/OT 취약점", t06_layer: "네트워크", t06_atk: "인터넷 연결 하드웨어(스마트 센서, CNC 조립 기계 또는 생산 제어 시스템)의<br>보안 취약점을 악용하는 공격.", t06_rl: "🟢 1 낮음",
    t07_type: "재전송 공격", t07_layer: "네트워크", t07_atk: "역사적으로 전례 없는 사고 문제(지문, 출입 카드, 음성 녹음 및 얼굴 인식에 대한<br>공격은 발생한 적이 없음).", t07_rl: "🟩 8 낮음에서 보통",
    t08_type: "지능형 지속 위협 (APT)", t08_layer: "인프라", t08_atk: "데이터를 천천히 추출하려는 매우 작은 파일(예: 메모장 스크립트 크기의<br>키젠 / .c 파일)을 심습니다.", t08_rl: "🟢 4 낮음",
    t09_type: "랜섬웨어 및 멀웨어 주입", t09_layer: "인프라", t09_atk: "회사 보안 네트워크 외부의 사용자 컴퓨터를 표적으로 삼는<br>**Petya 유형 랜섬웨어** 에 의한 데이터 접근 차단 또는 중요 시스템 암호화,<br>이후 몸값 요구.", t09_rl: "🟡 13 보통",
    t10_type: "산업 스파이", t10_layer: "데이터", t10_atk: "경쟁업체의 이익을 위해 영업 비밀, 기술 사양,<br>청사진(CAD) 및 항공 우주 제품 공식을<br>훔치려는 불법적인 시도.", t10_rl: "🟡 15 보통",
    t11_type: "재해", t11_layer: "인프라", t11_atk: "자연재해, 인적 오류, 전쟁, 그리고<br>지역적 정전과 같은 기술적 중단 등<br>대규모의 거대한 재해.", t11_rl: "🟡 15 보통"
  },
  ja: {
    title: "# IT リスクアセスメント",
    header: "| ID | 脅威タイプ | レイヤー | 攻撃 | 可能性 | 影響 | リスクレベル |",
    t01_type: "侵害された認証情報", t01_layer: "アイデンティティ", t01_atk: "**メールフィッシング**による<br>認証情報（ユーザー名とパスワード）の盗難と悪用。", t01_rl: "🟢 3 低",
    t02_type: "内部脅威", t02_layer: "アイデンティティ", t02_atk: "**企業内部（従業員）**から発生する<br>情報漏洩またはサイバー脅威。", t02_rl: "🟩 6 低から中",
    t03_type: "サプライチェーン攻撃", t03_layer: "アプリケーション", t03_atk: "メール操作技術（メールフィッシング/ドメインスプーフィング）を使用した<br>**第三者（中間者）**経由での企業の通信システムへの侵入。<br>攻撃者は公式ベンダーになりすまし、サプライチェーンを欺いて<br>攻撃者の口座に資金を送金させます。", t03_rl: "🟢 5 低",
    t04_type: "APIと統合の脆弱性", t04_layer: "アプリケーション", t04_atk: "脆弱な認証メカニズムとセキュリティの脆弱性による<br>システム間の統合ポイント（APIエンドポイント）の悪用。<br>権限のない第三者が内部データにアクセスできるようにします。", t04_rl: "🟩 8 低から中",
    t05_type: "ラテラルムーブメント", t05_layer: "ネットワーク", t05_atk: "悪意のあるプログラム（BOTまたは仮想通貨マイニング）がユーザーのデバイスに侵入し、<br>同じネットワークセグメント（VLAN）内の<br>システム/コンピューターに拡散します。", t05_rl: "🟢 4 低",
    t06_type: "IoT/OTの脆弱性", t06_layer: "ネットワーク", t06_atk: "インターネットに接続されたハードウェア（スマートセンサー、CNC組立機、または生産管理システム）<br>のセキュリティの脆弱性を悪用する攻撃。", t06_rl: "🟢 1 低",
    t07_type: "リプレイ攻撃", t07_layer: "ネットワーク", t07_atk: "歴史的に前例のないインシデントの問題（指紋、アクセスカード、<br>音声録音、および顔認識に対する攻撃は発生したことがありません）。", t07_rl: "🟩 8 低から中",
    t08_type: "高度な持続的脅威 (APT)", t08_layer: "インフラ", t08_atk: "データをゆっくりと抽出することを試みる、非常に小さなファイル（メモ帳スクリプトサイズの<br>キージェン/ .cファイルなど）の埋め込み。", t08_rl: "🟢 4 低",
    t09_type: "ランサムウェアとマルウェアのインジェクション", t09_layer: "インフラ", t09_atk: "企業のセキュアなネットワーク外のユーザーコンピューターを標的とした<br>**Petya型ランサムウェア**によるデータアクセスのロックまたは重要なシステムの暗号化、<br>それに続く身代金の要求。", t09_rl: "🟡 13 中",
    t10_type: "産業スパイ", t10_layer: "データ", t10_atk: "競合他社の利益のために、企業秘密、技術仕様、<br>青写真（CAD）、および航空宇宙製品の配合を<br>盗もうとする違法な試み。", t10_rl: "🟡 15 中",
    t11_type: "災害", t11_layer: "インフラ", t11_atk: "自然災害、人為的ミス、戦争、および<br>地域的な停電などの技術的混乱といった、<br>大規模で甚大な災害。", t11_rl: "🟡 15 中"
  }
};

let assessments = { en: assessmentEn };

for (const lang of ['id', 'zh', 'es', 'fr', 'de', 'ar', 'ru', 'ko', 'ja']) {
  const d = dict[lang];
  let md = `${d.title}\n\n${d.header}\n|:---:|---|---|---|:---:|:---:|:---:|\n`;
  md += `| T.01 | ${d.t01_type} | ${d.t01_layer} | ${d.t01_atk} | 3 | 1 | ${d.t01_rl} |\n`;
  md += `| T.02 | ${d.t02_type} | ${d.t02_layer} | ${d.t02_atk} | 2 | 2 | ${d.t02_rl} |\n`;
  md += `| T.03 | ${d.t03_type} | ${d.t03_layer} | ${d.t03_atk} | 1 | 2 | ${d.t03_rl} |\n`;
  md += `| T.04 | ${d.t04_type} | ${d.t04_layer} | ${d.t04_atk} | 3 | 2 | ${d.t04_rl} |\n`;
  md += `| T.05 | ${d.t05_type} | ${d.t05_layer} | ${d.t05_atk} | 4 | 1 | ${d.t05_rl} |\n`;
  md += `| T.06 | ${d.t06_type} | ${d.t06_layer} | ${d.t06_atk} | 1 | 1 | ${d.t06_rl} |\n`;
  md += `| T.07 | ${d.t07_type} | ${d.t07_layer} | ${d.t07_atk} | 3 | 2 | ${d.t07_rl} |\n`;
  md += `| T.08 | ${d.t08_type} | ${d.t08_layer} | ${d.t08_atk} | 4 | 1 | ${d.t08_rl} |\n`;
  md += `| T.09 | ${d.t09_type} | ${d.t09_layer} | ${d.t09_atk} | 3 | 3 | ${d.t09_rl} |\n`;
  md += `| T.10 | ${d.t10_type} | ${d.t10_layer} | ${d.t10_atk} | 1 | 4 | ${d.t10_rl} |\n`;
  md += `| T.11 | ${d.t11_type} | ${d.t11_layer} | ${d.t11_atk} | 1 | 4 | ${d.t11_rl} |\n`;
  assessments[lang] = md;
}

// 2. Replace embeddedMarkdown.assessment 
const originalAssessmentRegex = /assessment:\s*'# IT Risk Assessment[\s\S]*?\| T\.11 \|[\s\S]*?\\n',/;

if (originalAssessmentRegex.test(html)) {
  html = html.replace(originalAssessmentRegex, 'assessment: ' + JSON.stringify(assessments, null, 8) + ',');
} else {
  console.log("Could not find the original assessment string in index.html");
}

// 3. Update renderMarkdown
const renderMarkdownRegex = /document\.getElementById\("md-assessment"\)\.innerHTML\s*=\s*marked\.parse\(\s*embeddedMarkdown\.assessment,?\s*\);/g;

if (renderMarkdownRegex.test(html)) {
  html = html.replace(renderMarkdownRegex, `const lang = (typeof currentLang !== 'undefined') ? currentLang : 'en';\n        document.getElementById("md-assessment").innerHTML = marked.parse(\n          embeddedMarkdown.assessment[lang] || embeddedMarkdown.assessment.en,\n        );`);
} else {
  console.log("Could not find renderMarkdown implementation for assessment");
}

// 4. Update applyLanguage to call renderMarkdown()
const applyLangRegex = /(updateDashboard\(currentFilter\);\s*\n\s*)}/g;

if (applyLangRegex.test(html)) {
  html = html.replace(applyLangRegex, '$1  renderMarkdown();\n    }');
} else {
  console.log("Could not find updateDashboard in applyLanguage");
}

fs.writeFileSync('index.html', html, 'utf8');
console.log("Done");
