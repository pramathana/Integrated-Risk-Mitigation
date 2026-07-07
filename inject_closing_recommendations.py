import re
import json

file_path = "c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. Regex replacements to add data-i18n attributes ---

regex_replacements = [
    # Conclusion Item 5
    (r'<div class="closing-item-title">\s*Empirical Validation & Consensus\s*</div>', '<div class="closing-item-title" data-i18n="closing_item_5_title">Empirical Validation & Consensus</div>'),
    (r'<div class="closing-item-desc">\s*The <strong>Final Integrated Risk Mitigation Program</strong>.*?aerospace\s*industry\.</div>', '<div class="closing-item-desc" data-i18n="closing_item_5_desc">The <strong>Final Integrated Risk Mitigation Program</strong> has been enhanced through empirical validation by <strong>9 industry experts and academics</strong>, proving the relevance of the artifacts to the final results: <strong>7 out of 11 threats</strong> were rated "Highly Relevant" and <strong>4 out of 11 threats</strong> were rated "Relevant," and a unanimous consensus (100%) was reached during the Participant Validation phase. This can serve as a blueprint for cybersecurity that precisely aligns strategic risk management gaps with the execution of tactical security controls based on the <strong>Zero Trust Architecture principle</strong> in the aerospace industry.</div>'),
    
    # Recommendation Title & Badge
    (r'<h2 class="closing-title">\s*[^<]*Recommendation\s*</h2>', '<h2 class="closing-title" data-i18n="closing_rec_title">💡 Recommendation</h2>'),
    (r'<span class="closing-badge">\s*Strategic Next Steps\s*</span>', '<span class="closing-badge" data-i18n="closing_rec_badge">Strategic Next Steps</span>'),
    
    # Recommendation Item 1
    (r'<div class="closing-item-title">\s*Dynamic HR-IT Integration\s*</div>', '<div class="closing-item-title" data-i18n="closing_rec_1_title">Dynamic HR-IT Integration</div>'),
    (r'<div class="closing-item-desc">\s*<strong>Integrate the reporting system</strong>.*?bureaucratic processes\.\s*</div>', '<div class="closing-item-desc" data-i18n="closing_rec_1_desc"><strong>Integrate the reporting system</strong> for changes in employee status (transfers, retirement, resignation) from the Human Capital (HC) division with the Information Technology (IT) management system. This is to automate the revocation of system access rights in <strong>real time (dynamic policy)</strong> in order to eliminate reliance on slow and high-risk manual bureaucratic processes.</div>'),
    
    # Recommendation Item 2
    (r'<div class="closing-item-title">\s*Institutional MFA Transition\s*</div>', '<div class="closing-item-title" data-i18n="closing_rec_2_title">Institutional MFA Transition</div>'),
    (r'<div class="closing-item-desc">\s*Simulate a phased transition.*?\(SKEP or Decree\)\.</div>', '<div class="closing-item-desc" data-i18n="closing_rec_2_desc">Simulate a phased transition to the use of <strong>MFA at the institutional level</strong>; if well-received, this can become a mandatory policy issued through a formal instrument (SKEP or Decree).</div>'),
    
    # Recommendation Item 3
    (r'<div class="closing-item-title">\s*Mandatory Root Cause Analysis\s*</div>', '<div class="closing-item-title" data-i18n="closing_rec_3_title">Mandatory Root Cause Analysis</div>'),
    (r'<div class="closing-item-desc">\s*Formalize the <strong>root cause analysis process</strong>.*?highest decision-makers\.</div>', '<div class="closing-item-desc" data-i18n="closing_rec_3_desc">Formalize the <strong>root cause analysis process</strong> as a mandatory post-incident procedure by ensuring that the board of directors and senior management are actively involved in <strong>periodic risk oversight</strong>. Currently, APO12.06 Level 5 is rated zero because root causes are not escalated to the highest decision-makers.</div>'),
    
    # Recommendation Item 4
    (r'<div class="closing-item-title">\s*Stricter Intranet Governance\s*</div>', '<div class="closing-item-title" data-i18n="closing_rec_4_title">Stricter Intranet Governance</div>'),
    (r'<div class="closing-item-desc">\s*Establish a formal policy.*?reputation from damage\.</div>', '<div class="closing-item-desc" data-i18n="closing_rec_4_desc">Establish a formal policy regarding stricter <strong>restrictions on the use of the Intranet</strong>. This aims to protect the company\'s IP reputation from damage.</div>'),
    
    # Recommendation Item 5
    (r'<div class="closing-item-title">\s*Cybersecurity Workforce Training\s*</div>', '<div class="closing-item-title" data-i18n="closing_rec_5_title">Cybersecurity Workforce Training</div>'),
    (r'<div class="closing-item-desc">\s*Invest in cybersecurity workforce.*?implicit trust\.\s*</div>', '<div class="closing-item-desc" data-i18n="closing_rec_5_desc">Invest in cybersecurity workforce competency training through <strong>tiered training programs and specialized IT risk management certifications</strong>. This is crucial to reduce the risk of future information leaks, as internal employees will have a high level of awareness regarding implicit trust.</div>'),
    
    # Recommendation Item 6
    (r'<div class="closing-item-title">\s*DLP & DRM Procurement Priority\s*</div>', '<div class="closing-item-title" data-i18n="closing_rec_6_title">DLP & DRM Procurement Priority</div>'),
    (r'<div class="closing-item-desc">\s*The procurement of <strong>DLP \(Data Leak Prevention\)</strong>.*?physical paper\s*forms\.\s*</div>', '<div class="closing-item-desc" data-i18n="closing_rec_6_desc">The procurement of <strong>DLP (Data Leak Prevention)</strong> and <strong>DRM (Digital Rights Management)</strong> systems should be treated as a <strong>budget priority that cannot be postponed</strong>, as they are one way to replace the bureaucracy of physical paper forms.</div>')
]

for pat, repl in regex_replacements:
    content = re.sub(pat, repl, content, flags=re.DOTALL)

# --- 2. Add translations into the dictionary ---
translations = {
    'en': {
        'closing_item_5_title': 'Empirical Validation & Consensus',
        'closing_item_5_desc': 'The <strong>Final Integrated Risk Mitigation Program</strong> has been enhanced through empirical validation by <strong>9 industry experts and academics</strong>, proving the relevance of the artifacts to the final results: <strong>7 out of 11 threats</strong> were rated "Highly Relevant" and <strong>4 out of 11 threats</strong> were rated "Relevant," and a unanimous consensus (100%) was reached during the Participant Validation phase. This can serve as a blueprint for cybersecurity that precisely aligns strategic risk management gaps with the execution of tactical security controls based on the <strong>Zero Trust Architecture principle</strong> in the aerospace industry.',
        'closing_rec_title': '💡 Recommendation',
        'closing_rec_badge': 'Strategic Next Steps',
        'closing_rec_1_title': 'Dynamic HR-IT Integration',
        'closing_rec_1_desc': '<strong>Integrate the reporting system</strong> for changes in employee status (transfers, retirement, resignation) from the Human Capital (HC) division with the Information Technology (IT) management system. This is to automate the revocation of system access rights in <strong>real time (dynamic policy)</strong> in order to eliminate reliance on slow and high-risk manual bureaucratic processes.',
        'closing_rec_2_title': 'Institutional MFA Transition',
        'closing_rec_2_desc': 'Simulate a phased transition to the use of <strong>MFA at the institutional level</strong>; if well-received, this can become a mandatory policy issued through a formal instrument (SKEP or Decree).',
        'closing_rec_3_title': 'Mandatory Root Cause Analysis',
        'closing_rec_3_desc': 'Formalize the <strong>root cause analysis process</strong> as a mandatory post-incident procedure by ensuring that the board of directors and senior management are actively involved in <strong>periodic risk oversight</strong>. Currently, APO12.06 Level 5 is rated zero because root causes are not escalated to the highest decision-makers.',
        'closing_rec_4_title': 'Stricter Intranet Governance',
        'closing_rec_4_desc': 'Establish a formal policy regarding stricter <strong>restrictions on the use of the Intranet</strong>. This aims to protect the company\'s IP reputation from damage.',
        'closing_rec_5_title': 'Cybersecurity Workforce Training',
        'closing_rec_5_desc': 'Invest in cybersecurity workforce competency training through <strong>tiered training programs and specialized IT risk management certifications</strong>. This is crucial to reduce the risk of future information leaks, as internal employees will have a high level of awareness regarding implicit trust.',
        'closing_rec_6_title': 'DLP & DRM Procurement Priority',
        'closing_rec_6_desc': 'The procurement of <strong>DLP (Data Leak Prevention)</strong> and <strong>DRM (Digital Rights Management)</strong> systems should be treated as a <strong>budget priority that cannot be postponed</strong>, as they are one way to replace the bureaucracy of physical paper forms.'
    },
    'id': {
        'closing_item_5_title': 'Validasi Empiris & Konsensus',
        'closing_item_5_desc': '<strong>Program Mitigasi Risiko Terintegrasi Final</strong> telah ditingkatkan melalui validasi empiris oleh <strong>9 pakar industri dan akademisi</strong>, membuktikan relevansi artefak dengan hasil akhir: <strong>7 dari 11 ancaman</strong> dinilai "Sangat Relevan" dan <strong>4 dari 11 ancaman</strong> dinilai "Relevan", serta konsensus mutlak (100%) dicapai selama fase Validasi Peserta. Ini dapat berfungsi sebagai cetak biru untuk keamanan siber yang secara tepat menyelaraskan kesenjangan manajemen risiko strategis dengan eksekusi kontrol keamanan taktis berdasarkan <strong>prinsip Zero Trust Architecture</strong> di industri kedirgantaraan.',
        'closing_rec_title': '💡 Rekomendasi',
        'closing_rec_badge': 'Langkah Strategis Selanjutnya',
        'closing_rec_1_title': 'Integrasi Dinamis HR-IT',
        'closing_rec_1_desc': '<strong>Integrasikan sistem pelaporan</strong> perubahan status karyawan (mutasi, pensiun, pengunduran diri) dari divisi Human Capital (HC) dengan sistem manajemen Teknologi Informasi (TI). Hal ini untuk mengotomatiskan pencabutan hak akses sistem secara <strong>real time (kebijakan dinamis)</strong> guna menghilangkan ketergantungan pada proses birokrasi manual yang lambat dan berisiko tinggi.',
        'closing_rec_2_title': 'Transisi MFA Institusional',
        'closing_rec_2_desc': 'Simulasikan transisi bertahap penggunaan <strong>MFA di tingkat institusi</strong>; jika diterima dengan baik, hal ini dapat menjadi kebijakan wajib yang dikeluarkan melalui instrumen resmi (SKEP atau Surat Keputusan).',
        'closing_rec_3_title': 'Analisis Akar Masalah Wajib',
        'closing_rec_3_desc': 'Formalkan <strong>proses analisis akar masalah</strong> sebagai prosedur wajib pascainsiden dengan memastikan bahwa dewan direksi dan manajemen senior terlibat aktif dalam <strong>pengawasan risiko berkala</strong>. Saat ini, APO12.06 Level 5 dinilai nol karena akar penyebab tidak dieskalasi ke pengambil keputusan tertinggi.',
        'closing_rec_4_title': 'Tata Kelola Intranet yang Lebih Ketat',
        'closing_rec_4_desc': 'Tetapkan kebijakan formal mengenai <strong>pembatasan yang lebih ketat pada penggunaan Intranet</strong>. Hal ini bertujuan untuk melindungi reputasi IP perusahaan dari kerusakan.',
        'closing_rec_5_title': 'Pelatihan Tenaga Kerja Keamanan Siber',
        'closing_rec_5_desc': 'Investasikan dalam pelatihan kompetensi tenaga kerja keamanan siber melalui <strong>program pelatihan berjenjang dan sertifikasi khusus manajemen risiko TI</strong>. Ini sangat penting untuk mengurangi risiko kebocoran informasi di masa depan, karena karyawan internal akan memiliki tingkat kesadaran yang tinggi mengenai implicit trust.',
        'closing_rec_6_title': 'Prioritas Pengadaan DLP & DRM',
        'closing_rec_6_desc': 'Pengadaan sistem <strong>DLP (Data Leak Prevention)</strong> dan <strong>DRM (Digital Rights Management)</strong> harus diperlakukan sebagai <strong>prioritas anggaran yang tidak dapat ditunda</strong>, karena keduanya merupakan salah satu cara untuk menggantikan birokrasi formulir kertas fisik.'
    },
    'es': {
        'closing_item_5_title': 'Validación Empírica y Consenso',
        'closing_item_5_desc': 'El <strong>Programa Final Integrado de Mitigación de Riesgos</strong> se ha mejorado a través de la validación empírica por parte de <strong>9 expertos de la industria y académicos</strong>, demostrando la relevancia de los artefactos para los resultados finales: <strong>7 de 11 amenazas</strong> fueron calificadas como "Altamente Relevantes" y <strong>4 de 11 amenazas</strong> como "Relevantes", y se alcanzó un consenso unánime (100%) durante la fase de Validación de los Participantes. Esto puede servir como modelo para la ciberseguridad que alinee con precisión las brechas en la gestión de riesgos estratégicos con la ejecución de controles de seguridad tácticos basados en el <strong>principio de Arquitectura de Confianza Cero</strong> en la industria aeroespacial.',
        'closing_rec_title': '💡 Recomendación',
        'closing_rec_badge': 'Próximos Pasos Estratégicos',
        'closing_rec_1_title': 'Integración Dinámica HR-IT',
        'closing_rec_1_desc': '<strong>Integrar el sistema de reportes</strong> para los cambios en el estado de los empleados (traslados, jubilación, renuncia) de la división de Capital Humano (HC) con el sistema de gestión de Tecnología de la Información (TI). Esto es para automatizar la revocación de derechos de acceso al sistema en <strong>tiempo real (política dinámica)</strong> con el fin de eliminar la dependencia de procesos burocráticos manuales lentos y de alto riesgo.',
        'closing_rec_2_title': 'Transición Institucional de MFA',
        'closing_rec_2_desc': 'Simular una transición gradual al uso de <strong>MFA a nivel institucional</strong>; si se recibe bien, esto puede convertirse en una política obligatoria emitida a través de un instrumento formal (SKEP o Decreto).',
        'closing_rec_3_title': 'Análisis Obligatorio de Causa Raíz',
        'closing_rec_3_desc': 'Formalizar el <strong>proceso de análisis de causa raíz</strong> como un procedimiento obligatorio posterior a un incidente asegurando que la junta directiva y la alta gerencia participen activamente en la <strong>supervisión periódica de riesgos</strong>. Actualmente, APO12.06 Nivel 5 se califica con cero porque las causas fundamentales no se escalan a los más altos tomadores de decisiones.',
        'closing_rec_4_title': 'Gobernanza Más Estricta de la Intranet',
        'closing_rec_4_desc': 'Establecer una política formal con respecto a <strong>restricciones más estrictas sobre el uso de la Intranet</strong>. Esto tiene como objetivo proteger la reputación de IP de la empresa contra daños.',
        'closing_rec_5_title': 'Capacitación del Personal de Ciberseguridad',
        'closing_rec_5_desc': 'Invertir en capacitación de competencias para el personal de ciberseguridad a través de <strong>programas de capacitación escalonados y certificaciones especializadas en gestión de riesgos de TI</strong>. Esto es crucial para reducir el riesgo de futuras fugas de información, ya que los empleados internos tendrán un alto nivel de conciencia con respecto a la confianza implícita.',
        'closing_rec_6_title': 'Prioridad de Adquisición de DLP y DRM',
        'closing_rec_6_desc': 'La adquisición de sistemas <strong>DLP (Prevención de Fuga de Datos)</strong> y <strong>DRM (Gestión de Derechos Digitales)</strong> debe tratarse como una <strong>prioridad presupuestaria impostergable</strong>, ya que son una forma de reemplazar la burocracia de los formularios en papel físico.'
    },
    'fr': {
        'closing_item_5_title': 'Validation Empirique & Consensus',
        'closing_item_5_desc': 'Le <strong>Programme Intégré Final d\'Atténuation des Risques</strong> a été amélioré grâce à une validation empirique par <strong>9 experts de l\'industrie et universitaires</strong>, prouvant la pertinence des artefacts par rapport aux résultats finaux : <strong>7 menaces sur 11</strong> ont été jugées "Hautement Pertinentes" et <strong>4 menaces sur 11</strong> ont été jugées "Pertinentes", et un consensus unanime (100%) a été atteint lors de la phase de Validation des Participants. Cela peut servir de modèle pour la cybersécurité qui aligne précisément les lacunes de la gestion des risques stratégiques avec l\'exécution des contrôles de sécurité tactiques basés sur le <strong>principe de la Zero Trust Architecture</strong> dans l\'industrie aérospatiale.',
        'closing_rec_title': '💡 Recommandation',
        'closing_rec_badge': 'Prochaines Étapes Stratégiques',
        'closing_rec_1_title': 'Intégration Dynamique RH-IT',
        'closing_rec_1_desc': '<strong>Intégrer le système de signalement</strong> des changements de statut des employés (mutations, retraite, démission) de la division du Capital Humain (HC) avec le système de gestion des Technologies de l\'Information (IT). Il s\'agit d\'automatiser la révocation des droits d\'accès au système en <strong>temps réel (politique dynamique)</strong> afin d\'éliminer la dépendance aux processus bureaucratiques manuels lents et à haut risque.',
        'closing_rec_2_title': 'Transition Institutionnelle vers la MFA',
        'closing_rec_2_desc': 'Simuler une transition progressive vers l\'utilisation de la <strong>MFA au niveau institutionnel</strong> ; si elle est bien accueillie, cela peut devenir une politique obligatoire émise par le biais d\'un instrument formel (SKEP ou Décret).',
        'closing_rec_3_title': 'Analyse Obligatoire des Causes Profondes',
        'closing_rec_3_desc': 'Formaliser le <strong>processus d\'analyse des causes profondes</strong> en tant que procédure post-incident obligatoire en s\'assurant que le conseil d\'administration et la haute direction sont activement impliqués dans la <strong>surveillance périodique des risques</strong>. Actuellement, APO12.06 Niveau 5 est noté zéro car les causes profondes ne sont pas transmises aux plus hauts décideurs.',
        'closing_rec_4_title': 'Gouvernance Plus Stricte de l\'Intranet',
        'closing_rec_4_desc': 'Établir une politique formelle concernant des <strong>restrictions plus strictes sur l\'utilisation de l\'Intranet</strong>. Cela vise à protéger la réputation de la propriété intellectuelle de l\'entreprise contre les dommages.',
        'closing_rec_5_title': 'Formation de la Main-d\'œuvre en Cybersécurité',
        'closing_rec_5_desc': 'Investir dans la formation aux compétences de la main-d\'œuvre en cybersécurité grâce à des <strong>programmes de formation échelonnés et des certifications spécialisées en gestion des risques informatiques</strong>. Ceci est crucial pour réduire le risque de fuites d\'informations futures, car les employés internes auront un niveau de sensibilisation élevé concernant la confiance implicite.',
        'closing_rec_6_title': 'Priorité d\'Acquisition DLP et DRM',
        'closing_rec_6_desc': 'L\'acquisition de systèmes <strong>DLP (Prévention des Fuites de Données)</strong> et <strong>DRM (Gestion des Droits Numériques)</strong> doit être traitée comme une <strong>priorité budgétaire non reportable</strong>, car ils constituent un moyen de remplacer la bureaucratie des formulaires papier physiques.'
    },
    'de': {
        'closing_item_5_title': 'Empirische Validierung & Konsens',
        'closing_item_5_desc': 'Das <strong>Endgültige Integrierte Risikominderungsprogramm</strong> wurde durch empirische Validierung durch <strong>9 Branchenexperten und Akademiker</strong> verbessert, was die Relevanz der Artefakte für die Endergebnisse belegt: <strong>7 von 11 Bedrohungen</strong> wurden als "Sehr Relevante" und <strong>4 von 11 Bedrohungen</strong> als "Relevante" eingestuft, und während der Phase der Teilnehmervalidierung wurde ein einstimmiger Konsens (100%) erzielt. Dies kann als Blaupause für Cybersicherheit dienen, die Lücken im strategischen Risikomanagement präzise mit der Ausführung taktischer Sicherheitskontrollen auf der Grundlage des <strong>Prinzips der Zero Trust Architecture</strong> in der Luft- und Raumfahrtindustrie abstimmt.',
        'closing_rec_title': '💡 Empfehlung',
        'closing_rec_badge': 'Strategische Nächste Schritte',
        'closing_rec_1_title': 'Dynamische HR-IT Integration',
        'closing_rec_1_desc': '<strong>Integration des Meldesystems</strong> für Änderungen im Mitarbeiterstatus (Versetzungen, Ruhestand, Kündigung) aus der Abteilung Human Capital (HC) mit dem IT-Managementsystem. Dies dient der Automatisierung des Entzugs von Systemzugriffsrechten in <strong>Echtzeit (dynamische Richtlinie)</strong>, um die Abhängigkeit von langsamen und risikoreichen manuellen bürokratischen Prozessen zu beseitigen.',
        'closing_rec_2_title': 'Institutioneller MFA-Übergang',
        'closing_rec_2_desc': 'Simulation eines schrittweisen Übergangs zur Nutzung von <strong>MFA auf institutioneller Ebene</strong>; bei guter Akzeptanz kann dies zu einer obligatorischen Richtlinie werden, die durch ein formelles Instrument (SKEP oder Dekret) erlassen wird.',
        'closing_rec_3_title': 'Obligatorische Ursachenanalyse',
        'closing_rec_3_desc': 'Formalisierung des <strong>Ursachenanalyseprozesses</strong> als obligatorisches Post-Incident-Verfahren durch Sicherstellung, dass der Vorstand und das Senior Management aktiv an der <strong>regelmäßigen Risikoüberwachung</strong> beteiligt sind. Derzeit ist APO12.06 Level 5 mit Null bewertet, da die Grundursachen nicht an die höchsten Entscheidungsträger eskaliert werden.',
        'closing_rec_4_title': 'Strengere Intranet-Governance',
        'closing_rec_4_desc': 'Festlegung einer formellen Richtlinie bezüglich strengerer <strong>Einschränkungen bei der Nutzung des Intranets</strong>. Dies zielt darauf ab, die IP-Reputation des Unternehmens vor Schäden zu schützen.',
        'closing_rec_5_title': 'Schulung des Cybersicherheitspersonals',
        'closing_rec_5_desc': 'Investitionen in Kompetenzschulungen für das Cybersicherheitspersonal durch <strong>gestufte Schulungsprogramme und spezialisierte IT-Risikomanagement-Zertifizierungen</strong>. Dies ist von entscheidender Bedeutung, um das Risiko künftiger Informationslecks zu verringern, da interne Mitarbeiter ein hohes Maß an Bewusstsein für implizites Vertrauen haben werden.',
        'closing_rec_6_title': 'Priorität für DLP & DRM-Beschaffung',
        'closing_rec_6_desc': 'Die Beschaffung von <strong>DLP (Data Leak Prevention)</strong>- und <strong>DRM (Digital Rights Management)</strong>-Systemen sollte als <strong>nicht aufschiebbare Budgetpriorität</strong> behandelt werden, da sie eine Möglichkeit darstellen, die Bürokratie physischer Papierformulare zu ersetzen.'
    },
    'zh': {
        'closing_item_5_title': '实证验证与共识',
        'closing_item_5_desc': '通过 <strong>9 位行业专家和学者</strong> 的实证验证，<strong>最终的综合风险缓解计划</strong>得到了增强，证明了工件与最终结果的相关性：<strong>11 种威胁中的 7 种</strong>被评为“高度相关”，<strong>11 种威胁中的 4 种</strong>被评为“相关”，并在参与者验证阶段达成了一致共识 (100%)。这可以作为网络安全的蓝图，将战略风险管理差距与基于航空航天工业中 <strong>零信任架构原则</strong> 的战术安全控制的执行精确结合。',
        'closing_rec_title': '💡 建议',
        'closing_rec_badge': '战略下一步',
        'closing_rec_1_title': '动态人力资源-IT 整合',
        'closing_rec_1_desc': '<strong>整合报告系统</strong>，将人力资本 (HC) 部门的员工状态变化（调动、退休、辞职）与信息技术 (IT) 管理系统相结合。这是为了在 <strong>实时（动态策略）</strong> 中自动撤销系统访问权限，以消除对缓慢且高风险的手动官僚流程的依赖。',
        'closing_rec_2_title': '制度性多因素认证 (MFA) 过渡',
        'closing_rec_2_desc': '模拟向在 <strong>机构层面使用 MFA</strong> 的分阶段过渡；如果受到好评，这可以成为通过正式工具（SKEP 或法令）发布的强制性政策。',
        'closing_rec_3_title': '强制性根本原因分析',
        'closing_rec_3_desc': '通过确保董事会和高级管理层积极参与 <strong>定期风险监督</strong>，将 <strong>根本原因分析过程</strong> 正式化为强制性的事件后程序。目前，APO12.06 第 5 级评分为零，因为根本原因没有上报给最高决策者。',
        'closing_rec_4_title': '更严格的内部网治理',
        'closing_rec_4_desc': '制定一项关于更严格 <strong>限制内部网使用</strong> 的正式政策。这旨在保护公司的 IP 声誉免受损害。',
        'closing_rec_5_title': '网络安全员工培训',
        'closing_rec_5_desc': '通过 <strong>分级培训计划和专门的 IT 风险管理认证</strong> 投资于网络安全劳动力的能力培训。这对于降低未来信息泄露的风险至关重要，因为内部员工将对隐性信任有很高的认识。',
        'closing_rec_6_title': 'DLP & DRM 采购优先级',
        'closing_rec_6_desc': '应将采购 <strong>DLP (数据防泄露)</strong> 和 <strong>DRM (数字版权管理)</strong> 系统视为 <strong>不可推迟的预算优先事项</strong>，因为它们是取代物理纸质表格官僚主义的一种方式。'
    },
    'ja': {
        'closing_item_5_title': '実証的検証とコンセンサス',
        'closing_item_5_desc': '<strong>最終的な統合リスク軽減プログラム</strong>は、<strong>9人の業界専門家と学者</strong>による実証的検証を通じて強化され、成果物と最終結果の関連性が証明されました。<strong>11の脅威のうち7つ</strong>が「関連性が高い」、<strong>11の脅威のうち4つ</strong>が「関連性がある」と評価され、参加者検証フェーズで全会一致のコンセンサス（100％）に達しました。これは、航空宇宙産業における<strong>ゼロトラストアーキテクチャの原則</strong>に基づく戦術的セキュリティ制御の実行と戦略的リスク管理のギャップを正確に一致させるサイバーセキュリティの青写真として機能します。',
        'closing_rec_title': '💡 推奨事項',
        'closing_rec_badge': '戦略的な次のステップ',
        'closing_rec_1_title': '動的なHR-IT統合',
        'closing_rec_1_desc': 'ヒューマンキャピタル (HC) 部門からの従業員ステータスの変更 (異動、退職、辞任) の<strong>レポートシステムをIT管理システムと統合</strong>します。これは、遅くてリスクの高い手動の官僚的なプロセスへの依存をなくすために、<strong>リアルタイム（動的ポリシー）</strong>でシステムアクセス権の取り消しを自動化するためです。',
        'closing_rec_2_title': '組織的なMFA移行',
        'closing_rec_2_desc': '<strong>組織レベルでのMFA</strong>の使用への段階的な移行をシミュレートします。好評であれば、これは公式の文書 (SKEP または法令) を通じて発行される義務的なポリシーになる可能性があります。',
        'closing_rec_3_title': '必須の根本原因分析',
        'closing_rec_3_desc': '取締役会と上級管理職が<strong>定期的なリスク監視</strong>に積極的に関与していることを確認することにより、<strong>根本原因分析プロセス</strong>を必須のインシデント後の手順として正式化します。現在、根本原因が最高意思決定者にエスカレーションされていないため、APO12.06レベル5はゼロと評価されています。',
        'closing_rec_4_title': 'より厳格なイントラネットガバナンス',
        'closing_rec_4_desc': '<strong>イントラネットの使用に関するより厳格な制限</strong>に関する正式なポリシーを確立します。これは、会社のIP評判が損なわれるのを防ぐことを目的としています。',
        'closing_rec_5_title': 'サイバーセキュリティ従業員トレーニング',
        'closing_rec_5_desc': '<strong>段階的なトレーニングプログラムと専門的なITリスク管理認定</strong>を通じて、サイバーセキュリティ従業員のコンピテンシートレーニングに投資します。内部従業員は暗黙の信頼に関して高いレベルの認識を持つようになるため、これは将来の情報漏えいのリスクを減らすために重要です。',
        'closing_rec_6_title': 'DLP & DRM 調達の優先順位',
        'closing_rec_6_desc': '<strong>DLP（データ漏えい防止）</strong>および<strong>DRM（デジタル著作権管理）</strong>システムの調達は、物理的な紙のフォームの官僚主義に代わる方法の1つであるため、<strong>延期できない予算の優先事項</strong>として扱う必要があります。'
    },
    'ko': {
        'closing_item_5_title': '경험적 검증 및 합의',
        'closing_item_5_desc': '<strong>최종 통합 위험 완화 프로그램</strong>은 <strong>9명의 업계 전문가 및 학자</strong>의 경험적 검증을 통해 강화되었으며 산출물과 최종 결과의 관련성을 입증했습니다. <strong>11가지 위협 중 7가지</strong>는 "매우 관련성 높음"으로, <strong>11가지 위협 중 4가지</strong>는 "관련성 있음"으로 평가되었으며 참가자 검증 단계에서 만장일치(100%) 합의에 도달했습니다. 이는 항공 우주 산업에서 <strong>제로 트러스트 아키텍처 원칙</strong>을 기반으로 전술적 보안 통제의 실행과 전략적 위험 관리 격차를 정확하게 조정하는 사이버 보안의 청사진 역할을 할 수 있습니다.',
        'closing_rec_title': '💡 권고사항',
        'closing_rec_badge': '전략적 다음 단계',
        'closing_rec_1_title': '동적 HR-IT 통합',
        'closing_rec_1_desc': '인적 자본(HC) 부서의 직원 상태 변경(전근, 퇴직, 사임)에 대한 <strong>보고 시스템을 정보 기술(IT) 관리 시스템과 통합</strong>합니다. 이는 느리고 위험이 높은 수동 관료적 프로세스에 대한 의존도를 없애기 위해 <strong>실시간(동적 정책)</strong>으로 시스템 액세스 권한 취소를 자동화하기 위한 것입니다.',
        'closing_rec_2_title': '기관 MFA 전환',
        'closing_rec_2_desc': '<strong>기관 수준에서의 MFA</strong> 사용에 대한 단계적 전환을 시뮬레이션합니다. 좋은 반응을 얻으면 공식 문서(SKEP 또는 법령)를 통해 발행되는 의무 정책이 될 수 있습니다.',
        'closing_rec_3_title': '의무적 근본 원인 분석',
        'closing_rec_3_desc': '이사회와 고위 경영진이 <strong>주기적인 위험 감독</strong>에 적극적으로 참여하도록 함으로써 <strong>근본 원인 분석 프로세스</strong>를 필수적인 사고 후 절차로 공식화합니다. 현재 근본 원인이 최고 의사 결정권자에게 에스컬레이션되지 않기 때문에 APO12.06 레벨 5는 0으로 평가됩니다.',
        'closing_rec_4_title': '더 엄격한 인트라넷 거버넌스',
        'closing_rec_4_desc': '<strong>인트라넷 사용에 대한 더 엄격한 제한</strong>과 관련된 공식 정책을 수립합니다. 이는 회사의 IP 평판이 손상되지 않도록 보호하는 것을 목표로 합니다.',
        'closing_rec_5_title': '사이버 보안 인력 교육',
        'closing_rec_5_desc': '<strong>단계별 교육 프로그램 및 전문 IT 위험 관리 인증</strong>을 통해 사이버 보안 인력의 역량 교육에 투자하십시오. 내부 직원이 암묵적 신뢰와 관련하여 높은 수준의 인식을 갖게 되므로 이는 향후 정보 유출 위험을 줄이는 데 중요합니다.',
        'closing_rec_6_title': 'DLP 및 DRM 조달 우선순위',
        'closing_rec_6_desc': '<strong>DLP(데이터 유출 방지)</strong> 및 <strong>DRM(디지털 권한 관리)</strong> 시스템의 조달은 실제 종이 양식의 관료주의를 대체하는 한 가지 방법이므로 <strong>연기할 수 없는 예산 우선순위</strong>로 취급되어야 합니다.'
    },
    'ar': {
        'closing_item_5_title': 'التحقق التجريبي والإجماع',
        'closing_item_5_desc': 'تم تعزيز <strong>البرنامج النهائي المتكامل لتخفيف المخاطر</strong> من خلال التحقق التجريبي بواسطة <strong>9 خبراء وأكاديميين في الصناعة</strong>، مما يثبت مدى صلة العناصر بالنتائج النهائية: <strong>7 من أصل 11 تهديدًا</strong> تم تقييمها على أنها "ذات صلة قوية" و <strong>4 من أصل 11 تهديدًا</strong> تم تقييمها على أنها "ذات صلة"، وتم التوصل إلى إجماع (100%) خلال مرحلة التحقق من المشاركين. يمكن أن يكون هذا بمثابة مخطط للأمن السيبراني ينسق بدقة الفجوات في إدارة المخاطر الاستراتيجية مع تنفيذ ضوابط الأمان التكتيكية بناءً على <strong>مبدأ هندسة انعدام الثقة</strong> في صناعة الطيران.',
        'closing_rec_title': '💡 توصية',
        'closing_rec_badge': 'الخطوات الاستراتيجية التالية',
        'closing_rec_1_title': 'التكامل الديناميكي بين الموارد البشرية وتكنولوجيا المعلومات',
        'closing_rec_1_desc': '<strong>دمج نظام الإبلاغ</strong> عن التغييرات في حالة الموظف (التحويلات، التقاعد، الاستقالة) من قسم رأس المال البشري (HC) مع نظام إدارة تكنولوجيا المعلومات (IT). ويهدف ذلك إلى أتمتة إلغاء حقوق الوصول إلى النظام في <strong>الوقت الفعلي (سياسة ديناميكية)</strong> من أجل القضاء على الاعتماد على العمليات البيروقراطية اليدوية البطيئة والعالية المخاطر.',
        'closing_rec_2_title': 'انتقال المصادقة متعددة العوامل المؤسسية',
        'closing_rec_2_desc': 'محاكاة انتقال تدريجي لاستخدام <strong>MFA على المستوى المؤسسي</strong>؛ إذا لاقى استحسانًا، فقد يصبح هذا سياسة إلزامية تصدر من خلال أداة رسمية (SKEP أو مرسوم).',
        'closing_rec_3_title': 'تحليل السبب الجذري الإلزامي',
        'closing_rec_3_desc': 'إضفاء الطابع الرسمي على <strong>عملية تحليل السبب الجذري</strong> كإجراء إلزامي بعد الحادث من خلال ضمان مشاركة مجلس الإدارة والإدارة العليا بنشاط في <strong>الرقابة الدورية على المخاطر</strong>. حاليًا، تم تصنيف APO12.06 Level 5 بصفر لأنه لم يتم تصعيد الأسباب الجذرية إلى أعلى صانعي القرار.',
        'closing_rec_4_title': 'حوكمة أكثر صرامة للإنترانت',
        'closing_rec_4_desc': 'وضع سياسة رسمية بشأن <strong>قيود أكثر صرامة على استخدام الإنترانت</strong>. يهدف هذا إلى حماية سمعة الملكية الفكرية للشركة من التلف.',
        'closing_rec_5_title': 'تدريب القوى العاملة في مجال الأمن السيبراني',
        'closing_rec_5_desc': 'الاستثمار في تدريب كفاءة القوى العاملة في مجال الأمن السيبراني من خلال <strong>برامج تدريب متدرجة وشهادات متخصصة في إدارة مخاطر تكنولوجيا المعلومات</strong>. يعد هذا أمرًا بالغ الأهمية لتقليل مخاطر تسريب المعلومات في المستقبل، حيث سيكون لدى الموظفين الداخليين مستوى عالٍ من الوعي فيما يتعلق بالثقة الضمنية.',
        'closing_rec_6_title': 'أولوية شراء DLP و DRM',
        'closing_rec_6_desc': 'يجب التعامل مع شراء أنظمة <strong>DLP (منع تسرب البيانات)</strong> و <strong>DRM (إدارة الحقوق الرقمية)</strong> كـ <strong>أولوية ميزانية لا يمكن تأجيلها</strong>، حيث إنها طريقة واحدة لاستبدال بيروقراطية النماذج الورقية المادية.'
    },
    'ru': {
        'closing_item_5_title': 'Эмпирическая Валидация и Консенсус',
        'closing_item_5_desc': '<strong>Окончательная Интегрированная Программа Снижения Рисков</strong> была улучшена за счет эмпирической проверки <strong>9 отраслевыми экспертами и учеными</strong>, что доказывает актуальность артефактов для окончательных результатов: <strong>7 из 11 угроз</strong> были оценены как «в высокой степени актуальные», а <strong>4 из 11 угроз</strong> были оценены как «актуальные», и во время фазы валидации участниками был достигнут единогласный консенсус (100%). Это может служить планом обеспечения кибербезопасности, который точно согласовывает пробелы в стратегическом управлении рисками с выполнением тактических мер безопасности на основе <strong>принципа архитектуры нулевого доверия (ZTA)</strong> в аэрокосмической отрасли.',
        'closing_rec_title': '💡 Рекомендация',
        'closing_rec_badge': 'Стратегические Следующие Шаги',
        'closing_rec_1_title': 'Динамическая Интеграция HR-IT',
        'closing_rec_1_desc': '<strong>Интегрировать систему отчетности</strong> об изменениях статуса сотрудников (переводы, выход на пенсию, увольнение) из отдела человеческого капитала (HC) с системой управления информационными технологиями (IT). Это необходимо для автоматизации аннулирования прав доступа к системе в <strong>режиме реального времени (динамическая политика)</strong>, чтобы устранить зависимость от медленных и высокорискованных ручных бюрократических процессов.',
        'closing_rec_2_title': 'Институциональный Переход на MFA',
        'closing_rec_2_desc': 'Смоделировать поэтапный переход к использованию <strong>МФА (многофакторная аутентификация) на институциональном уровне</strong>; в случае положительного восприятия это может стать обязательной политикой, издаваемой через официальный документ (SKEP или Указ).',
        'closing_rec_3_title': 'Обязательный Анализ Первопричин',
        'closing_rec_3_desc': 'Формализовать <strong>процесс анализа первопричин</strong> как обязательную процедуру после инцидента, обеспечив активное участие совета директоров и высшего руководства в <strong>периодическом надзоре за рисками</strong>. В настоящее время APO12.06 Уровень 5 оценивается как нулевой, поскольку основные причины не доводятся до сведения лиц, принимающих решения на самом высоком уровне.',
        'closing_rec_4_title': 'Более Строгое Управление Интранетом',
        'closing_rec_4_desc': 'Установить официальную политику в отношении более строгих <strong>ограничений на использование интранета</strong>. Это направлено на защиту репутации интеллектуальной собственности компании от ущерба.',
        'closing_rec_5_title': 'Обучение Персонала Кибербезопасности',
        'closing_rec_5_desc': 'Инвестировать в обучение компетентности персонала по кибербезопасности посредством <strong>многоуровневых программ обучения и специализированных сертификаций по управлению ИТ-рисками</strong>. Это имеет решающее значение для снижения риска утечки информации в будущем, поскольку внутренние сотрудники будут иметь высокий уровень осведомленности о неявном доверии.',
        'closing_rec_6_title': 'Приоритет Закупок DLP и DRM',
        'closing_rec_6_desc': 'Закупка систем <strong>DLP (предотвращение утечки данных)</strong> и <strong>DRM (управление цифровыми правами)</strong> должна рассматриваться как <strong>неотложный приоритет бюджета</strong>, поскольку это один из способов заменить бюрократию физических бумажных форм.'
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

print("Done recommendations")
