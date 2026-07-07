import re

file_path = "c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- 1. Add data-i18n attributes ---

regex_replacements = [
    # Section Headers
    (r'<h2 class="sec-title">\s*Family\s*</h2>', '<h2 class="sec-title" data-i18n="ack_sec_family">Family</h2>'),
    (r'<h2 class="sec-title">\s*Advisors\s*</h2>', '<h2 class="sec-title" data-i18n="ack_sec_advisors">Advisors</h2>'),
    (r'<h2 class="sec-title">\s*Research Partners\s*</h2>', '<h2 class="sec-title" data-i18n="ack_sec_research_partners">Research Partners</h2>'),
    (r'<h2 class="sec-title">\s*Colleagues\s*</h2>', '<h2 class="sec-title" data-i18n="ack_sec_colleagues">Colleagues</h2>'),

    # Family Card
    (r'<p class="fc-label">\s*Primary Dedication\s*</p>', '<p class="fc-label" data-i18n="ack_fam_label">Primary Dedication</p>'),
    (r'<h3 class="fc-title">\s*Immediate &amp; Extended Family\s*</h3>', '<h3 class="fc-title" data-i18n="ack_fam_title">Immediate &amp; Extended Family</h3>'),
    (r'<p class="fc-body">\s*Dedicated with deep gratitude to the author\'s <strong>immediate</strong> and <strong>extended\s*family</strong>.*?to their fullest extent\.\s*</p>', '<p class="fc-body" data-i18n="ack_fam_body">Dedicated with deep gratitude to the author\'s <strong>immediate</strong> and <strong>extended family</strong>. The prayers that have always accompanied me, the moral guidance, and the boundless support have been the essential foundation that has enabled me to keep moving forward and complete this series of final thesis research projects to their fullest extent.</p>'),

    # Advisors Card
    (r'<p class="sup-role">\s*First Advisor\s*</p>', '<p class="sup-role" data-i18n="ack_adv_role_1">First Advisor</p>'),
    (r'<p class="sup-body">\s*Thank you for your meticulous direction.*?invaluable guiding light\.\s*</p>', '<p class="sup-body" data-i18n="ack_adv_body_1">Thank you for your meticulous direction, patient guidance, and full dedication in mentoring the author from the beginning to the end of this final project. Every piece of advice provided has been an invaluable guiding light.</p>'),
    (r'<span class="sup-tag">\s*Academic Advisor\s*</span>', '<span class="sup-tag" data-i18n="ack_adv_tag_1">Academic Advisor</span>'),
    
    (r'<p class="sup-role">\s*Second Advisor\s*</p>', '<p class="sup-role" data-i18n="ack_adv_role_2">Second Advisor</p>'),
    (r'<p class="sup-body">\s*Thank you for your deep academic insights.*?analytical framework of this final\s*project\.\s*</p>', '<p class="sup-body" data-i18n="ack_adv_body_2">Thank you for your deep academic insights, encouragement to always think critically, and highly helpful technical guidance in strengthening the methodology and analytical framework of this final project.</p>'),
    (r'<span class="sup-tag">\s*Technical Advisor\s*</span>', '<span class="sup-tag" data-i18n="ack_adv_tag_2">Technical Advisor</span>'),

    # Research Partners Card
    (r'<p class="co-label">\s*Resource Persons &amp; Data Partners\s*</p>', '<p class="co-label" data-i18n="ack_co_label">Resource Persons &amp; Data Partners</p>'),
    (r'<p style="font-size:14px;color:var\(--slate-muted\);line-height:1\.8;text-align:justify">\s*Thank you to the entire management.*?empirical foundation for this research\.\s*</p>', '<p style="font-size:14px;color:var(--slate-muted);line-height:1.8;text-align:justify" data-i18n="ack_co_body">Thank you to the entire management and IT division at <strong style="color:var(--slate)">DetereCo</strong> who, with full openness and trust, were willing to be the primary resource persons in this final project. The contribution of data and time provided has become an invaluable empirical foundation for this research.</p>'),

    # Method pills
    (r'(<div class="method-pill">\s*<span class="mp-icon" aria-hidden="true">.*?</span>)\s*Structured Interview\s*</div>', r'\1 <span data-i18n="ack_meth_1">Structured Interview</span></div>'),
    (r'(<div class="method-pill">\s*<span class="mp-icon" aria-hidden="true">.*?</span>)\s*Expert Judgment\s*</div>', r'\1 <span data-i18n="ack_meth_2">Expert Judgment</span></div>'),
    (r'(<div class="method-pill">\s*<span class="mp-icon" aria-hidden="true">.*?</span>)\s*Focus Group Discussion\s*</div>', r'\1 <span data-i18n="ack_meth_3">Focus Group Discussion</span></div>'),
    (r'(<div class="method-pill">\s*<span class="mp-icon" aria-hidden="true">.*?</span>)\s*Participant Validation\s*</div>', r'\1 <span data-i18n="ack_meth_4">Participant Validation</span></div>'),
    (r'(<div class="method-pill">\s*<span class="mp-icon" aria-hidden="true">.*?</span>)\s*Supporting Documents\s*</div>', r'\1 <span data-i18n="ack_meth_5">Supporting Documents</span></div>'),

    # Colleagues Card
    (r'<p class="pc-label">\s*Bachelor\'s Thesis Partner\s*</p>', '<p class="pc-label" data-i18n="ack_pc_label">Bachelor\'s Thesis Partner</p>'),
    (r'<p class="pc-body">\s*Thank you to Miftahul Falah.*?truly valuable\s*academic experience\.\s*</p>', '<p class="pc-body" data-i18n="ack_pc_body">Thank you to Miftahul Falah for being an exceptional colleague throughout this final project. Your commitment to supporting one another amid various technical challenges, along with your consistent spirit of collaboration, has facilitated the smooth progress of this research and made it a truly valuable academic experience.</p>'),
    (r'(<span class="pc-badge">\s*<span class="pc-badge-dot" aria-hidden="true"></span>)\s*Fellow Colleague\s*</span>', r'\1 <span data-i18n="ack_pc_badge">Fellow Colleague</span></span>')
]

for pat, repl in regex_replacements:
    content = re.sub(pat, repl, content, flags=re.DOTALL)

# --- 2. Add translations ---
translations = {
    'en': {
        'menu_acknowledgment': 'Acknowledgment',
        'ack_sec_family': 'Family',
        'ack_sec_advisors': 'Advisors',
        'ack_sec_research_partners': 'Research Partners',
        'ack_sec_colleagues': 'Colleagues',
        'ack_fam_label': 'Primary Dedication',
        'ack_fam_title': 'Immediate & Extended Family',
        'ack_fam_body': 'Dedicated with deep gratitude to the author\'s <strong>immediate</strong> and <strong>extended family</strong>. The prayers that have always accompanied me, the moral guidance, and the boundless support have been the essential foundation that has enabled me to keep moving forward and complete this series of final thesis research projects to their fullest extent.',
        'ack_adv_role_1': 'First Advisor',
        'ack_adv_body_1': 'Thank you for your meticulous direction, patient guidance, and full dedication in mentoring the author from the beginning to the end of this final project. Every piece of advice provided has been an invaluable guiding light.',
        'ack_adv_tag_1': 'Academic Advisor',
        'ack_adv_role_2': 'Second Advisor',
        'ack_adv_body_2': 'Thank you for your deep academic insights, encouragement to always think critically, and highly helpful technical guidance in strengthening the methodology and analytical framework of this final project.',
        'ack_adv_tag_2': 'Technical Advisor',
        'ack_co_label': 'Resource Persons & Data Partners',
        'ack_co_body': 'Thank you to the entire management and IT division at <strong style="color:var(--slate)">DetereCo</strong> who, with full openness and trust, were willing to be the primary resource persons in this final project. The contribution of data and time provided has become an invaluable empirical foundation for this research.',
        'ack_meth_1': 'Structured Interview',
        'ack_meth_2': 'Expert Judgment',
        'ack_meth_3': 'Focus Group Discussion',
        'ack_meth_4': 'Participant Validation',
        'ack_meth_5': 'Supporting Documents',
        'ack_pc_label': 'Bachelor\'s Thesis Partner',
        'ack_pc_body': 'Thank you to Miftahul Falah for being an exceptional colleague throughout this final project. Your commitment to supporting one another amid various technical challenges, along with your consistent spirit of collaboration, has facilitated the smooth progress of this research and made it a truly valuable academic experience.',
        'ack_pc_badge': 'Fellow Colleague'
    },
    'id': {
        'menu_acknowledgment': 'Ucapan Terima Kasih',
        'ack_sec_family': 'Keluarga',
        'ack_sec_advisors': 'Pembimbing',
        'ack_sec_research_partners': 'Mitra Penelitian',
        'ack_sec_colleagues': 'Rekan',
        'ack_fam_label': 'Dedikasi Utama',
        'ack_fam_title': 'Keluarga Inti & Besar',
        'ack_fam_body': 'Didedikasikan dengan rasa syukur yang mendalam kepada <strong>keluarga inti</strong> dan <strong>keluarga besar</strong> penulis. Doa yang selalu menyertai, bimbingan moral, dan dukungan tanpa batas telah menjadi fondasi esensial yang memungkinkan saya untuk terus melangkah maju dan menyelesaikan rangkaian proyek penelitian skripsi ini dengan sebaik-baiknya.',
        'ack_adv_role_1': 'Pembimbing Pertama',
        'ack_adv_body_1': 'Terima kasih atas arahan yang teliti, bimbingan yang penuh kesabaran, dan dedikasi penuh dalam membimbing penulis dari awal hingga akhir tugas akhir ini. Setiap nasihat yang diberikan telah menjadi cahaya penuntun yang tak ternilai.',
        'ack_adv_tag_1': 'Pembimbing Akademik',
        'ack_adv_role_2': 'Pembimbing Kedua',
        'ack_adv_body_2': 'Terima kasih atas wawasan akademik yang mendalam, dorongan untuk selalu berpikir kritis, dan bimbingan teknis yang sangat membantu dalam memperkuat metodologi serta kerangka analitis tugas akhir ini.',
        'ack_adv_tag_2': 'Pembimbing Teknis',
        'ack_co_label': 'Narasumber & Mitra Data',
        'ack_co_body': 'Terima kasih kepada seluruh jajaran manajemen dan divisi TI di <strong style="color:var(--slate)">DetereCo</strong> yang dengan penuh keterbukaan dan kepercayaan bersedia menjadi narasumber utama dalam tugas akhir ini. Kontribusi data dan waktu yang diberikan telah menjadi landasan empiris yang tak ternilai bagi penelitian ini.',
        'ack_meth_1': 'Wawancara Terstruktur',
        'ack_meth_2': 'Penilaian Ahli',
        'ack_meth_3': 'Diskusi Kelompok Terpumpun',
        'ack_meth_4': 'Validasi Peserta',
        'ack_meth_5': 'Dokumen Pendukung',
        'ack_pc_label': 'Rekan Skripsi',
        'ack_pc_body': 'Terima kasih kepada Miftahul Falah karena telah menjadi rekan yang luar biasa sepanjang tugas akhir ini. Komitmen untuk saling mendukung di tengah berbagai tantangan teknis, bersama dengan semangat kolaborasi yang konsisten, telah memfasilitasi kelancaran penelitian ini dan menjadikannya pengalaman akademik yang sangat berharga.',
        'ack_pc_badge': 'Rekan Sejawat'
    },
    'es': {
        'menu_acknowledgment': 'Agradecimientos',
        'ack_sec_family': 'Familia',
        'ack_sec_advisors': 'Asesores',
        'ack_sec_research_partners': 'Socios de Investigación',
        'ack_sec_colleagues': 'Colegas',
        'ack_fam_label': 'Dedicación Principal',
        'ack_fam_title': 'Familia Directa y Extendida',
        'ack_fam_body': 'Dedicado con profunda gratitud a la <strong>familia directa</strong> y <strong>extendida</strong> del autor. Las oraciones que siempre me han acompañado, la guía moral y el apoyo incondicional han sido la base esencial que me ha permitido seguir adelante y completar esta serie de proyectos de investigación de tesis al máximo.',
        'ack_adv_role_1': 'Primer Asesor',
        'ack_adv_body_1': 'Gracias por su dirección meticulosa, orientación paciente y dedicación completa al asesorar al autor desde el principio hasta el final de este proyecto. Cada consejo proporcionado ha sido una luz guía invaluable.',
        'ack_adv_tag_1': 'Asesor Académico',
        'ack_adv_role_2': 'Segundo Asesor',
        'ack_adv_body_2': 'Gracias por sus profundos conocimientos académicos, aliento para pensar siempre críticamente y orientación técnica de gran ayuda para fortalecer la metodología y el marco analítico de este proyecto.',
        'ack_adv_tag_2': 'Asesor Técnico',
        'ack_co_label': 'Personas de Apoyo y Socios de Datos',
        'ack_co_body': 'Gracias a toda la gerencia y a la división de TI en <strong style="color:var(--slate)">DetereCo</strong> quienes, con total apertura y confianza, estuvieron dispuestos a ser los principales informantes en este proyecto. La contribución de datos y tiempo proporcionada se ha convertido en una base empírica invaluable para esta investigación.',
        'ack_meth_1': 'Entrevista Estructurada',
        'ack_meth_2': 'Juicio de Expertos',
        'ack_meth_3': 'Discusión de Grupo Focal',
        'ack_meth_4': 'Validación de Participantes',
        'ack_meth_5': 'Documentos de Respaldo',
        'ack_pc_label': 'Compañero de Tesis',
        'ack_pc_body': 'Gracias a Miftahul Falah por ser un colega excepcional a lo largo de este proyecto. Su compromiso de apoyarnos mutuamente en medio de diversos desafíos técnicos, junto con su constante espíritu de colaboración, ha facilitado el progreso de esta investigación y la ha convertido en una experiencia académica verdaderamente valiosa.',
        'ack_pc_badge': 'Colega'
    },
    'fr': {
        'menu_acknowledgment': 'Remerciements',
        'ack_sec_family': 'Famille',
        'ack_sec_advisors': 'Conseillers',
        'ack_sec_research_partners': 'Partenaires de Recherche',
        'ack_sec_colleagues': 'Collègues',
        'ack_fam_label': 'Dédicace Principale',
        'ack_fam_title': 'Famille Proche et Élargie',
        'ack_fam_body': 'Dédié avec une profonde gratitude à la <strong>famille proche</strong> et <strong>élargie</strong> de l\'auteur. Les prières qui m\'ont toujours accompagné, les conseils moraux et le soutien sans limite ont été la base essentielle qui m\'a permis de continuer à avancer et de mener à bien cette série de projets de recherche.',
        'ack_adv_role_1': 'Premier Conseiller',
        'ack_adv_body_1': 'Merci pour votre direction minutieuse, vos conseils patients et votre dévouement total à encadrer l\'auteur du début à la fin de ce projet. Chaque conseil fourni a été une lumière précieuse.',
        'ack_adv_tag_1': 'Conseiller Académique',
        'ack_adv_role_2': 'Deuxième Conseiller',
        'ack_adv_body_2': 'Merci pour vos profondes connaissances académiques, vos encouragements à toujours penser de manière critique, et vos conseils techniques très utiles pour renforcer la méthodologie et le cadre analytique de ce projet.',
        'ack_adv_tag_2': 'Conseiller Technique',
        'ack_co_label': 'Personnes Ressources et Partenaires de Données',
        'ack_co_body': 'Merci à l\'ensemble de la direction et à la division informatique de <strong style="color:var(--slate)">DetereCo</strong> qui, avec une ouverture d\'esprit et une confiance totales, ont bien voulu être les principales personnes ressources de ce projet. La contribution des données et du temps accordé est devenue une base empirique inestimable pour cette recherche.',
        'ack_meth_1': 'Entretien Structuré',
        'ack_meth_2': 'Jugement d\'Expert',
        'ack_meth_3': 'Discussion de Groupe (Focus Group)',
        'ack_meth_4': 'Validation des Participants',
        'ack_meth_5': 'Documents Justificatifs',
        'ack_pc_label': 'Partenaire de Thèse de Licence',
        'ack_pc_body': 'Merci à Miftahul Falah d\'avoir été un collègue exceptionnel tout au long de ce projet. Ton engagement à se soutenir mutuellement au milieu de divers défis techniques, ainsi que ton esprit de collaboration constant, ont facilité la progression de cette recherche et en ont fait une expérience académique véritablement précieuse.',
        'ack_pc_badge': 'Collègue'
    },
    'de': {
        'menu_acknowledgment': 'Danksagung',
        'ack_sec_family': 'Familie',
        'ack_sec_advisors': 'Betreuer',
        'ack_sec_research_partners': 'Forschungspartner',
        'ack_sec_colleagues': 'Kollegen',
        'ack_fam_label': 'Hauptwidmung',
        'ack_fam_title': 'Engere & erweiterte Familie',
        'ack_fam_body': 'Mit tiefer Dankbarkeit der <strong>engeren</strong> und <strong>erweiterten Familie</strong> des Autors gewidmet. Die Gebete, die mich stets begleitet haben, die moralische Führung und die grenzenlose Unterstützung waren das wesentliche Fundament, das es mir ermöglicht hat, weiter voranzukommen und diese Reihe von Abschlussarbeiten in vollem Umfang abzuschließen.',
        'ack_adv_role_1': 'Erster Betreuer',
        'ack_adv_body_1': 'Vielen Dank für Ihre sorgfältige Leitung, Ihre geduldige Führung und Ihr volles Engagement bei der Betreuung des Autors von Anfang bis Ende dieses Projekts. Jeder Ratschlag war ein unschätzbarer Wegweiser.',
        'ack_adv_tag_1': 'Akademischer Betreuer',
        'ack_adv_role_2': 'Zweiter Betreuer',
        'ack_adv_body_2': 'Vielen Dank für Ihre tiefen akademischen Einblicke, Ihre Ermutigung, stets kritisch zu denken, und Ihre äußerst hilfreiche technische Anleitung zur Stärkung der Methodik und des analytischen Rahmens dieses Projekts.',
        'ack_adv_tag_2': 'Technischer Betreuer',
        'ack_co_label': 'Auskunftspersonen & Datenpartner',
        'ack_co_body': 'Vielen Dank an das gesamte Management und die IT-Abteilung von <strong style="color:var(--slate)">DetereCo</strong>, die mit voller Offenheit und Vertrauen bereit waren, die wichtigsten Auskunftspersonen in diesem Projekt zu sein. Der Beitrag an Daten und Zeit ist zu einer unschätzbaren empirischen Grundlage für diese Forschung geworden.',
        'ack_meth_1': 'Strukturiertes Interview',
        'ack_meth_2': 'Expertenurteil',
        'ack_meth_3': 'Fokusgruppen-Diskussion',
        'ack_meth_4': 'Teilnehmervalidierung',
        'ack_meth_5': 'Unterstützende Dokumente',
        'ack_pc_label': 'Bachelorarbeitspartner',
        'ack_pc_body': 'Vielen Dank an Miftahul Falah, der während dieses gesamten Projekts ein außergewöhnlicher Kollege war. Dein Engagement, sich gegenseitig inmitten verschiedener technischer Herausforderungen zu unterstützen, zusammen mit deinem beständigen Geist der Zusammenarbeit, hat den reibungslosen Ablauf dieser Forschung erleichtert und sie zu einer wirklich wertvollen akademischen Erfahrung gemacht.',
        'ack_pc_badge': 'Kollege'
    },
    'zh': {
        'menu_acknowledgment': '致谢',
        'ack_sec_family': '家人',
        'ack_sec_advisors': '导师',
        'ack_sec_research_partners': '研究合作伙伴',
        'ack_sec_colleagues': '同事',
        'ack_fam_label': '主要奉献',
        'ack_fam_title': '直系与旁系亲属',
        'ack_fam_body': '怀着深深的感激之情，献给作者的 <strong>直系</strong> 和 <strong>旁系亲属</strong>。一直伴随我的祈祷、道德指引和无限的支持是我能够继续前进并充分完成这一系列毕业论文研究项目的重要基础。',
        'ack_adv_role_1': '第一导师',
        'ack_adv_body_1': '感谢您从本项目开始到结束对作者的悉心指导、耐心指引和全身心的投入。您提供的每一条建议都是宝贵的指路明灯。',
        'ack_adv_tag_1': '学术导师',
        'ack_adv_role_2': '第二导师',
        'ack_adv_body_2': '感谢您深刻的学术见解、鼓励我始终进行批判性思考，以及在加强本项目的立论方法和分析框架方面提供的极其有益的技术指导。',
        'ack_adv_tag_2': '技术导师',
        'ack_co_label': '受访人与数据合作伙伴',
        'ack_co_body': '感谢 <strong style="color:var(--slate)">DetereCo</strong> 的整个管理层和IT部门，他们以完全的开放和信任，愿意成为本项目的主要受访人。所提供的数据和时间的贡献已成为这项研究宝贵的实证基础。',
        'ack_meth_1': '结构化访谈',
        'ack_meth_2': '专家评审',
        'ack_meth_3': '焦点小组讨论',
        'ack_meth_4': '参与者验证',
        'ack_meth_5': '支持文件',
        'ack_pc_label': '学士论文伙伴',
        'ack_pc_body': '感谢 Miftahul Falah 在整个项目中成为一位出色的同事。您在各种技术挑战中相互支持的承诺，以及您一贯的合作精神，促进了这项研究的顺利进行，使其成为一次真正有价值的学术经历。',
        'ack_pc_badge': '同事'
    },
    'ja': {
        'menu_acknowledgment': '謝辞',
        'ack_sec_family': '家族',
        'ack_sec_advisors': '指導教員',
        'ack_sec_research_partners': '研究パートナー',
        'ack_sec_colleagues': '同僚',
        'ack_fam_label': '主な献身',
        'ack_fam_title': '直系および親戚',
        'ack_fam_body': '著者の<strong>直系の家族</strong>と<strong>親戚</strong>に深い感謝を込めて捧げます。常に私に寄り添ってくれた祈り、道徳的な指導、そして無限の支援は、私が前進し続け、この一連の卒業論文研究プロジェクトを最大限に完了させるための重要な基盤となりました。',
        'ack_adv_role_1': '第一指導教員',
        'ack_adv_body_1': 'この最終プロジェクトの始まりから終わりまで、著者を指導する上でのあなたの細心の注意、忍耐強い指導、そして完全な献身に感謝します。提供されたすべてのアドバイスは貴重な道標となりました。',
        'ack_adv_tag_1': '学術指導教員',
        'ack_adv_role_2': '第二指導教員',
        'ack_adv_body_2': 'あなたの深い学術的洞察力、常に批判的に考えるようにとの励まし、そしてこの最終プロジェクトの方法論と分析フレームワークを強化する上での非常に役立つ技術的指導に感謝します。',
        'ack_adv_tag_2': '技術指導教員',
        'ack_co_label': '情報提供者とデータパートナー',
        'ack_co_body': '<strong style="color:var(--slate)">DetereCo</strong> の経営陣とIT部門の皆様に感謝します。完全な開放性と信頼をもって、この最終プロジェクトの主要な情報提供者となることを快諾してくださいました。提供されたデータと時間の貢献は、この研究にとって貴重な実証的基盤となりました。',
        'ack_meth_1': '構造化面接',
        'ack_meth_2': '専門家の判断',
        'ack_meth_3': 'フォーカスグループディスカッション',
        'ack_meth_4': '参加者の検証',
        'ack_meth_5': 'サポートドキュメント',
        'ack_pc_label': '学士論文パートナー',
        'ack_pc_body': 'この最終プロジェクトを通じて並外れた同僚であったMiftahul Falahに感謝します。さまざまな技術的課題の中で互いを支え合うというあなたのコミットメントは、あなたの首尾一貫した協力の精神とともに、この研究の円滑な進行を促進し、それを真に価値のある学術的経験にしました。',
        'ack_pc_badge': '同僚'
    },
    'ko': {
        'menu_acknowledgment': '감사 인사',
        'ack_sec_family': '가족',
        'ack_sec_advisors': '지도 교수',
        'ack_sec_research_partners': '연구 파트너',
        'ack_sec_colleagues': '동료',
        'ack_fam_label': '주요 헌신',
        'ack_fam_title': '직계 및 방계 가족',
        'ack_fam_body': '저자의 <strong>직계</strong> 및 <strong>방계 가족</strong>에게 깊은 감사를 드립니다. 항상 저와 함께 해주신 기도, 도덕적 지도, 무한한 지원은 제가 계속 앞으로 나아가고 이 학사 논문 연구 프로젝트를 성공적으로 마칠 수 있게 해준 필수적인 기반이 되었습니다.',
        'ack_adv_role_1': '제1 지도 교수',
        'ack_adv_body_1': '이 최종 프로젝트의 처음부터 끝까지 저자를 지도하는 데 있어 꼼꼼한 지시, 인내심 있는 지도, 온전한 헌신에 감사드립니다. 제공해 주신 모든 조언은 귀중한 길잡이가 되었습니다.',
        'ack_adv_tag_1': '학술 지도 교수',
        'ack_adv_role_2': '제2 지도 교수',
        'ack_adv_body_2': '깊은 학술적 통찰력, 항상 비판적으로 생각하도록 격려해주신 점, 그리고 이 프로젝트의 방법론과 분석 프레임워크를 강화하는 데 있어 매우 유용한 기술적 지도에 감사드립니다.',
        'ack_adv_tag_2': '기술 지도 교수',
        'ack_co_label': '정보 제공자 및 데이터 파트너',
        'ack_co_body': '이 최종 프로젝트에서 전적인 개방성과 신뢰를 바탕으로 주요 정보 제공자가 기꺼이 되어주신 <strong style="color:var(--slate)">DetereCo</strong>의 전체 경영진과 IT 부서에 감사드립니다. 제공된 데이터와 시간의 기여는 이 연구에 대한 귀중한 경험적 기반이 되었습니다.',
        'ack_meth_1': '구조화된 인터뷰',
        'ack_meth_2': '전문가 판단',
        'ack_meth_3': '포커스 그룹 토론',
        'ack_meth_4': '참가자 검증',
        'ack_meth_5': '지원 문서',
        'ack_pc_label': '학사 논문 파트너',
        'ack_pc_body': '이 최종 프로젝트 내내 훌륭한 동료가 되어준 Miftahul Falah에게 감사합니다. 다양한 기술적 문제 속에서 서로를 지원하겠다는 당신의 헌신과 일관된 협력 정신은 이 연구가 원활하게 진행되도록 도왔으며 이를 진정으로 가치 있는 학술적 경험으로 만들었습니다.',
        'ack_pc_badge': '동료'
    },
    'ar': {
        'menu_acknowledgment': 'شكر وتقدير',
        'ack_sec_family': 'العائلة',
        'ack_sec_advisors': 'المستشارون',
        'ack_sec_research_partners': 'شركاء البحث',
        'ack_sec_colleagues': 'الزملاء',
        'ack_fam_label': 'الإهداء الرئيسي',
        'ack_fam_title': 'العائلة المباشرة والممتدة',
        'ack_fam_body': 'مُهدى بامتنان عميق إلى <strong>عائلة المؤلف المباشرة</strong> و<strong>الممتدة</strong>. إن الدعوات التي رافقتني دائمًا، والتوجيه الأخلاقي، والدعم اللامحدود كانت الأساس المتين الذي مكنني من المضي قدمًا وإكمال هذه السلسلة من مشاريع البحث الجامعية على أكمل وجه.',
        'ack_adv_role_1': 'المستشار الأول',
        'ack_adv_body_1': 'أشكرك على توجيهاتك الدقيقة، وإرشادك الصبور، وتفانيك الكامل في توجيه المؤلف من بداية هذا المشروع النهائي حتى نهايته. كل نصيحة قُدمت كانت ضوءًا هاديًا لا يقدر بثمن.',
        'ack_adv_tag_1': 'المستشار الأكاديمي',
        'ack_adv_role_2': 'المستشار الثاني',
        'ack_adv_body_2': 'أشكرك على رؤيتك الأكاديمية العميقة، وتشجيعك على التفكير النقدي دائمًا، وتوجيهاتك الفنية المفيدة للغاية في تعزيز المنهجية والإطار التحليلي لهذا المشروع النهائي.',
        'ack_adv_tag_2': 'المستشار الفني',
        'ack_co_label': 'الأشخاص المرجعيون وشركاء البيانات',
        'ack_co_body': 'أشكر جميع أفراد الإدارة وقسم تكنولوجيا المعلومات في <strong style="color:var(--slate)">DetereCo</strong> الذين كانوا مستعدين، بكل انفتاح وثقة، ليكونوا المصادر الرئيسية للمعلومات في هذا المشروع النهائي. أصبحت مساهمة البيانات والوقت المقدم أساسًا تجريبيًا لا يقدر بثمن لهذا البحث.',
        'ack_meth_1': 'مقابلة منظمة',
        'ack_meth_2': 'حكم الخبراء',
        'ack_meth_3': 'نقاش مجموعة التركيز (Focus Group)',
        'ack_meth_4': 'تحقق المشاركين',
        'ack_meth_5': 'المستندات الداعمة',
        'ack_pc_label': 'شريك أطروحة البكالوريوس',
        'ack_pc_body': 'أشكر مفتاح الفلاح لكونه زميلًا استثنائيًا طوال هذا المشروع النهائي. إن التزامك بدعم بعضنا البعض وسط التحديات الفنية المختلفة، إلى جانب روح التعاون المتسقة، قد سهل التقدم السلس لهذا البحث وجعله تجربة أكاديمية قيمة حقًا.',
        'ack_pc_badge': 'زميل'
    },
    'ru': {
        'menu_acknowledgment': 'Благодарности',
        'ack_sec_family': 'Семья',
        'ack_sec_advisors': 'Научные Руководители',
        'ack_sec_research_partners': 'Партнеры по Исследованию',
        'ack_sec_colleagues': 'Коллеги',
        'ack_fam_label': 'Главное Посвящение',
        'ack_fam_title': 'Близкие и Родственники',
        'ack_fam_body': 'Посвящается с глубокой благодарностью <strong>близким</strong> и <strong>дальним родственникам</strong> автора. Молитвы, которые всегда сопровождали меня, моральное руководство и безграничная поддержка были той необходимой основой, которая позволила мне продолжать двигаться вперед и завершить эту серию исследовательских проектов в полной мере.',
        'ack_adv_role_1': 'Первый Руководитель',
        'ack_adv_body_1': 'Спасибо за Ваше скрупулезное руководство, терпеливое наставничество и полную самоотдачу в наставничестве автора с начала до конца этого финального проекта. Каждый предоставленный совет был бесценным путеводным светом.',
        'ack_adv_tag_1': 'Академический Руководитель',
        'ack_adv_role_2': 'Второй Руководитель',
        'ack_adv_body_2': 'Спасибо за Ваше глубокое академическое понимание, поощрение всегда мыслить критически и весьма полезное техническое руководство в укреплении методологии и аналитической базы этого финального проекта.',
        'ack_adv_tag_2': 'Технический Руководитель',
        'ack_co_label': 'Информаторы и Партнеры по Данным',
        'ack_co_body': 'Спасибо всему руководству и ИТ-отделу в <strong style="color:var(--slate)">DetereCo</strong>, которые с полной открытостью и доверием согласились стать основными информаторами в этом финальном проекте. Предоставленные данные и уделенное время стали бесценной эмпирической основой для этого исследования.',
        'ack_meth_1': 'Структурированное Интервью',
        'ack_meth_2': 'Экспертная Оценка',
        'ack_meth_3': 'Обсуждение в Фокус-Группе',
        'ack_meth_4': 'Валидация Участниками',
        'ack_meth_5': 'Подтверждающие Документы',
        'ack_pc_label': 'Партнер по Дипломной Работе',
        'ack_pc_body': 'Спасибо Мифтахулу Фалаху за то, что он был исключительным коллегой на протяжении всего этого финального проекта. Твое стремление поддерживать друг друга среди различных технических проблем, наряду с твоим последовательным духом сотрудничества, способствовало плавному ходу этого исследования и сделало его поистине ценным академическим опытом.',
        'ack_pc_badge': 'Коллега'
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

print("Done acknowledgments translations")
