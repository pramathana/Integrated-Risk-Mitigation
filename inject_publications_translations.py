import re

file_path = "c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

regex_replacements = [
    # Section Header
    (r'<h2 style="font-size: 1\.8rem; font-weight: 700; margin-top: 0; margin-bottom: 1rem; color:\s*var\(--text-primary\);">\s*Related Publications\s*</h2>',
     '<h2 style="font-size: 1.8rem; font-weight: 700; margin-top: 0; margin-bottom: 1rem; color: var(--text-primary);" data-i18n="pub_section_title">Related Publications</h2>'),
    
    (r'<h3 style="color: var\(--pub-subtitle-color\); font-size: 1\.1rem; font-weight: 600; margin-bottom: 2rem;">\s*Extending the Bachelor Thesis into International IEEE Xplore Publications\s*</h3>',
     '<h3 style="color: var(--pub-subtitle-color); font-size: 1.1rem; font-weight: 600; margin-bottom: 2rem;" data-i18n="pub_section_subtitle">Extending the Bachelor Thesis into International IEEE Xplore Publications</h3>'),
    
    (r'<p class="pub-desc" style="font-size: 1rem; text-align: justify; margin: 0;">\s*The Integrated Risk Mitigation Program based on Zero Trust Architecture \(ZTA\).*?IEEE Xplore Digital Library database\.\s*</p>',
     '<p class="pub-desc" style="font-size: 1rem; text-align: justify; margin: 0;" data-i18n="pub_section_desc">The Integrated Risk Mitigation Program based on Zero Trust Architecture (ZTA), developed in this Bachelor\'s Thesis, has undergone a peer-review process and been accepted for publication at two international conferences. These two research outputs detail the specific application of the main framework within critical operational domains and will be indexed in the IEEE Xplore Digital Library database.</p>'),
    
    # Badges
    (r'<a href="([^"]+)" target="_blank"\s*class="pub-badge-accepted" style="text-decoration: none; cursor: pointer;"><i\s*class="ph-fill ph-check-circle"></i> ACCEPTED</a>',
     r'<a href="\1" target="_blank" class="pub-badge-accepted" style="text-decoration: none; cursor: pointer;" data-i18n="pub_badge_accepted"><i class="ph-fill ph-check-circle"></i> ACCEPTED</a>'),
     
    # Paper 1
    (r'<h2 class="pub-title">Designing an Integrated Cyber Risk Mitigation Based on Zero Trust Architecture: A\s*Conceptual Framework for the Aerospace Industry</h2>',
     '<h2 class="pub-title" data-i18n="pub_1_title">Designing an Integrated Cyber Risk Mitigation Based on Zero Trust Architecture: A Conceptual Framework for the Aerospace Industry</h2>'),
     
    (r'<span class="pub-meta-value"><a href="https://icadeis.org/index.php" target="_blank"\s*style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> \(The 2026\s*International\s*Conference on Advancement in Data\s*Science, E-learning, and Information Systems\)</span>',
     '<span class="pub-meta-value" data-i18n="pub_1_conf"><a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (The 2026 International Conference on Advancement in Data Science, E-learning, and Information Systems)</span>'),
     
    (r'<span class="pub-meta-value">This paper focuses on <strong>bridging the gap</strong> between\s*<strong>strategic IT\s*governance</strong> and\s*<strong>technical execution</strong> by designing a <strong>5-layer Zero Trust framework</strong>\s*specifically to protect\s*<strong>critical ERP\s*systems</strong> and <strong>Access Rights</strong> from <strong>Privilege Escalation</strong> in\s*converged IT/OT aerospace environments\.</span>',
     '<span class="pub-meta-value" data-i18n="pub_1_focus">This paper focuses on <strong>bridging the gap</strong> between <strong>strategic IT governance</strong> and <strong>technical execution</strong> by designing a <strong>5-layer Zero Trust framework</strong> specifically to protect <strong>critical ERP systems</strong> and <strong>Access Rights</strong> from <strong>Privilege Escalation</strong> in converged IT/OT aerospace environments.</span>'),
     
    (r'<span class="pub-meta-value">This paper is a <strong>direct extraction of the core foundation</strong>\s*established in my\s*Bachelor\'s Thesis\. While the thesis comprehensively covers the entire security mitigation program up to\s*the expert validation stage, this paper specifically highlights the <strong>conceptual design\s*phase</strong>\. It introduces\s*the <strong>"5-Layer Zero Trust Defense Model"</strong> as a targeted solution to combat specific threats,\s*such as <strong>illegal\s*privilege escalation</strong>, within <strong>Enterprise Resource Planning \(ERP\)</strong> systems in the\s*aerospace industry\.</span>',
     '<span class="pub-meta-value" data-i18n="pub_1_relation">This paper is a <strong>direct extraction of the core foundation</strong> established in my Bachelor\'s Thesis. While the thesis comprehensively covers the entire security mitigation program up to the expert validation stage, this paper specifically highlights the <strong>conceptual design phase</strong>. It introduces the <strong>"5-Layer Zero Trust Defense Model"</strong> as a targeted solution to combat specific threats, such as <strong>illegal privilege escalation</strong>, within <strong>Enterprise Resource Planning (ERP)</strong> systems in the aerospace industry.</span>'),
     
    # Paper 2
    (r'<h2 class="pub-title">A Zero Trust Security Architecture for IoT and Cloud: Conceptualizing a Risk Mitigation\s*Program for Digital Twins in the Aerospace Industry</h2>',
     '<h2 class="pub-title" data-i18n="pub_2_title">A Zero Trust Security Architecture for IoT and Cloud: Conceptualizing a Risk Mitigation Program for Digital Twins in the Aerospace Industry</h2>'),
     
    (r'<span class="pub-meta-value"><a href="https://iciss.goesmart.id/" target="_blank"\s*style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> \(The 13th\s*International\s*Conference on ICT for Smart\s*Societies\)</span>',
     '<span class="pub-meta-value" data-i18n="pub_2_conf"><a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (The 13th International Conference on ICT for Smart Societies)</span>'),
     
    (r'<span class="pub-meta-value">This paper focuses on <strong>adapting the Zero Trust framework</strong> for\s*<strong>machine-to-machine \(M2M\) interactions</strong> to secure the data flow between physical\s*<strong>IoT Edge Gateways</strong> and <strong>Cloud Digital Twins</strong> against <strong>False Data\s*Injection \(FDI\)</strong> attacks\.</span>',
     '<span class="pub-meta-value" data-i18n="pub_2_focus">This paper focuses on <strong>adapting the Zero Trust framework</strong> for <strong>machine-to-machine (M2M) interactions</strong> to secure the data flow between physical <strong>IoT Edge Gateways</strong> and <strong>Cloud Digital Twins</strong> against <strong>False Data Injection (FDI)</strong> attacks.</span>'),
     
    (r'<span class="pub-meta-value">This paper serves as a <strong>technical extension</strong> of the framework\s*developed in the\s*Bachelor\'s Thesis\. While the thesis focuses on broader enterprise security, this paper specifically\s*applies the <strong>"5-Layer Zero Trust Defense Model"</strong> to protect <strong>automated\s*machine-to-machine \(M2M\)\s*communications</strong> within <strong>IoT and Cloud \(Digital Twins\)</strong> ecosystems\. Validated\s*through <strong>STRIDE Analysis</strong>, the\s*paper proves that the security framework is <strong>highly adaptable</strong>; it is not only robust in\s*securing human\s*access but also analytically proven to prevent <strong>False Data Injection \(FDI\)</strong> threats on\s*physical factory\s*sensors\.</span>',
     '<span class="pub-meta-value" data-i18n="pub_2_relation">This paper serves as a <strong>technical extension</strong> of the framework developed in the Bachelor\'s Thesis. While the thesis focuses on broader enterprise security, this paper specifically applies the <strong>"5-Layer Zero Trust Defense Model"</strong> to protect <strong>automated machine-to-machine (M2M) communications</strong> within <strong>IoT and Cloud (Digital Twins)</strong> ecosystems. Validated through <strong>STRIDE Analysis</strong>, the paper proves that the security framework is <strong>highly adaptable</strong>; it is not only robust in securing human access but also analytically proven to prevent <strong>False Data Injection (FDI)</strong> threats on physical factory sensors.</span>'),
     
    # Shared labels
    (r'<span class="pub-meta-label">Conference</span>', '<span class="pub-meta-label" data-i18n="pub_label_conference">Conference</span>'),
    (r'<span class="pub-meta-label">Research Focus</span>', '<span class="pub-meta-label" data-i18n="pub_label_research_focus">Research Focus</span>'),
    (r'<span class="pub-meta-label">Relation to Bachelor\'s Thesis</span>', '<span class="pub-meta-label" data-i18n="pub_label_relation">Relation to Bachelor\'s Thesis</span>'),
    (r'<span class="pub-meta-label">Standards Applied</span>', '<span class="pub-meta-label" data-i18n="pub_label_standards">Standards Applied</span>'),
    
    (r'<div class="pub-footer-text">\s*<strong>Publisher:</strong> IEEE \(Institute of Electrical and Electronics Engineers\)<br>\s*<strong>Indexing:</strong> Scopus / IEEE Xplore\s*</div>',
     '<div class="pub-footer-text" data-i18n="pub_footer_text"><strong>Publisher:</strong> IEEE (Institute of Electrical and Electronics Engineers)<br><strong>Indexing:</strong> Scopus / IEEE Xplore</div>'),
     
    (r'<a href="https://ieeexplore.ieee.org/Xplore/home.jsp" target="_blank" rel="noopener noreferrer"\s*class="pub-link-btn">\s*<i class="ph-bold ph-arrow-square-out"></i> Access\s*</a>',
     '<a href="https://ieeexplore.ieee.org/Xplore/home.jsp" target="_blank" rel="noopener noreferrer" class="pub-link-btn" data-i18n="pub_btn_access"><i class="ph-bold ph-arrow-square-out"></i> Access</a>')
]

for pat, repl in regex_replacements:
    content = re.sub(pat, repl, content, flags=re.DOTALL)

translations = {
    'en': {
        'menu_publications': 'Related Publications',
        'pub_section_title': 'Related Publications',
        'pub_section_subtitle': 'Extending the Bachelor Thesis into International IEEE Xplore Publications',
        'pub_section_desc': 'The Integrated Risk Mitigation Program based on Zero Trust Architecture (ZTA), developed in this Bachelor\'s Thesis, has undergone a peer-review process and been accepted for publication at two international conferences. These two research outputs detail the specific application of the main framework within critical operational domains and will be indexed in the IEEE Xplore Digital Library database.',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> ACCEPTED',
        'pub_1_title': 'Designing an Integrated Cyber Risk Mitigation Based on Zero Trust Architecture: A Conceptual Framework for the Aerospace Industry',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (The 2026 International Conference on Advancement in Data Science, E-learning, and Information Systems)',
        'pub_1_focus': 'This paper focuses on <strong>bridging the gap</strong> between <strong>strategic IT governance</strong> and <strong>technical execution</strong> by designing a <strong>5-layer Zero Trust framework</strong> specifically to protect <strong>critical ERP systems</strong> and <strong>Access Rights</strong> from <strong>Privilege Escalation</strong> in converged IT/OT aerospace environments.',
        'pub_1_relation': 'This paper is a <strong>direct extraction of the core foundation</strong> established in my Bachelor\'s Thesis. While the thesis comprehensively covers the entire security mitigation program up to the expert validation stage, this paper specifically highlights the <strong>conceptual design phase</strong>. It introduces the <strong>"5-Layer Zero Trust Defense Model"</strong> as a targeted solution to combat specific threats, such as <strong>illegal privilege escalation</strong>, within <strong>Enterprise Resource Planning (ERP)</strong> systems in the aerospace industry.',
        'pub_2_title': 'A Zero Trust Security Architecture for IoT and Cloud: Conceptualizing a Risk Mitigation Program for Digital Twins in the Aerospace Industry',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (The 13th International Conference on ICT for Smart Societies)',
        'pub_2_focus': 'This paper focuses on <strong>adapting the Zero Trust framework</strong> for <strong>machine-to-machine (M2M) interactions</strong> to secure the data flow between physical <strong>IoT Edge Gateways</strong> and <strong>Cloud Digital Twins</strong> against <strong>False Data Injection (FDI)</strong> attacks.',
        'pub_2_relation': 'This paper serves as a <strong>technical extension</strong> of the framework developed in the Bachelor\'s Thesis. While the thesis focuses on broader enterprise security, this paper specifically applies the <strong>"5-Layer Zero Trust Defense Model"</strong> to protect <strong>automated machine-to-machine (M2M) communications</strong> within <strong>IoT and Cloud (Digital Twins)</strong> ecosystems. Validated through <strong>STRIDE Analysis</strong>, the paper proves that the security framework is <strong>highly adaptable</strong>; it is not only robust in securing human access but also analytically proven to prevent <strong>False Data Injection (FDI)</strong> threats on physical factory sensors.',
        'pub_label_conference': 'Conference',
        'pub_label_research_focus': 'Research Focus',
        'pub_label_relation': 'Relation to Bachelor\'s Thesis',
        'pub_label_standards': 'Standards Applied',
        'pub_footer_text': '<strong>Publisher:</strong> IEEE (Institute of Electrical and Electronics Engineers)<br><strong>Indexing:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> Access'
    },
    'id': {
        'menu_publications': 'Publikasi Terkait',
        'pub_section_title': 'Publikasi Terkait',
        'pub_section_subtitle': 'Memperluas Skripsi menjadi Publikasi Internasional IEEE Xplore',
        'pub_section_desc': 'Program Mitigasi Risiko Terintegrasi berbasis Zero Trust Architecture (ZTA), yang dikembangkan dalam Skripsi ini, telah melalui proses peer-review dan diterima untuk publikasi pada dua konferensi internasional. Kedua luaran penelitian ini merinci penerapan spesifik kerangka kerja utama dalam domain operasional kritis dan akan diindeks dalam database IEEE Xplore Digital Library.',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> DITERIMA',
        'pub_1_title': 'Merancang Mitigasi Risiko Siber Terintegrasi Berbasis Zero Trust Architecture: Kerangka Konseptual untuk Industri Kedirgantaraan',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (Konferensi Internasional tentang Kemajuan dalam Ilmu Data, E-learning, dan Sistem Informasi 2026)',
        'pub_1_focus': 'Makalah ini berfokus pada <strong>menjembatani kesenjangan</strong> antara <strong>tata kelola TI strategis</strong> dan <strong>eksekusi teknis</strong> dengan merancang <strong>kerangka Zero Trust 5-lapis</strong> secara khusus untuk melindungi <strong>sistem ERP kritis</strong> dan <strong>Hak Akses</strong> dari <strong>Eskalasi Hak Istimewa</strong> di lingkungan konvergensi IT/OT kedirgantaraan.',
        'pub_1_relation': 'Makalah ini merupakan <strong>ekstraksi langsung dari fondasi inti</strong> yang ditetapkan dalam Skripsi saya. Sementara skripsi secara komprehensif mencakup seluruh program mitigasi keamanan hingga tahap validasi ahli, makalah ini secara khusus menyoroti <strong>fase desain konseptual</strong>. Makalah ini memperkenalkan <strong>"Model Pertahanan Zero Trust 5-Lapis"</strong> sebagai solusi yang ditargetkan untuk memerangi ancaman spesifik, seperti <strong>eskalasi hak istimewa ilegal</strong>, di dalam sistem <strong>Enterprise Resource Planning (ERP)</strong> di industri kedirgantaraan.',
        'pub_2_title': 'Arsitektur Keamanan Zero Trust untuk IoT dan Cloud: Mengonseptualisasikan Program Mitigasi Risiko untuk Digital Twins di Industri Kedirgantaraan',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (Konferensi Internasional ke-13 tentang TIK untuk Masyarakat Cerdas)',
        'pub_2_focus': 'Makalah ini berfokus pada <strong>mengadaptasi kerangka Zero Trust</strong> untuk <strong>interaksi mesin-ke-mesin (M2M)</strong> guna mengamankan aliran data antara <strong>IoT Edge Gateways</strong> fisik dan <strong>Cloud Digital Twins</strong> dari serangan <strong>False Data Injection (FDI)</strong>.',
        'pub_2_relation': 'Makalah ini berfungsi sebagai <strong>ekstensi teknis</strong> dari kerangka kerja yang dikembangkan dalam Skripsi. Walaupun skripsi berfokus pada keamanan perusahaan yang lebih luas, makalah ini secara khusus menerapkan <strong>"Model Pertahanan Zero Trust 5-Lapis"</strong> untuk melindungi <strong>komunikasi mesin-ke-mesin (M2M) otomatis</strong> dalam ekosistem <strong>IoT dan Cloud (Digital Twins)</strong>. Divalidasi melalui <strong>Analisis STRIDE</strong>, makalah ini membuktikan bahwa kerangka keamanan tersebut <strong>sangat dapat diadaptasi</strong>; tidak hanya kuat dalam mengamankan akses manusia tetapi juga terbukti secara analitis untuk mencegah ancaman <strong>False Data Injection (FDI)</strong> pada sensor pabrik fisik.',
        'pub_label_conference': 'Konferensi',
        'pub_label_research_focus': 'Fokus Penelitian',
        'pub_label_relation': 'Hubungan dengan Skripsi',
        'pub_label_standards': 'Standar yang Diterapkan',
        'pub_footer_text': '<strong>Penerbit:</strong> IEEE (Institute of Electrical and Electronics Engineers)<br><strong>Pengindeksan:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> Akses'
    },
    'es': {
        'menu_publications': 'Publicaciones Relacionadas',
        'pub_section_title': 'Publicaciones Relacionadas',
        'pub_section_subtitle': 'Ampliación de la Tesis de Grado en Publicaciones Internacionales de IEEE Xplore',
        'pub_section_desc': 'El Programa Integrado de Mitigación de Riesgos basado en la Arquitectura de Confianza Cero (ZTA), desarrollado en esta Tesis de Grado, ha sido sometido a un proceso de revisión por pares y aceptado para su publicación en dos conferencias internacionales. Estos dos resultados de investigación detallan la aplicación específica del marco principal dentro de dominios operativos críticos y serán indexados en la base de datos de la Biblioteca Digital IEEE Xplore.',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> ACEPTADO',
        'pub_1_title': 'Diseño de una Mitigación Integrada de Riesgos Cibernéticos Basada en la Arquitectura de Confianza Cero: Un Marco Conceptual para la Industria Aeroespacial',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (Conferencia Internacional 2026 sobre el Avance en la Ciencia de Datos, E-learning y Sistemas de Información)',
        'pub_1_focus': 'Este documento se centra en <strong>cerrar la brecha</strong> entre la <strong>gobernanza estratégica de TI</strong> y la <strong>ejecución técnica</strong> mediante el diseño de un <strong>marco de Confianza Cero de 5 capas</strong> específicamente para proteger <strong>sistemas ERP críticos</strong> y <strong>Derechos de Acceso</strong> frente a la <strong>Escalada de Privilegios</strong> en entornos aeroespaciales convergentes TI/TO.',
        'pub_1_relation': 'Este documento es una <strong>extracción directa de la base fundamental</strong> establecida en mi Tesis de Grado. Si bien la tesis cubre de manera exhaustiva todo el programa de mitigación de seguridad hasta la etapa de validación por expertos, este documento destaca específicamente la <strong>fase de diseño conceptual</strong>. Introduce el <strong>"Modelo de Defensa de Confianza Cero de 5 Capas"</strong> como una solución específica para combatir amenazas particulares, como la <strong>escalada ilegal de privilegios</strong>, dentro de los sistemas de <strong>Planificación de Recursos Empresariales (ERP)</strong> en la industria aeroespacial.',
        'pub_2_title': 'Una Arquitectura de Seguridad de Confianza Cero para IoT y la Nube: Conceptualizando un Programa de Mitigación de Riesgos para Gemelos Digitales en la Industria Aeroespacial',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (La 13ª Conferencia Internacional sobre TIC para Sociedades Inteligentes)',
        'pub_2_focus': 'Este documento se centra en <strong>adaptar el marco de Confianza Cero</strong> para <strong>interacciones máquina a máquina (M2M)</strong> para asegurar el flujo de datos entre los <strong>Gateways Perimetrales IoT</strong> físicos y los <strong>Gemelos Digitales en la Nube</strong> frente a ataques de <strong>Inyección de Datos Falsos (FDI)</strong>.',
        'pub_2_relation': 'Este documento sirve como una <strong>extensión técnica</strong> del marco desarrollado en la Tesis de Grado. Si bien la tesis se centra en una seguridad empresarial más amplia, este documento aplica específicamente el <strong>"Modelo de Defensa de Confianza Cero de 5 Capas"</strong> para proteger las <strong>comunicaciones automatizadas máquina a máquina (M2M)</strong> dentro de los ecosistemas de <strong>IoT y la Nube (Gemelos Digitales)</strong>. Validado mediante el <strong>Análisis STRIDE</strong>, el documento demuestra que el marco de seguridad es <strong>altamente adaptable</strong>; no solo es robusto para asegurar el acceso humano, sino que también está analíticamente probado para prevenir amenazas de <strong>Inyección de Datos Falsos (FDI)</strong> en sensores de fábricas físicas.',
        'pub_label_conference': 'Conferencia',
        'pub_label_research_focus': 'Enfoque de Investigación',
        'pub_label_relation': 'Relación con la Tesis',
        'pub_label_standards': 'Estándares Aplicados',
        'pub_footer_text': '<strong>Editor:</strong> IEEE (Instituto de Ingenieros Eléctricos y Electrónicos)<br><strong>Indexación:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> Acceder'
    },
    'fr': {
        'menu_publications': 'Publications Connexes',
        'pub_section_title': 'Publications Connexes',
        'pub_section_subtitle': 'Extension de la Thèse de Licence en Publications Internationales IEEE Xplore',
        'pub_section_desc': 'Le Programme Intégré d\'Atténuation des Risques basé sur la Zero Trust Architecture (ZTA), développé dans cette Thèse de Licence, a fait l\'objet d\'un processus d\'évaluation par les pairs et a été accepté pour publication lors de deux conférences internationales. Ces deux résultats de recherche détaillent l\'application spécifique du cadre principal au sein de domaines opérationnels critiques et seront indexés dans la base de données de la Bibliothèque Numérique IEEE Xplore.',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> ACCEPTÉ',
        'pub_1_title': 'Conception d\'une Atténuation Intégrée des Risques Cybernétiques Basée sur la Zero Trust Architecture : Un Cadre Conceptuel pour l\'Industrie Aérospatiale',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (Conférence Internationale 2026 sur l\'Avancement de la Science des Données, du E-learning et des Systèmes d\'Information)',
        'pub_1_focus': 'Cet article se concentre sur la <strong>réduction de l\'écart</strong> entre la <strong>gouvernance informatique stratégique</strong> et l\'<strong>exécution technique</strong> en concevant un <strong>cadre Zero Trust à 5 couches</strong> spécifiquement pour protéger les <strong>systèmes ERP critiques</strong> et les <strong>Droits d\'Accès</strong> contre l\'<strong>Élévation de Privilèges</strong> dans les environnements aérospatiaux convergents IT/OT.',
        'pub_1_relation': 'Cet article est une <strong>extraction directe de la base fondamentale</strong> établie dans ma Thèse de Licence. Alors que la thèse couvre de manière exhaustive l\'ensemble du programme d\'atténuation de la sécurité jusqu\'à l\'étape de validation par les experts, cet article met spécifiquement en évidence la <strong>phase de conception conceptuelle</strong>. Il introduit le <strong>"Modèle de Défense Zero Trust à 5 Couches"</strong> comme une solution ciblée pour combattre des menaces spécifiques, telles que l\'<strong>élévation illégale de privilèges</strong>, au sein des systèmes de <strong>Planification des Ressources d\'Entreprise (ERP)</strong> dans l\'industrie aérospatiale.',
        'pub_2_title': 'Une Architecture de Sécurité Zero Trust pour l\'IoT et le Cloud : Conceptualisation d\'un Programme d\'Atténuation des Risques pour les Jumeaux Numériques dans l\'Industrie Aérospatiale',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (La 13ème Conférence Internationale sur les TIC pour les Sociétés Intelligentes)',
        'pub_2_focus': 'Cet article se concentre sur l\'<strong>adaptation du cadre Zero Trust</strong> pour les <strong>interactions machine-à-machine (M2M)</strong> afin de sécuriser le flux de données entre les <strong>Passerelles Edge IoT</strong> physiques et les <strong>Jumeaux Numériques Cloud</strong> contre les attaques par <strong>Injection de Fausses Données (FDI)</strong>.',
        'pub_2_relation': 'Cet article sert d\'<strong>extension technique</strong> du cadre développé dans la Thèse de Licence. Alors que la thèse se concentre sur la sécurité globale de l\'entreprise, cet article applique spécifiquement le <strong>"Modèle de Défense Zero Trust à 5 Couches"</strong> pour protéger les <strong>communications automatisées machine-à-machine (M2M)</strong> au sein des écosystèmes <strong>IoT et Cloud (Jumeaux Numériques)</strong>. Validé grâce à l\'<strong>Analyse STRIDE</strong>, l\'article prouve que le cadre de sécurité est <strong>hautement adaptable</strong> ; il est non seulement robuste pour sécuriser l\'accès humain, mais également prouvé de manière analytique pour prévenir les menaces par <strong>Injection de Fausses Données (FDI)</strong> sur les capteurs d\'usine physiques.',
        'pub_label_conference': 'Conférence',
        'pub_label_research_focus': 'Axe de Recherche',
        'pub_label_relation': 'Relation avec la Thèse',
        'pub_label_standards': 'Normes Appliquées',
        'pub_footer_text': '<strong>Éditeur:</strong> IEEE (Institut des Ingénieurs Électriciens et Électroniciens)<br><strong>Indexation:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> Accéder'
    },
    'de': {
        'menu_publications': 'Zugehörige Publikationen',
        'pub_section_title': 'Zugehörige Publikationen',
        'pub_section_subtitle': 'Erweiterung der Bachelorarbeit in internationale IEEE Xplore-Publikationen',
        'pub_section_desc': 'Das in dieser Bachelorarbeit entwickelte Integrierte Risikominderungsprogramm auf Basis der Zero Trust Architecture (ZTA) wurde einem Peer-Review-Verfahren unterzogen und zur Veröffentlichung auf zwei internationalen Konferenzen angenommen. Diese beiden Forschungsergebnisse beschreiben die spezifische Anwendung des Hauptrahmens innerhalb kritischer operativer Bereiche und werden in der IEEE Xplore Digital Library-Datenbank indiziert.',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> AKZEPTIERT',
        'pub_1_title': 'Entwurf einer integrierten Cyber-Risikominderung basierend auf der Zero Trust Architecture: Ein konzeptioneller Rahmen für die Luft- und Raumfahrtindustrie',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (Die Internationale Konferenz 2026 über Fortschritte in Datenwissenschaft, E-Learning und Informationssystemen)',
        'pub_1_focus': 'Dieses Papier konzentriert sich auf die <strong>Überbrückung der Lücke</strong> zwischen <strong>strategischer IT-Governance</strong> und <strong>technischer Ausführung</strong> durch den Entwurf eines <strong>5-Schichten-Zero-Trust-Rahmens</strong>, der speziell darauf ausgelegt ist, <strong>kritische ERP-Systeme</strong> und <strong>Zugriffsrechte</strong> vor <strong>Privilegien-Eskalation</strong> in konvergierten IT/OT-Umgebungen der Luft- und Raumfahrt zu schützen.',
        'pub_1_relation': 'Dieses Papier ist eine <strong>direkte Extraktion der Kerngrundlage</strong>, die in meiner Bachelorarbeit etabliert wurde. Während die Arbeit das gesamte Sicherheitsminderungsprogramm bis zur Expertenvalidierungsphase umfassend abdeckt, hebt dieses Papier speziell die <strong>konzeptionelle Designphase</strong> hervor. Es führt das <strong>"5-Schichten-Zero-Trust-Verteidigungsmodell"</strong> als zielgerichtete Lösung zur Bekämpfung spezifischer Bedrohungen, wie z. B. der <strong>illegalen Privilegien-Eskalation</strong>, innerhalb von <strong>Enterprise Resource Planning (ERP)</strong>-Systemen in der Luft- und Raumfahrtindustrie ein.',
        'pub_2_title': 'Eine Zero-Trust-Sicherheitsarchitektur für IoT und Cloud: Konzeptualisierung eines Risikominderungsprogramms für digitale Zwillinge in der Luft- und Raumfahrtindustrie',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (Die 13. Internationale Konferenz über IKT für smarte Gesellschaften)',
        'pub_2_focus': 'Dieses Papier konzentriert sich auf die <strong>Anpassung des Zero-Trust-Rahmens</strong> für <strong>Maschine-zu-Maschine (M2M)-Interaktionen</strong>, um den Datenfluss zwischen physischen <strong>IoT Edge Gateways</strong> und <strong>Cloud Digital Twins</strong> vor <strong>False Data Injection (FDI)</strong>-Angriffen zu schützen.',
        'pub_2_relation': 'Dieses Papier dient als <strong>technische Erweiterung</strong> des in der Bachelorarbeit entwickelten Rahmens. Während sich die Arbeit auf umfassendere Unternehmenssicherheit konzentriert, wendet dieses Papier spezifisch das <strong>"5-Schichten-Zero-Trust-Verteidigungsmodell"</strong> an, um <strong>automatisierte Maschine-zu-Maschine (M2M)-Kommunikation</strong> in <strong>IoT- und Cloud- (Digital Twins)</strong> Ökosystemen zu schützen. Validiert durch eine <strong>STRIDE-Analyse</strong> beweist das Papier, dass der Sicherheitsrahmen <strong>hochgradig anpassbar</strong> ist; Er ist nicht nur robust bei der Sicherung des menschlichen Zugriffs, sondern schützt analytisch erwiesen auch vor <strong>False Data Injection (FDI)</strong>-Bedrohungen für physische Fabriksensoren.',
        'pub_label_conference': 'Konferenz',
        'pub_label_research_focus': 'Forschungsschwerpunkt',
        'pub_label_relation': 'Bezug zur Bachelorarbeit',
        'pub_label_standards': 'Angewandte Standards',
        'pub_footer_text': '<strong>Herausgeber:</strong> IEEE (Institut der Elektro- und Elektronikingenieure)<br><strong>Indizierung:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> Zugriff'
    },
    'zh': {
        'menu_publications': '相关出版物',
        'pub_section_title': '相关出版物',
        'pub_section_subtitle': '将学士论文扩展到国际 IEEE Xplore 出版物中',
        'pub_section_desc': '本学士论文中制定的基于零信任架构（ZTA）的综合风险缓解计划已通过同行评审程序，并被两个国际会议接受发表。这两项研究成果详细说明了主要框架在关键业务领域的具体应用，并将被编入 IEEE Xplore 数字图书馆数据库。',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> 已接受',
        'pub_1_title': '基于零信任架构设计综合网络风险缓解计划：航空航天业的概念框架',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (2026年数据科学、电子学习和信息系统进步国际会议)',
        'pub_1_focus': '本文侧重于通过设计一个 <strong>5层零信任框架</strong> 来 <strong>弥合战略IT治理</strong> 和 <strong>技术执行</strong> 之间的差距，专门用于保护融合的IT/OT航空航天环境中的 <strong>关键ERP系统</strong> 和 <strong>访问权限</strong> 免受 <strong>特权提升</strong> 的影响。',
        'pub_1_relation': '本文是我的学士论文中建立的 <strong>核心基础的直接提取</strong>。虽然论文全面涵盖了直到专家验证阶段的整个安全缓解计划，但本文特别强调了 <strong>概念设计阶段</strong>。它引入了 <strong>"5层零信任防御模型"</strong>，作为在航空航天业的 <strong>企业资源规划 (ERP)</strong> 系统中应对特定威胁（如 <strong>非法特权提升</strong>）的针对性解决方案。',
        'pub_2_title': '物联网和云的零信任安全架构：航空航天业数字孪生风险缓解计划的概念化',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (第13届智慧社会信息通信技术国际会议)',
        'pub_2_focus': '本文重点关注 <strong>使零信任框架适应</strong> <strong>机器对机器 (M2M) 交互</strong>，以保护物理 <strong>物联网边缘网关</strong> 和 <strong>云数字孪生</strong> 之间的数据流免受 <strong>虚假数据注入 (FDI)</strong> 攻击。',
        'pub_2_relation': '本文是学士论文中开发的框架的 <strong>技术延伸</strong>。论文侧重于更广泛的企业安全，而本文具体应用了 <strong>"5层零信任防御模型"</strong>，以保护 <strong>物联网和云（数字孪生）</strong> 生态系统中的 <strong>自动化机器对机器 (M2M) 通信</strong>。通过 <strong>STRIDE分析</strong> 验证，论文证明了安全框架 <strong>具有高度的适应性</strong>；它不仅在保护人类访问方面很稳健，而且通过分析证明可以防止对物理工厂传感器的 <strong>虚假数据注入 (FDI)</strong> 威胁。',
        'pub_label_conference': '会议',
        'pub_label_research_focus': '研究重点',
        'pub_label_relation': '与论文的关系',
        'pub_label_standards': '应用标准',
        'pub_footer_text': '<strong>出版商:</strong> IEEE (电气和电子工程师协会)<br><strong>索引:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> 访问'
    },
    'ja': {
        'menu_publications': '関連出版物',
        'pub_section_title': '関連出版物',
        'pub_section_subtitle': '学士論文から国際的なIEEE Xplore出版物への拡張',
        'pub_section_desc': 'この学士論文で開発されたゼロトラストアーキテクチャ（ZTA）に基づく統合リスク軽減プログラムは、査読プロセスを経て、2つの国際会議での発表が承認されました。これら2つの研究成果は、重要な運用ドメイン内での主要なフレームワークの具体的な適用を詳述しており、IEEE Xploreデジタルライブラリデータベースにインデックス付けされます。',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> 受理済み',
        'pub_1_title': 'ゼロトラストアーキテクチャに基づく統合サイバーリスク軽減の設計：航空宇宙産業のための概念フレームワーク',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (2026年データサイエンス、eラーニング、および情報システムの進歩に関する国際会議)',
        'pub_1_focus': 'この論文は、統合されたIT/OT航空宇宙環境において、<strong>特権の昇格</strong>から<strong>重要なERPシステム</strong>と<strong>アクセス権</strong>を保護するために特別に<strong>5層ゼロトラストフレームワーク</strong>を設計することにより、<strong>戦略的ITガバナンス</strong>と<strong>技術的実行</strong>の間の<strong>ギャップを埋める</strong>ことに焦点を当てています。',
        'pub_1_relation': 'この論文は、私の学士論文で確立された<strong>コア基盤の直接的な抽出</strong>です。論文は専門家による検証段階までのセキュリティ緩和プログラム全体を包括的にカバーしていますが、この論文は特に<strong>概念設計フェーズ</strong>を強調しています。航空宇宙産業の<strong>エンタープライズリソースプランニング（ERP）</strong>システム内における<strong>違法な特権の昇格</strong>などの特定の脅威と戦うためのターゲットソリューションとして、<strong>「5層ゼロトラスト防御モデル」</strong>を導入しています。',
        'pub_2_title': 'IoTとクラウドのためのゼロトラストセキュリティアーキテクチャ：航空宇宙産業におけるデジタルツインのリスク軽減プログラムの概念化',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (第13回スマート社会のためのICTに関する国際会議)',
        'pub_2_focus': 'この論文は、物理的な<strong>IoTエッジゲートウェイ</strong>と<strong>クラウドデジタルツイン</strong>間のデータフローを<strong>虚偽データ注入（FDI）</strong>攻撃から保護するために、<strong>マシンツーマシン（M2M）インタラクション</strong>のための<strong>ゼロトラストフレームワークの適応</strong>に焦点を当てています。',
        'pub_2_relation': 'この論文は、学士論文で開発されたフレームワークの<strong>技術的拡張</strong>として機能します。論文はより広範なエンタープライズセキュリティに焦点を当てていますが、この論文は特に<strong>「5層ゼロトラスト防御モデル」</strong>を適用して、<strong>IoTおよびクラウド（デジタルツイン）</strong>エコシステム内の<strong>自動化されたマシンツーマシン（M2M）通信</strong>を保護します。<strong>STRIDE分析</strong>によって検証されたこの論文は、セキュリティフレームワークが<strong>高度に適応可能</strong>であることを証明しています。人間のアクセスを保護する上で堅牢であるだけでなく、物理的な工場センサーに対する<strong>虚偽データ注入（FDI）</strong>の脅威を防ぐことが分析的に証明されています。',
        'pub_label_conference': '会議',
        'pub_label_research_focus': '研究の焦点',
        'pub_label_relation': '論文との関係',
        'pub_label_standards': '適用される基準',
        'pub_footer_text': '<strong>出版社:</strong> IEEE (米国電気電子学会)<br><strong>インデックス:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> アクセス'
    },
    'ko': {
        'menu_publications': '관련 간행물',
        'pub_section_title': '관련 간행물',
        'pub_section_subtitle': '학사 논문을 국제 IEEE Xplore 간행물로 확장',
        'pub_section_desc': '이 학사 논문에서 개발된 제로 트러스트 아키텍처(ZTA) 기반의 통합 위험 완화 프로그램은 동료 검토(peer-review) 과정을 거쳐 두 개의 국제 회의에서 발표되도록 승인되었습니다. 이 두 가지 연구 결과는 중요한 운영 도메인 내에서 주요 프레임워크의 특정 적용을 자세히 설명하며 IEEE Xplore 디지털 라이브러리 데이터베이스에 색인화됩니다.',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> 승인됨',
        'pub_1_title': '제로 트러스트 아키텍처를 기반으로 한 통합 사이버 위험 완화 설계: 항공 우주 산업을 위한 개념적 프레임워크',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (2026년 데이터 과학, E-러닝 및 정보 시스템 발전에 관한 국제 회의)',
        'pub_1_focus': '이 논문은 융합된 IT/OT 항공 우주 환경에서 <strong>권한 상승</strong>으로부터 <strong>중요한 ERP 시스템</strong> 및 <strong>액세스 권한</strong>을 보호하기 위해 특별히 <strong>5계층 제로 트러스트 프레임워크</strong>를 설계함으로써 <strong>전략적 IT 거버넌스</strong>와 <strong>기술적 실행</strong> 사이의 <strong>격차를 해소</strong>하는 데 중점을 둡니다.',
        'pub_1_relation': '이 논문은 제 학사 논문에서 설정된 <strong>핵심 기반을 직접 추출</strong>한 것입니다. 논문은 전문가 검증 단계까지의 전체 보안 완화 프로그램을 포괄적으로 다루지만, 이 논문은 특별히 <strong>개념적 설계 단계</strong>를 강조합니다. 항공 우주 산업의 <strong>전사적 자원 관리(ERP)</strong> 시스템 내에서 <strong>불법적인 권한 상승</strong>과 같은 특정 위협에 맞서기 위한 표적 솔루션으로 <strong>"5계층 제로 트러스트 방어 모델"</strong>을 소개합니다.',
        'pub_2_title': 'IoT 및 클라우드를 위한 제로 트러스트 보안 아키텍처: 항공 우주 산업의 디지털 트윈을 위한 위험 완화 프로그램 개념화',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (제13회 스마트 사회를 위한 ICT에 관한 국제 회의)',
        'pub_2_focus': '이 논문은 물리적 <strong>IoT 에지 게이트웨이</strong>와 <strong>클라우드 디지털 트윈</strong> 간의 데이터 흐름을 <strong>FDI(False Data Injection)</strong> 공격으로부터 보호하기 위해 <strong>머신 투 머신(M2M) 상호 작용</strong>을 위한 <strong>제로 트러스트 프레임워크를 적용</strong>하는 데 중점을 둡니다.',
        'pub_2_relation': '이 논문은 학사 논문에서 개발된 프레임워크의 <strong>기술적 확장</strong> 역할을 합니다. 논문은 광범위한 엔터프라이즈 보안에 중점을 두는 반면, 이 논문은 특별히 <strong>"5계층 제로 트러스트 방어 모델"</strong>을 적용하여 <strong>IoT 및 클라우드(디지털 트윈)</strong> 에코시스템 내에서 <strong>자동화된 머신 투 머신(M2M) 통신</strong>을 보호합니다. <strong>STRIDE 분석</strong>을 통해 검증된 이 논문은 보안 프레임워크가 <strong>적응성이 뛰어남</strong>을 증명합니다. 인간의 액세스를 보호하는 데 강력할 뿐만 아니라 물리적 공장 센서에 대한 <strong>FDI(False Data Injection)</strong> 위협을 방지하는 것으로 분석적으로 입증되었습니다.',
        'pub_label_conference': '회의',
        'pub_label_research_focus': '연구 초점',
        'pub_label_relation': '논문과의 관계',
        'pub_label_standards': '적용된 기준',
        'pub_footer_text': '<strong>출판사:</strong> IEEE (전기 전자 기술자 협회)<br><strong>색인:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> 액세스'
    },
    'ar': {
        'menu_publications': 'المنشورات ذات الصلة',
        'pub_section_title': 'المنشورات ذات الصلة',
        'pub_section_subtitle': 'توسيع أطروحة البكالوريوس إلى منشورات IEEE Xplore الدولية',
        'pub_section_desc': 'خضع برنامج التخفيف المتكامل للمخاطر القائم على هندسة انعدام الثقة (ZTA)، والذي تم تطويره في أطروحة البكالوريوس هذه، لعملية مراجعة الأقران وتم قبوله للنشر في مؤتمرين دوليين. تفصل هاتان المخرجات البحثية التطبيق المحدد للإطار الرئيسي ضمن المجالات التشغيلية الحرجة وسيتم فهرستها في قاعدة بيانات مكتبة IEEE Xplore الرقمية.',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> مقبولة',
        'pub_1_title': 'تصميم تخفيف متكامل للمخاطر السيبرانية بناءً على هندسة انعدام الثقة: إطار مفاهيمي لصناعة الطيران',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (المؤتمر الدولي لعام 2026 حول التقدم في علوم البيانات والتعلم الإلكتروني ونظم المعلومات)',
        'pub_1_focus': 'يركز هذا البحث على <strong>سد الفجوة</strong> بين <strong>حوكمة تكنولوجيا المعلومات الاستراتيجية</strong> و <strong>التنفيذ التقني</strong> من خلال تصميم <strong>إطار انعدام ثقة مكون من 5 طبقات</strong> خصيصًا لحماية <strong>أنظمة ERP الحرجة</strong> و <strong>حقوق الوصول</strong> من <strong>تصعيد الامتيازات</strong> في بيئات الطيران المتقاربة IT/OT.',
        'pub_1_relation': 'هذا البحث هو <strong>استخراج مباشر للأساس الجوهري</strong> الذي تم إنشاؤه في أطروحة البكالوريوس الخاصة بي. بينما تغطي الأطروحة بشكل شامل برنامج التخفيف الأمني بأكمله حتى مرحلة التحقق من صحة الخبراء، يسلط هذا البحث الضوء بشكل خاص على <strong>مرحلة التصميم المفاهيمي</strong>. يقدم <strong>"نموذج دفاع انعدام الثقة المكون من 5 طبقات"</strong> كحل مستهدف لمكافحة تهديدات محددة، مثل <strong>تصعيد الامتيازات غير القانوني</strong>، داخل أنظمة <strong>تخطيط موارد المؤسسات (ERP)</strong> في صناعة الطيران.',
        'pub_2_title': 'هندسة أمان انعدام الثقة لإنترنت الأشياء والسحابة: وضع تصور لبرنامج تخفيف المخاطر للتوائم الرقمية في صناعة الطيران',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (المؤتمر الدولي الثالث عشر حول تكنولوجيا المعلومات والاتصالات من أجل مجتمعات ذكية)',
        'pub_2_focus': 'يركز هذا البحث على <strong>تكييف إطار انعدام الثقة</strong> لـ <strong>تفاعلات الآلة إلى الآلة (M2M)</strong> لتأمين تدفق البيانات بين <strong>بوابات حافة إنترنت الأشياء (IoT Edge)</strong> المادية و <strong>التوائم الرقمية السحابية</strong> ضد هجمات <strong>حقن البيانات الخاطئة (FDI)</strong>.',
        'pub_2_relation': 'يعمل هذا البحث بمثابة <strong>امتداد تقني</strong> للإطار الذي تم تطويره في أطروحة البكالوريوس. بينما تركز الأطروحة على أمن المؤسسة على نطاق أوسع، يطبق هذا البحث على وجه التحديد <strong>"نموذج دفاع انعدام الثقة المكون من 5 طبقات"</strong> لحماية <strong>اتصالات الآلة إلى الآلة (M2M) الآلية</strong> داخل النظم البيئية لـ <strong>إنترنت الأشياء والسحابة (التوائم الرقمية)</strong>. تم التحقق من صحته من خلال <strong>تحليل STRIDE</strong>، ويثبت البحث أن الإطار الأمني <strong>قابل للتكيف بدرجة كبيرة</strong>؛ فهو ليس قويًا فقط في تأمين وصول الإنسان ولكنه أثبت تحليليًا أنه يمنع تهديدات <strong>حقن البيانات الخاطئة (FDI)</strong> على مستشعرات المصنع المادية.',
        'pub_label_conference': 'المؤتمر',
        'pub_label_research_focus': 'محور البحث',
        'pub_label_relation': 'العلاقة بالأطروحة',
        'pub_label_standards': 'المعايير المطبقة',
        'pub_footer_text': '<strong>الناشر:</strong> IEEE (معهد مهندسي الكهرباء والإلكترونيات)<br><strong>الفهرسة:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> وصول'
    },
    'ru': {
        'menu_publications': 'Связанные Публикации',
        'pub_section_title': 'Связанные Публикации',
        'pub_section_subtitle': 'Расширение дипломной работы в международные публикации IEEE Xplore',
        'pub_section_desc': 'Интегрированная программа снижения рисков, основанная на архитектуре нулевого доверия (ZTA), разработанная в этой дипломной работе, прошла процесс рецензирования и была принята к публикации на двух международных конференциях. Эти два результата исследований детализируют конкретное применение основной структуры в критически важных операционных областях и будут проиндексированы в базе данных цифровой библиотеки IEEE Xplore.',
        'pub_badge_accepted': '<i class="ph-fill ph-check-circle"></i> ПРИНЯТО',
        'pub_1_title': 'Разработка интегрированной системы снижения киберрисков на основе архитектуры нулевого доверия: концептуальная основа для аэрокосмической отрасли',
        'pub_1_conf': '<a href="https://icadeis.org/index.php" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICADEIS 2026</strong></a> (Международная конференция 2026 года по достижениям в области науки о данных, электронного обучения и информационных систем)',
        'pub_1_focus': 'Эта статья фокусируется на <strong>преодолении разрыва</strong> между <strong>стратегическим ИТ-управлением</strong> и <strong>техническим исполнением</strong> путем разработки <strong>5-уровневой структуры нулевого доверия</strong>, специально предназначенной для защиты <strong>критических ERP-систем</strong> и <strong>прав доступа</strong> от <strong>эскалации привилегий</strong> в конвергентных ИТ/ОТ-средах аэрокосмической отрасли.',
        'pub_1_relation': 'Эта статья является <strong>прямым извлечением основы</strong>, установленной в моей дипломной работе. Хотя диссертация всесторонне охватывает всю программу снижения рисков безопасности вплоть до стадии экспертной оценки, в этой статье особо выделяется <strong>фаза концептуального проектирования</strong>. В ней представлена <strong>«5-уровневая модель защиты с нулевым доверием»</strong> как целевое решение для борьбы с конкретными угрозами, такими как <strong>незаконное повышение привилегий</strong>, в системах <strong>планирования ресурсов предприятия (ERP)</strong> в аэрокосмической отрасли.',
        'pub_2_title': 'Архитектура безопасности с нулевым доверием для IoT и облака: концептуализация программы снижения рисков для цифровых двойников в аэрокосмической отрасли',
        'pub_2_conf': '<a href="https://iciss.goesmart.id/" target="_blank" style="color: #00629B; text-decoration: underline;"><strong>ICISS 2026</strong></a> (13-я Международная конференция по ИКТ для умных обществ)',
        'pub_2_focus': 'Эта статья фокусируется на <strong>адаптации структуры нулевого доверия</strong> для <strong>межмашинного (M2M) взаимодействия</strong> с целью защиты потока данных между физическими <strong>пограничными шлюзами IoT</strong> и <strong>облачными цифровыми двойниками</strong> от атак <strong>внедрения ложных данных (FDI)</strong>.',
        'pub_2_relation': 'Эта статья служит <strong>техническим расширением</strong> структуры, разработанной в дипломной работе. В то время как диссертация фокусируется на более широкой корпоративной безопасности, в этой статье специально применяется <strong>«5-уровневая модель защиты с нулевым доверием»</strong> для защиты <strong>автоматизированных межмашинных (M2M) коммуникаций</strong> в экосистемах <strong>IoT и облака (цифровых двойников)</strong>. Подтвержденная посредством <strong>анализа STRIDE</strong>, статья доказывает, что система безопасности <strong>в высокой степени адаптируема</strong>; она не только надежна в обеспечении доступа людей, но и аналитически доказано, что она предотвращает угрозы <strong>внедрения ложных данных (FDI)</strong> на физических заводских датчиках.',
        'pub_label_conference': 'Конференция',
        'pub_label_research_focus': 'Фокус Исследований',
        'pub_label_relation': 'Связь с Дипломной Работой',
        'pub_label_standards': 'Применяемые Стандарты',
        'pub_footer_text': '<strong>Издатель:</strong> IEEE (Институт инженеров по электротехнике и радиоэлектронике)<br><strong>Индексация:</strong> Scopus / IEEE Xplore',
        'pub_btn_access': '<i class="ph-bold ph-arrow-square-out"></i> Доступ'
    }
}

for lang, trans_dict in translations.items():
    entries_str = ""
    for k, v in trans_dict.items():
        val = v.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", " ")
        entries_str += f'          "{k}": "{val}",\n'
    
    # Inject into content right after the language key
    pattern = r'(' + lang + r':\s*\{)'
    replacement = r'\1\n' + entries_str
    content = re.sub(pattern, replacement, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done publications translations")
