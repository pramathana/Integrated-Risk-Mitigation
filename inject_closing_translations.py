import re
import json

file_path = "c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML with data-i18n attributes
html_replacements = [
    ('<h2 class="closing-title">🎯 Conclusion</h2>', '<h2 class="closing-title" data-i18n="closing_title">🎯 Conclusion</h2>'),
    ('<span class="closing-badge">Key Points</span>', '<span class="closing-badge" data-i18n="closing_badge">Key Points</span>'),
    ('<div class="closing-item-title">Risk Profile & Threat Identification</div>', '<div class="closing-item-title" data-i18n="closing_item_1_title">Risk Profile & Threat Identification</div>'),
    ('<div class="closing-item-desc">The risk profile was successfully compiled into a <strong>Priority Risk\n                  List</strong>, identifying <strong>11 contemporary threats</strong> based on qualitative studies and\n                structured interviews that were verified by internal employees in accordance with DetereCo\'s operational\n                conditions. There are <strong>3 threats with a Moderate risk level</strong> that are the highest\n                priority (T.10, T.11, T.09), followed by <strong>3 threats with Low to Moderate risk</strong> (T.04,\n                T.07, T.02), and finally <strong>5 threats classified as Low risk</strong> (T.01, T.03, T.05, T.06,\n                T.08).</div>', '<div class="closing-item-desc" data-i18n="closing_item_1_desc">The risk profile was successfully compiled into a <strong>Priority Risk List</strong>, identifying <strong>11 contemporary threats</strong> based on qualitative studies and structured interviews that were verified by internal employees in accordance with DetereCo\'s operational conditions. There are <strong>3 threats with a Moderate risk level</strong> that are the highest priority (T.10, T.11, T.09), followed by <strong>3 threats with Low to Moderate risk</strong> (T.04, T.07, T.02), and finally <strong>5 threats classified as Low risk</strong> (T.01, T.03, T.05, T.06, T.08).</div>'),
    ('<div class="closing-item-title">Universal Risk Modification under ZTA</div>', '<div class="closing-item-title" data-i18n="closing_item_2_title">Universal Risk Modification under ZTA</div>'),
    ('<div class="closing-item-desc">Although there are <strong>8 threats</strong> whose risk levels align with\n                the organization\'s risk appetite, because the <strong>Zero Trust Architecture</strong> principle assumes\n                that every threat will be exploited by an attacker and existing control mechanisms have not been\n                implemented in accordance with the <strong>7 Tenets of NIST SP 800-207</strong>, the entire Priority\n                Risk List, containing 11 threat risk, falls under the <strong>"Risk Modification"</strong> response\n                option. This is done to design a <strong>Risk Mitigation Program (RMP)</strong> based on the principles\n                of Zero Trust Architecture.</div>', '<div class="closing-item-desc" data-i18n="closing_item_2_desc">Although there are <strong>8 threats</strong> whose risk levels align with the organization\'s risk appetite, because the <strong>Zero Trust Architecture</strong> principle assumes that every threat will be exploited by an attacker and existing control mechanisms have not been implemented in accordance with the <strong>7 Tenets of NIST SP 800-207</strong>, the entire Priority Risk List, containing 11 threat risk, falls under the <strong>"Risk Modification"</strong> response option. This is done to design a <strong>Risk Mitigation Program (RMP)</strong> based on the principles of Zero Trust Architecture.</div>'),
    ('<div class="closing-item-title">Governance & Oversight Deficiencies</div>', '<div class="closing-item-title" data-i18n="closing_item_3_title">Governance & Oversight Deficiencies</div>'),
    ('<div class="closing-item-desc">The results of the capability level assessment highlight deficiencies in\n                the domain of <strong>executive strategic oversight</strong> (EDM03.01, EDM03.02, and EDM03.03) stemming\n                from the lack of training programs and the absence of active, substantive oversight by stakeholders.\n                Weaknesses in <strong>managerial operational execution</strong> in the field (APO12.01, APO12.02,\n                APO12.03, APO12.04, and APO12.06), which collectively constitute the root cause of the company\'s exposed\n                technical vulnerabilities.</div>', '<div class="closing-item-desc" data-i18n="closing_item_3_desc">The results of the capability level assessment highlight deficiencies in the domain of <strong>executive strategic oversight</strong> (EDM03.01, EDM03.02, and EDM03.03) stemming from the lack of training programs and the absence of active, substantive oversight by stakeholders. Weaknesses in <strong>managerial operational execution</strong> in the field (APO12.01, APO12.02, APO12.03, APO12.04, and APO12.06), which collectively constitute the root cause of the company\'s exposed technical vulnerabilities.</div>'),
    ('<div class="closing-item-title">ISO 27005 & COBIT 2019 Integration</div>', '<div class="closing-item-title" data-i18n="closing_item_4_title">ISO 27005 & COBIT 2019 Integration</div>'),
    ('<div class="closing-item-desc">The <strong>Integrated Risk Mitigation Program</strong> was successfully\n                designed by adopting the <strong>ISO/IEC 27005 process flow</strong> (from context establishment and\n                risk assessment to risk treatment). The 11 priority risks were then precisely mapped to governance\n                practice weaknesses in the <strong>COBIT 2019 domains EDM03 and APO12</strong>. This mapping\n                demonstrates that the root cause of each technical vulnerability can be directly traced to specific\n                deficiencies in governance management practices that are not yet optimal.</div>', '<div class="closing-item-desc" data-i18n="closing_item_4_desc">The <strong>Integrated Risk Mitigation Program</strong> was successfully designed by adopting the <strong>ISO/IEC 27005 process flow</strong> (from context establishment and risk assessment to risk treatment). The 11 priority risks were then precisely mapped to governance practice weaknesses in the <strong>COBIT 2019 domains EDM03 and APO12</strong>. This mapping demonstrates that the root cause of each technical vulnerability can be directly traced to specific deficiencies in governance management practices that are not yet optimal.</div>')
]

# Note: The HTML whitespace might differ slightly. A regex approach is safer.
html_regex_replacements = [
    (r'<h2 class="closing-title">\s*🎯 Conclusion\s*</h2>', '<h2 class="closing-title" data-i18n="closing_title">🎯 Conclusion</h2>'),
    (r'<span class="closing-badge">\s*Key Points\s*</span>', '<span class="closing-badge" data-i18n="closing_badge">Key Points</span>'),
    (r'<div class="closing-item-title">\s*Risk Profile & Threat Identification\s*</div>', '<div class="closing-item-title" data-i18n="closing_item_1_title">Risk Profile & Threat Identification</div>'),
    (r'<div class="closing-item-title">\s*Universal Risk Modification under ZTA\s*</div>', '<div class="closing-item-title" data-i18n="closing_item_2_title">Universal Risk Modification under ZTA</div>'),
    (r'<div class="closing-item-title">\s*Governance & Oversight Deficiencies\s*</div>', '<div class="closing-item-title" data-i18n="closing_item_3_title">Governance & Oversight Deficiencies</div>'),
    (r'<div class="closing-item-title">\s*ISO 27005 & COBIT 2019 Integration\s*</div>', '<div class="closing-item-title" data-i18n="closing_item_4_title">ISO 27005 & COBIT 2019 Integration</div>')
]

for pat, repl in html_regex_replacements:
    content = re.sub(pat, repl, content, count=1)

desc_1_pat = r'<div class="closing-item-desc">\s*The risk profile was successfully compiled into a <strong>Priority Risk\s*List</strong>.*?\(T\.01, T\.03, T\.05, T\.06,\s*T\.08\)\.</div>'
desc_1_repl = '<div class="closing-item-desc" data-i18n="closing_item_1_desc">The risk profile was successfully compiled into a <strong>Priority Risk List</strong>, identifying <strong>11 contemporary threats</strong> based on qualitative studies and structured interviews that were verified by internal employees in accordance with DetereCo\'s operational conditions. There are <strong>3 threats with a Moderate risk level</strong> that are the highest priority (T.10, T.11, T.09), followed by <strong>3 threats with Low to Moderate risk</strong> (T.04, T.07, T.02), and finally <strong>5 threats classified as Low risk</strong> (T.01, T.03, T.05, T.06, T.08).</div>'
content = re.sub(desc_1_pat, desc_1_repl, content, flags=re.DOTALL)

desc_2_pat = r'<div class="closing-item-desc">\s*Although there are <strong>8 threats</strong>.*?principles\s*of Zero Trust Architecture\.</div>'
desc_2_repl = '<div class="closing-item-desc" data-i18n="closing_item_2_desc">Although there are <strong>8 threats</strong> whose risk levels align with the organization\'s risk appetite, because the <strong>Zero Trust Architecture</strong> principle assumes that every threat will be exploited by an attacker and existing control mechanisms have not been implemented in accordance with the <strong>7 Tenets of NIST SP 800-207</strong>, the entire Priority Risk List, containing 11 threat risk, falls under the <strong>"Risk Modification"</strong> response option. This is done to design a <strong>Risk Mitigation Program (RMP)</strong> based on the principles of Zero Trust Architecture.</div>'
content = re.sub(desc_2_pat, desc_2_repl, content, flags=re.DOTALL)

desc_3_pat = r'<div class="closing-item-desc">\s*The results of the capability level assessment highlight.*?exposed\s*technical vulnerabilities\.</div>'
desc_3_repl = '<div class="closing-item-desc" data-i18n="closing_item_3_desc">The results of the capability level assessment highlight deficiencies in the domain of <strong>executive strategic oversight</strong> (EDM03.01, EDM03.02, and EDM03.03) stemming from the lack of training programs and the absence of active, substantive oversight by stakeholders. Weaknesses in <strong>managerial operational execution</strong> in the field (APO12.01, APO12.02, APO12.03, APO12.04, and APO12.06), which collectively constitute the root cause of the company\'s exposed technical vulnerabilities.</div>'
content = re.sub(desc_3_pat, desc_3_repl, content, flags=re.DOTALL)

desc_4_pat = r'<div class="closing-item-desc">\s*The <strong>Integrated Risk Mitigation Program</strong>.*?practices that are not yet optimal\.</div>'
desc_4_repl = '<div class="closing-item-desc" data-i18n="closing_item_4_desc">The <strong>Integrated Risk Mitigation Program</strong> was successfully designed by adopting the <strong>ISO/IEC 27005 process flow</strong> (from context establishment and risk assessment to risk treatment). The 11 priority risks were then precisely mapped to governance practice weaknesses in the <strong>COBIT 2019 domains EDM03 and APO12</strong>. This mapping demonstrates that the root cause of each technical vulnerability can be directly traced to specific deficiencies in governance management practices that are not yet optimal.</div>'
content = re.sub(desc_4_pat, desc_4_repl, content, flags=re.DOTALL)

# 2. Update el.innerText to el.innerHTML
content = content.replace("el.innerText = translations[lang][key];", "el.innerHTML = translations[lang][key];")

# 3. Add translations for all languages
translations = {
    'en': {
        'closing_title': '🎯 Conclusion',
        'closing_badge': 'Key Points',
        'closing_item_1_title': 'Risk Profile & Threat Identification',
        'closing_item_1_desc': 'The risk profile was successfully compiled into a <strong>Priority Risk List</strong>, identifying <strong>11 contemporary threats</strong> based on qualitative studies and structured interviews that were verified by internal employees in accordance with DetereCo\'s operational conditions. There are <strong>3 threats with a Moderate risk level</strong> that are the highest priority (T.10, T.11, T.09), followed by <strong>3 threats with Low to Moderate risk</strong> (T.04, T.07, T.02), and finally <strong>5 threats classified as Low risk</strong> (T.01, T.03, T.05, T.06, T.08).',
        'closing_item_2_title': 'Universal Risk Modification under ZTA',
        'closing_item_2_desc': 'Although there are <strong>8 threats</strong> whose risk levels align with the organization\'s risk appetite, because the <strong>Zero Trust Architecture</strong> principle assumes that every threat will be exploited by an attacker and existing control mechanisms have not been implemented in accordance with the <strong>7 Tenets of NIST SP 800-207</strong>, the entire Priority Risk List, containing 11 threat risk, falls under the <strong>"Risk Modification"</strong> response option. This is done to design a <strong>Risk Mitigation Program (RMP)</strong> based on the principles of Zero Trust Architecture.',
        'closing_item_3_title': 'Governance & Oversight Deficiencies',
        'closing_item_3_desc': 'The results of the capability level assessment highlight deficiencies in the domain of <strong>executive strategic oversight</strong> (EDM03.01, EDM03.02, and EDM03.03) stemming from the lack of training programs and the absence of active, substantive oversight by stakeholders. Weaknesses in <strong>managerial operational execution</strong> in the field (APO12.01, APO12.02, APO12.03, APO12.04, and APO12.06), which collectively constitute the root cause of the company\'s exposed technical vulnerabilities.',
        'closing_item_4_title': 'ISO 27005 & COBIT 2019 Integration',
        'closing_item_4_desc': 'The <strong>Integrated Risk Mitigation Program</strong> was successfully designed by adopting the <strong>ISO/IEC 27005 process flow</strong> (from context establishment and risk assessment to risk treatment). The 11 priority risks were then precisely mapped to governance practice weaknesses in the <strong>COBIT 2019 domains EDM03 and APO12</strong>. This mapping demonstrates that the root cause of each technical vulnerability can be directly traced to specific deficiencies in governance management practices that are not yet optimal.'
    },
    'id': {
        'closing_title': '🎯 Kesimpulan',
        'closing_badge': 'Poin Penting',
        'closing_item_1_title': 'Profil Risiko & Identifikasi Ancaman',
        'closing_item_1_desc': 'Profil risiko berhasil disusun menjadi <strong>Daftar Risiko Prioritas</strong>, mengidentifikasi <strong>11 ancaman kontemporer</strong> berdasarkan studi kualitatif dan wawancara terstruktur yang diverifikasi oleh karyawan internal sesuai dengan kondisi operasional DetereCo. Terdapat <strong>3 ancaman dengan tingkat risiko Sedang</strong> yang menjadi prioritas tertinggi (T.10, T.11, T.09), diikuti oleh <strong>3 ancaman dengan risiko Rendah ke Sedang</strong> (T.04, T.07, T.02), dan akhirnya <strong>5 ancaman diklasifikasikan sebagai risiko Rendah</strong> (T.01, T.03, T.05, T.06, T.08).',
        'closing_item_2_title': 'Modifikasi Risiko Universal di bawah ZTA',
        'closing_item_2_desc': 'Meskipun ada <strong>8 ancaman</strong> yang tingkat risikonya sesuai dengan selera risiko organisasi, karena prinsip <strong>Zero Trust Architecture</strong> mengasumsikan bahwa setiap ancaman akan dieksploitasi oleh penyerang dan mekanisme kontrol yang ada belum diimplementasikan sesuai dengan <strong>7 Prinsip NIST SP 800-207</strong>, seluruh Daftar Risiko Prioritas, yang berisi 11 risiko ancaman, berada di bawah opsi respons <strong>"Modifikasi Risiko"</strong>. Hal ini dilakukan untuk merancang <strong>Program Mitigasi Risiko (RMP)</strong> berdasarkan prinsip-prinsip Zero Trust Architecture.',
        'closing_item_3_title': 'Kekurangan Tata Kelola & Pengawasan',
        'closing_item_3_desc': 'Hasil penilaian tingkat kapabilitas menyoroti kekurangan dalam domain <strong>pengawasan strategis eksekutif</strong> (EDM03.01, EDM03.02, dan EDM03.03) yang berasal dari kurangnya program pelatihan dan tidak adanya pengawasan substantif yang aktif oleh pemangku kepentingan. Kelemahan dalam <strong>eksekusi operasional manajerial</strong> di lapangan (APO12.01, APO12.02, APO12.03, APO12.04, dan APO12.06), yang secara kolektif merupakan akar penyebab kerentanan teknis perusahaan yang terekspos.',
        'closing_item_4_title': 'Integrasi ISO 27005 & COBIT 2019',
        'closing_item_4_desc': '<strong>Program Mitigasi Risiko Terintegrasi</strong> berhasil dirancang dengan mengadopsi <strong>alur proses ISO/IEC 27005</strong> (mulai dari penetapan konteks dan penilaian risiko hingga perlakuan risiko). 11 risiko prioritas kemudian dipetakan secara tepat ke kelemahan praktik tata kelola dalam <strong>domain COBIT 2019 EDM03 dan APO12</strong>. Pemetaan ini menunjukkan bahwa akar penyebab setiap kerentanan teknis dapat ditelusuri langsung ke kelemahan spesifik dalam praktik manajemen tata kelola yang belum optimal.'
    },
    'es': {
        'closing_title': '🎯 Conclusión',
        'closing_badge': 'Puntos Clave',
        'closing_item_1_title': 'Perfil de Riesgo e Identificación de Amenazas',
        'closing_item_1_desc': 'El perfil de riesgo se compiló con éxito en una <strong>Lista de Riesgos Prioritarios</strong>, identificando <strong>11 amenazas contemporáneas</strong> basadas en estudios cualitativos y entrevistas estructuradas que fueron verificadas por empleados internos de acuerdo con las condiciones operativas de DetereCo. Hay <strong>3 amenazas con un nivel de riesgo Moderado</strong> que son la máxima prioridad (T.10, T.11, T.09), seguidas de <strong>3 amenazas con riesgo Bajo a Moderado</strong> (T.04, T.07, T.02), y finalmente <strong>5 amenazas clasificadas como de riesgo Bajo</strong> (T.01, T.03, T.05, T.06, T.08).',
        'closing_item_2_title': 'Modificación de Riesgo Universal bajo ZTA',
        'closing_item_2_desc': 'Aunque hay <strong>8 amenazas</strong> cuyos niveles de riesgo se alinean con el apetito de riesgo de la organización, debido a que el principio de <strong>Zero Trust Architecture</strong> asume que cada amenaza será explotada por un atacante y los mecanismos de control existentes no se han implementado de acuerdo con los <strong>7 Principios de NIST SP 800-207</strong>, toda la Lista de Riesgos Prioritarios, que contiene 11 riesgos de amenaza, cae bajo la opción de respuesta de <strong>"Modificación de Riesgo"</strong>. Esto se hace para diseñar un <strong>Programa de Mitigación de Riesgos (RMP)</strong> basado en los principios de Zero Trust Architecture.',
        'closing_item_3_title': 'Deficiencias de Gobernanza y Supervisión',
        'closing_item_3_desc': 'Los resultados de la evaluación del nivel de capacidad destacan deficiencias en el dominio de <strong>supervisión estratégica ejecutiva</strong> (EDM03.01, EDM03.02 y EDM03.03) derivadas de la falta de programas de capacitación y la ausencia de una supervisión sustantiva y activa por parte de las partes interesadas. Debilidades en la <strong>ejecución operativa gerencial</strong> en el campo (APO12.01, APO12.02, APO12.03, APO12.04 y APO12.06), que en conjunto constituyen la causa raíz de las vulnerabilidades técnicas expuestas de la empresa.',
        'closing_item_4_title': 'Integración de ISO 27005 y COBIT 2019',
        'closing_item_4_desc': 'El <strong>Programa Integrado de Mitigación de Riesgos</strong> fue diseñado con éxito adoptando el <strong>flujo de procesos de ISO/IEC 27005</strong> (desde el establecimiento del contexto y la evaluación de riesgos hasta el tratamiento de riesgos). Los 11 riesgos prioritarios se mapearon con precisión a las debilidades de las prácticas de gobernanza en los <strong>dominios de COBIT 2019 EDM03 y APO12</strong>. Este mapeo demuestra que la causa raíz de cada vulnerabilidad técnica puede rastrearse directamente hasta deficiencias específicas en las prácticas de gestión de la gobernanza que aún no son óptimas.'
    },
    'fr': {
        'closing_title': '🎯 Conclusion',
        'closing_badge': 'Points Clés',
        'closing_item_1_title': 'Profil de Risque et Identification des Menaces',
        'closing_item_1_desc': 'Le profil de risque a été compilé avec succès dans une <strong>Liste des Risques Prioritaires</strong>, identifiant <strong>11 menaces contemporaines</strong> basées sur des études qualitatives et des entretiens structurés vérifiés par des employés internes conformément aux conditions opérationnelles de DetereCo. Il y a <strong>3 menaces avec un niveau de risque Modéré</strong> qui sont la priorité absolue (T.10, T.11, T.09), suivies de <strong>3 menaces avec un risque Faible à Modéré</strong> (T.04, T.07, T.02), et enfin <strong>5 menaces classées comme à risque Faible</strong> (T.01, T.03, T.05, T.06, T.08).',
        'closing_item_2_title': 'Modification Universelle des Risques sous ZTA',
        'closing_item_2_desc': 'Bien qu\'il y ait <strong>8 menaces</strong> dont les niveaux de risque s\'alignent sur l\'appétit pour le risque de l\'organisation, parce que le principe de la <strong>Zero Trust Architecture</strong> suppose que chaque menace sera exploitée par un attaquant et que les mécanismes de contrôle existants n\'ont pas été mis en œuvre conformément aux <strong>7 Principes du NIST SP 800-207</strong>, l\'ensemble de la Liste des Risques Prioritaires, contenant 11 risques de menaces, relève de l\'option de réponse <strong>"Modification du Risque"</strong>. Cela est fait pour concevoir un <strong>Programme d\'Atténuation des Risques (RMP)</strong> basé sur les principes de la Zero Trust Architecture.',
        'closing_item_3_title': 'Lacunes en Matière de Gouvernance et de Surveillance',
        'closing_item_3_desc': 'Les résultats de l\'évaluation du niveau de capacité soulignent des lacunes dans le domaine de la <strong>surveillance stratégique exécutive</strong> (EDM03.01, EDM03.02 et EDM03.03) découlant du manque de programmes de formation et de l\'absence d\'une surveillance active et substantielle par les parties prenantes. Des faiblesses dans l\'<strong>exécution opérationnelle managériale</strong> sur le terrain (APO12.01, APO12.02, APO12.03, APO12.04 et APO12.06), qui constituent collectivement la cause profonde des vulnérabilités techniques exposées de l\'entreprise.',
        'closing_item_4_title': 'Intégration d\'ISO 27005 et COBIT 2019',
        'closing_item_4_desc': 'Le <strong>Programme Intégré d\'Atténuation des Risques</strong> a été conçu avec succès en adoptant le <strong>flux de processus ISO/IEC 27005</strong> (de l\'établissement du contexte et de l\'évaluation des risques au traitement des risques). Les 11 risques prioritaires ont ensuite été mappés avec précision aux faiblesses des pratiques de gouvernance dans les <strong>domaines COBIT 2019 EDM03 et APO12</strong>. Cette cartographie démontre que la cause profonde de chaque vulnérabilité technique peut être retracée directement à des lacunes spécifiques dans les pratiques de gestion de la gouvernance qui ne sont pas encore optimales.'
    },
    'de': {
        'closing_title': '🎯 Fazit',
        'closing_badge': 'Wichtige Punkte',
        'closing_item_1_title': 'Risikoprofil & Bedrohungsidentifikation',
        'closing_item_1_desc': 'Das Risikoprofil wurde erfolgreich in einer <strong>Prioritäten-Risikoliste</strong> zusammengefasst, in der <strong>11 aktuelle Bedrohungen</strong> identifiziert wurden, basierend auf qualitativen Studien und strukturierten Interviews, die von internen Mitarbeitern in Übereinstimmung mit den Betriebsbedingungen von DetereCo verifiziert wurden. Es gibt <strong>3 Bedrohungen mit einem moderaten Risikoniveau</strong>, die höchste Priorität haben (T.10, T.11, T.09), gefolgt von <strong>3 Bedrohungen mit niedrigem bis moderatem Risiko</strong> (T.04, T.07, T.02) und schließlich <strong>5 als risikoarm eingestuften Bedrohungen</strong> (T.01, T.03, T.05, T.06, T.08).',
        'closing_item_2_title': 'Universelle Risikomodifikation unter ZTA',
        'closing_item_2_desc': 'Obwohl es <strong>8 Bedrohungen</strong> gibt, deren Risikoniveau der Risikobereitschaft der Organisation entspricht, fällt die gesamte Prioritäten-Risikoliste mit 11 Bedrohungsrisiken unter die Reaktionsoption <strong>"Risikomodifikation"</strong>, da das Prinzip der <strong>Zero Trust Architecture</strong> davon ausgeht, dass jede Bedrohung von einem Angreifer ausgenutzt wird und bestehende Kontrollmechanismen nicht gemäß den <strong>7 Grundsätzen der NIST SP 800-207</strong> implementiert wurden. Dies geschieht, um ein <strong>Risikominderungsprogramm (RMP)</strong> basierend auf den Prinzipien der Zero Trust Architecture zu entwerfen.',
        'closing_item_3_title': 'Mängel in Governance und Aufsicht',
        'closing_item_3_desc': 'Die Ergebnisse der Bewertung des Fähigkeitsniveaus zeigen Mängel im Bereich der <strong>strategischen Aufsicht durch Führungskräfte</strong> (EDM03.01, EDM03.02 und EDM03.03) auf, die auf das Fehlen von Schulungsprogrammen und die Abwesenheit einer aktiven, inhaltlichen Aufsicht durch Stakeholder zurückzuführen sind. Schwächen in der <strong>operativen Durchführung durch das Management</strong> vor Ort (APO12.01, APO12.02, APO12.03, APO12.04 und APO12.06), die zusammen die Grundursache der exponierten technischen Schwachstellen des Unternehmens darstellen.',
        'closing_item_4_title': 'Integration von ISO 27005 & COBIT 2019',
        'closing_item_4_desc': 'Das <strong>Integrierte Risikominderungsprogramm</strong> wurde erfolgreich durch Übernahme des <strong>ISO/IEC 27005-Prozessablaufs</strong> entworfen (von der Kontextfestlegung und Risikobewertung bis zur Risikobehandlung). Die 11 vorrangigen Risiken wurden dann präzise auf Schwächen in der Governance-Praxis in den <strong>COBIT 2019-Domänen EDM03 und APO12</strong> abgebildet. Diese Abbildung zeigt, dass die Grundursache jeder technischen Schwachstelle direkt auf spezifische Mängel in den noch nicht optimalen Governance-Managementpraktiken zurückgeführt werden kann.'
    },
    'zh': {
        'closing_title': '🎯 结论',
        'closing_badge': '关键点',
        'closing_item_1_title': '风险概况与威胁识别',
        'closing_item_1_desc': '风险概况已成功汇编成<strong>优先风险列表</strong>，根据内部员工根据 DetereCo 运营条件验证的定性研究和结构化访谈，确定了 <strong>11 种当代威胁</strong>。有 <strong>3 个中等风险级别的威胁</strong> 是最高优先级 (T.10, T.11, T.09)，其次是 <strong>3 个中低风险威胁</strong> (T.04, T.07, T.02)，最后 <strong>5 个威胁被归类为低风险</strong> (T.01, T.03, T.05, T.06, T.08)。',
        'closing_item_2_title': 'ZTA 下的全面风险修正',
        'closing_item_2_desc': '尽管有 <strong>8 个威胁</strong> 的风险水平符合组织的风险偏好，但由于 <strong>零信任架构 (ZTA)</strong> 原则假设每个威胁都会被攻击者利用，并且现有控制机制尚未根据 <strong>NIST SP 800-207 的 7 项原则</strong> 实施，因此包含 11 个威胁风险的整个优先风险列表都属于 <strong>"风险修正"</strong> 响应选项。这样做是为了设计一个基于零信任架构原则的 <strong>风险缓解计划 (RMP)</strong>。',
        'closing_item_3_title': '治理和监督缺陷',
        'closing_item_3_desc': '能力水平评估结果突出了 <strong>执行战略监督</strong> 领域 (EDM03.01, EDM03.02 和 EDM03.03) 的缺陷，这源于缺乏培训计划以及利益相关者缺乏积极实质性的监督。现场 <strong>管理运营执行</strong> 方面的弱点 (APO12.01, APO12.02, APO12.03, APO12.04 和 APO12.06) 共同构成了公司暴露的技术漏洞的根本原因。',
        'closing_item_4_title': 'ISO 27005 与 COBIT 2019 整合',
        'closing_item_4_desc': '通过采用 <strong>ISO/IEC 27005 流程</strong>（从环境建立和风险评估到风险处理），成功设计了 <strong>综合风险缓解计划</strong>。然后将 11 个优先风险精确映射到 <strong>COBIT 2019 域 EDM03 和 APO12</strong> 中的治理实践弱点。这种映射表明，每个技术漏洞的根本原因都可以直接追溯到尚未优化的治理管理实践中的具体缺陷。'
    },
    'ja': {
        'closing_title': '🎯 結論',
        'closing_badge': 'キーポイント',
        'closing_item_1_title': 'リスクプロファイルと脅威の特定',
        'closing_item_1_desc': 'リスクプロファイルは<strong>優先リスクリスト</strong>に正常にまとめられ、DetereCoの運用条件に従って内部従業員によって検証された定性的研究と構造化されたインタビューに基づいて、<strong>11の現代の脅威</strong>が特定されました。優先度が最も高い<strong>中程度のリスクレベルの脅威が3つ</strong> (T.10, T.11, T.09) あり、それに続いて<strong>低〜中程度のリスクの脅威が3つ</strong> (T.04, T.07, T.02)、そして最後に<strong>低リスクに分類される脅威が5つ</strong> (T.01, T.03, T.05, T.06, T.08) あります。',
        'closing_item_2_title': 'ZTAに基づく普遍的なリスク修正',
        'closing_item_2_desc': 'リスクレベルが組織のリスク選好に一致する<strong>8つの脅威</strong>がありますが、<strong>ゼロトラストアーキテクチャ</strong>の原則ではすべての脅威が攻撃者によって悪用されると想定しており、既存の制御メカニズムは<strong>NIST SP 800-207の7つの原則</strong>に従って実装されていないため、11の脅威リスクを含む優先リスクリスト全体が<strong>「リスク修正」</strong>対応オプションに該当します。これは、ゼロトラストアーキテクチャの原則に基づいて<strong>リスク軽減プログラム (RMP)</strong> を設計するために行われます。',
        'closing_item_3_title': 'ガバナンスと監視の欠陥',
        'closing_item_3_desc': '能力レベル評価の結果は、トレーニングプログラムの欠如と利害関係者による積極的で実質的な監視の不在に起因する、<strong>経営幹部の戦略的監視</strong> (EDM03.01, EDM03.02, EDM03.03) のドメインにおける欠陥を浮き彫りにしています。現場の<strong>管理的運用実行</strong>における弱点 (APO12.01, APO12.02, APO12.03, APO12.04, APO12.06) が、総合して会社の露出した技術的脆弱性の根本原因となっています。',
        'closing_item_4_title': 'ISO 27005とCOBIT 2019の統合',
        'closing_item_4_desc': '<strong>統合リスク軽減プログラム</strong>は、<strong>ISO/IEC 27005プロセスフロー</strong>（コンテキストの確立とリスク評価からリスク対応まで）を採用することによって正常に設計されました。その後、11の優先リスクは、<strong>COBIT 2019ドメインEDM03およびAPO12</strong>のガバナンス慣行の弱点に正確にマッピングされました。このマッピングは、各技術的脆弱性の根本原因が、まだ最適化されていないガバナンス管理慣行の特定の欠陥に直接遡ることができることを示しています。'
    },
    'ko': {
        'closing_title': '🎯 결론',
        'closing_badge': '주요 요점',
        'closing_item_1_title': '위험 프로필 및 위협 식별',
        'closing_item_1_desc': '위험 프로필은 <strong>우선순위 위험 목록</strong>으로 성공적으로 컴파일되었으며, DetereCo의 운영 조건에 따라 내부 직원이 검증한 질적 연구 및 구조화된 인터뷰를 기반으로 <strong>11가지 현대적 위협</strong>을 식별했습니다. 가장 우선순위가 높은 <strong>중간 위험 수준의 위협이 3개</strong>(T.10, T.11, T.09) 있고, 그 다음으로 <strong>낮음에서 중간 위험의 위협이 3개</strong>(T.04, T.07, T.02), 마지막으로 <strong>낮은 위험으로 분류된 위협이 5개</strong>(T.01, T.03, T.05, T.06, T.08) 있습니다.',
        'closing_item_2_title': 'ZTA 하의 보편적 위험 수정',
        'closing_item_2_desc': '조직의 위험 성향과 일치하는 위험 수준을 가진 <strong>8가지 위협</strong>이 있지만, <strong>제로 트러스트 아키텍처(ZTA)</strong> 원칙은 모든 위협이 공격자에 의해 악용될 것이라고 가정하고 기존 통제 메커니즘이 <strong>NIST SP 800-207의 7가지 원칙</strong>에 따라 구현되지 않았기 때문에, 11가지 위협 위험을 포함하는 전체 우선순위 위험 목록은 <strong>"위험 수정"</strong> 대응 옵션에 해당합니다. 이는 제로 트러스트 아키텍처의 원칙에 따라 <strong>위험 완화 프로그램(RMP)</strong>을 설계하기 위해 수행됩니다.',
        'closing_item_3_title': '거버넌스 및 감독 결함',
        'closing_item_3_desc': '역량 수준 평가 결과는 교육 프로그램의 부족과 이해관계자의 적극적이고 실질적인 감독 부재로 인해 발생하는 <strong>임원 전략 감독</strong>(EDM03.01, EDM03.02, EDM03.03) 영역의 결함을 강조합니다. 현장의 <strong>관리적 운영 실행</strong>의 약점(APO12.01, APO12.02, APO12.03, APO12.04, APO12.06)은 전체적으로 회사의 노출된 기술적 취약성의 근본 원인을 구성합니다.',
        'closing_item_4_title': 'ISO 27005 및 COBIT 2019 통합',
        'closing_item_4_desc': '<strong>통합 위험 완화 프로그램</strong>은 <strong>ISO/IEC 27005 프로세스 흐름</strong>(컨텍스트 설정 및 위험 평가에서 위험 처리까지)을 채택하여 성공적으로 설계되었습니다. 그런 다음 11가지 우선순위 위험은 <strong>COBIT 2019 도메인 EDM03 및 APO12</strong>의 거버넌스 관행 약점에 정확하게 매핑되었습니다. 이 매핑은 각 기술적 취약성의 근본 원인이 아직 최적화되지 않은 거버넌스 관리 관행의 특정 결함으로 직접 추적될 수 있음을 보여줍니다.'
    },
    'ar': {
        'closing_title': '🎯 استنتاج',
        'closing_badge': 'النقاط الرئيسية',
        'closing_item_1_title': 'ملف تعريف المخاطر وتحديد التهديدات',
        'closing_item_1_desc': 'تم تجميع ملف تعريف المخاطر بنجاح في <strong>قائمة المخاطر ذات الأولوية</strong>، مع تحديد <strong>11 تهديدًا معاصرًا</strong> بناءً على دراسات نوعية ومقابلات منظمة تم التحقق منها من قبل موظفين داخليين وفقًا للظروف التشغيلية لشركة DetereCo. هناك <strong>3 تهديدات بمستوى خطر معتدل</strong> وهي الأولوية القصوى (T.10, T.11, T.09)، تليها <strong>3 تهديدات ذات مخاطر منخفضة إلى معتدلة</strong> (T.04, T.07, T.02)، وأخيرًا <strong>5 تهديدات مصنفة على أنها منخفضة المخاطر</strong> (T.01, T.03, T.05, T.06, T.08).',
        'closing_item_2_title': 'تعديل المخاطر الشامل تحت هندسة انعدام الثقة (ZTA)',
        'closing_item_2_desc': 'على الرغم من وجود <strong>8 تهديدات</strong> تتوافق مستويات مخاطرها مع شهية المخاطر للمؤسسة، ولأن مبدأ <strong>هندسة انعدام الثقة</strong> يفترض أن كل تهديد سيتم استغلاله من قبل المهاجم وأن آليات التحكم الحالية لم يتم تنفيذها وفقًا لـ <strong>المبادئ السبعة لـ NIST SP 800-207</strong>، فإن قائمة المخاطر ذات الأولوية بأكملها، والتي تحتوي على 11 خطر تهديد، تندرج تحت خيار الاستجابة <strong>"تعديل المخاطر"</strong>. يتم ذلك لتصميم <strong>برنامج تخفيف المخاطر (RMP)</strong> بناءً على مبادئ هندسة انعدام الثقة.',
        'closing_item_3_title': 'أوجه القصور في الحوكمة والرقابة',
        'closing_item_3_desc': 'تسلط نتائج تقييم مستوى القدرات الضوء على أوجه القصور في مجال <strong>الرقابة الاستراتيجية التنفيذية</strong> (EDM03.01 و EDM03.02 و EDM03.03) الناتجة عن نقص البرامج التدريبية وغياب الرقابة النشطة والجوهرية من قبل أصحاب المصلحة. وتشكل نقاط الضعف في <strong>التنفيذ التشغيلي الإداري</strong> في الميدان (APO12.01 و APO12.02 و APO12.03 و APO12.04 و APO12.06)، معًا، السبب الجذري للثغرات الفنية المكشوفة للشركة.',
        'closing_item_4_title': 'تكامل ISO 27005 و COBIT 2019',
        'closing_item_4_desc': 'تم تصميم <strong>برنامج التخفيف المتكامل للمخاطر</strong> بنجاح من خلال اعتماد <strong>مسار عملية ISO/IEC 27005</strong> (من إنشاء السياق وتقييم المخاطر إلى معالجة المخاطر). ثم تم تعيين المخاطر ذات الأولوية الـ 11 بدقة إلى نقاط الضعف في ممارسات الحوكمة في <strong>مجالات COBIT 2019 EDM03 و APO12</strong>. يوضح هذا التعيين أنه يمكن تتبع السبب الجذري لكل ثغرة فنية مباشرة إلى أوجه قصور محددة في ممارسات إدارة الحوكمة التي لم تصل بعد إلى المستوى الأمثل.'
    },
    'ru': {
        'closing_title': '🎯 Заключение',
        'closing_badge': 'Ключевые моменты',
        'closing_item_1_title': 'Профиль Рисков и Выявление Угроз',
        'closing_item_1_desc': 'Профиль рисков был успешно скомпилирован в <strong>Список Приоритетных Рисков</strong>, в котором выявлено <strong>11 современных угроз</strong> на основе качественных исследований и структурированных интервью, которые были проверены внутренними сотрудниками в соответствии с условиями эксплуатации DetereCo. Имеется <strong>3 угрозы с умеренным уровнем риска</strong>, которые имеют наивысший приоритет (T.10, T.11, T.09), за ними следуют <strong>3 угрозы с уровнем риска от низкого до умеренного</strong> (T.04, T.07, T.02), и, наконец, <strong>5 угроз классифицируются как с низким уровнем риска</strong> (T.01, T.03, T.05, T.06, T.08).',
        'closing_item_2_title': 'Универсальная Модификация Рисков при ZTA',
        'closing_item_2_desc': 'Хотя существует <strong>8 угроз</strong>, уровни риска которых соответствуют аппетиту организации к риску, поскольку принцип <strong>Zero Trust Architecture (ZTA)</strong> предполагает, что каждая угроза будет использована злоумышленником, а существующие механизмы контроля не были внедрены в соответствии с <strong>7 принципами NIST SP 800-207</strong>, весь Список Приоритетных Рисков, содержащий 11 рисков угроз, подпадает под вариант реагирования <strong>«Модификация Риска»</strong>. Это делается для разработки <strong>Программы Снижения Рисков (RMP)</strong>, основанной на принципах архитектуры нулевого доверия.',
        'closing_item_3_title': 'Недостатки Управления и Надзора',
        'closing_item_3_desc': 'Результаты оценки уровня возможностей выявляют недостатки в области <strong>стратегического надзора со стороны руководства</strong> (EDM03.01, EDM03.02 и EDM03.03), возникающие из-за нехватки программ обучения и отсутствия активного, предметного контроля со стороны заинтересованных сторон. Слабые стороны в <strong>управленческом оперативном исполнении</strong> на местах (APO12.01, APO12.02, APO12.03, APO12.04 и APO12.06), которые в совокупности составляют первопричину выявленных технических уязвимостей компании.',
        'closing_item_4_title': 'Интеграция ISO 27005 и COBIT 2019',
        'closing_item_4_desc': '<strong>Интегрированная Программа Снижения Рисков</strong> была успешно разработана путем принятия <strong>технологического процесса ISO/IEC 27005</strong> (от определения контекста и оценки рисков до обработки рисков). Затем 11 приоритетных рисков были точно сопоставлены со слабыми местами практики управления в <strong>доменах COBIT 2019 EDM03 и APO12</strong>. Это сопоставление показывает, что первопричину каждой технической уязвимости можно проследить непосредственно до конкретных недостатков в практике управления, которые еще не являются оптимальными.'
    }
}

for lang, trans_dict in translations.items():
    # Construct translation entries string
    entries_str = ""
    for k, v in trans_dict.items():
        # Escape quotes and backslashes
        val = v.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", " ")
        entries_str += f'          "{k}": "{val}",\n'
    
    # Inject into content
    pattern = r'(' + lang + r':\s*\{)'
    replacement = r'\1\n' + entries_str
    content = re.sub(pattern, replacement, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
