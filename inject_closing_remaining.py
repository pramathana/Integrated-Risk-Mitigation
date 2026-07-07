import re

file_path = "c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML with data-i18n attributes
html_regex_replacements = [
    (r'<div class="closing-item-title">\s*ZTA Tenets & ISO 27002 Translation\s*</div>', '<div class="closing-item-title" data-i18n="closing_item_zta_title">ZTA Tenets & ISO 27002 Translation</div>'),
    (r'<div class="closing-item-desc">\s*Risk treatment recommendations were successfully designed by mapping the.*?mitigate modern threats in a\s*structured manner\.</div>', '<div class="closing-item-desc" data-i18n="closing_item_zta_desc">Risk treatment recommendations were successfully designed by mapping the root causes of governance issues to the <strong>7 fundamental principles (Tenets) of Zero Trust Architecture</strong>. To make them practical, these ZTA principles were translated into technical security controls from <strong>ISO/IEC 27002:2022</strong> (such as control 8.12 Data Leakage Prevention, 8.22 Segregation of Networks, 8.5 Secure Authentication, etc.). These recommendations are classified using the <strong>5-Layer Zero Trust Defense Model</strong> to mitigate modern threats in a structured manner.</div>')
]

for pat, repl in html_regex_replacements:
    content = re.sub(pat, repl, content, flags=re.DOTALL)

# 2. Add translations
translations = {
    'en': {
        'menu_closing': 'Closing',
        'closing_item_zta_title': 'ZTA Tenets & ISO 27002 Translation',
        'closing_item_zta_desc': 'Risk treatment recommendations were successfully designed by mapping the root causes of governance issues to the <strong>7 fundamental principles (Tenets) of Zero Trust Architecture</strong>. To make them practical, these ZTA principles were translated into technical security controls from <strong>ISO/IEC 27002:2022</strong> (such as control 8.12 Data Leakage Prevention, 8.22 Segregation of Networks, 8.5 Secure Authentication, etc.). These recommendations are classified using the <strong>5-Layer Zero Trust Defense Model</strong> to mitigate modern threats in a structured manner.'
    },
    'id': {
        'menu_closing': 'Penutup',
        'closing_item_zta_title': 'Prinsip ZTA & Terjemahan ISO 27002',
        'closing_item_zta_desc': 'Rekomendasi perlakuan risiko berhasil dirancang dengan memetakan akar penyebab masalah tata kelola ke <strong>7 prinsip fundamental (Tenets) dari Zero Trust Architecture</strong>. Agar praktis, prinsip-prinsip ZTA ini diterjemahkan ke dalam kontrol keamanan teknis dari <strong>ISO/IEC 27002:2022</strong> (seperti kontrol 8.12 Data Leakage Prevention, 8.22 Segregation of Networks, 8.5 Secure Authentication, dll.). Rekomendasi ini diklasifikasikan menggunakan <strong>Model Pertahanan Zero Trust 5-Lapis</strong> untuk memitigasi ancaman modern secara terstruktur.'
    },
    'es': {
        'menu_closing': 'Cierre',
        'closing_item_zta_title': 'Principios ZTA y Traducción ISO 27002',
        'closing_item_zta_desc': 'Las recomendaciones de tratamiento de riesgos se diseñaron con éxito al mapear las causas subyacentes de los problemas de gobernanza con los <strong>7 principios fundamentales de la Arquitectura de Confianza Cero</strong>. Para hacerlos prácticos, estos principios ZTA se tradujeron en controles de seguridad técnicos de <strong>ISO/IEC 27002:2022</strong> (como el control 8.12 Prevención de Fuga de Datos, 8.22 Segregación de Redes, 8.5 Autenticación Segura, etc.). Estas recomendaciones se clasifican utilizando el <strong>Modelo de Defensa de Confianza Cero de 5 Capas</strong> para mitigar las amenazas modernas de manera estructurada.'
    },
    'fr': {
        'menu_closing': 'Clôture',
        'closing_item_zta_title': 'Principes ZTA et Traduction ISO 27002',
        'closing_item_zta_desc': 'Les recommandations de traitement des risques ont été conçues avec succès en mappant les causes profondes des problèmes de gouvernance aux <strong>7 principes fondamentaux de la Zero Trust Architecture</strong>. Pour les rendre pratiques, ces principes ZTA ont été traduits en contrôles de sécurité techniques à partir de la norme <strong>ISO/IEC 27002:2022</strong> (tels que le contrôle 8.12 Prévention des Fuites de Données, 8.22 Ségrégation des Réseaux, 8.5 Authentification Sécurisée, etc.). Ces recommandations sont classées à l\'aide du <strong>Modèle de Défense Zero Trust à 5 Couches</strong> pour atténuer les menaces modernes de manière structurée.'
    },
    'de': {
        'menu_closing': 'Abschluss',
        'closing_item_zta_title': 'ZTA-Prinzipien & ISO 27002-Übersetzung',
        'closing_item_zta_desc': 'Risikobehandlungsempfehlungen wurden erfolgreich entworfen, indem die Grundursachen von Governance-Problemen auf die <strong>7 Grundprinzipien der Zero Trust Architecture</strong> abgebildet wurden. Um sie praktikabel zu machen, wurden diese ZTA-Prinzipien in technische Sicherheitskontrollen der <strong>ISO/IEC 27002:2022</strong> übersetzt (z. B. Kontrolle 8.12 Data Leakage Prevention, 8.22 Segregation of Networks, 8.5 Secure Authentication usw.). Diese Empfehlungen werden anhand des <strong>5-Schichten-Zero-Trust-Verteidigungsmodells</strong> klassifiziert, um moderne Bedrohungen strukturiert abzuwehren.'
    },
    'zh': {
        'menu_closing': '结论',
        'closing_item_zta_title': 'ZTA 原则与 ISO 27002 转换',
        'closing_item_zta_desc': '通过将治理问题的根本原因映射到 <strong>零信任架构的 7 个基本原则</strong>，成功设计了风险处理建议。为了使其具有实用性，这些 ZTA 原则被转换为 <strong>ISO/IEC 27002:2022</strong> 中的技术安全控制（如控制 8.12 数据防泄露，8.22 网络隔离，8.5 安全身份验证等）。使用 <strong>5 层零信任防御模型</strong>对这些建议进行分类，以结构化的方式缓解现代威胁。'
    },
    'ja': {
        'menu_closing': '結論',
        'closing_item_zta_title': 'ZTAの原則とISO 27002の変換',
        'closing_item_zta_desc': 'ガバナンス問題の根本原因を<strong>ゼロトラストアーキテクチャの7つの基本原則</strong>にマッピングすることにより、リスク対応の推奨事項が正常に設計されました。実用的にするために、これらのZTAの原則は<strong>ISO/IEC 27002:2022</strong>の技術的セキュリティ管理（管理8.12データ漏えい防止、8.22ネットワークの分離、8.5安全な認証など）に変換されました。これらの推奨事項は、現代の脅威を構造化された方法で軽減するために、<strong>5層ゼロトラスト防御モデル</strong>を使用して分類されています。'
    },
    'ko': {
        'menu_closing': '결론',
        'closing_item_zta_title': 'ZTA 원칙 및 ISO 27002 변환',
        'closing_item_zta_desc': '거버넌스 문제의 근본 원인을 <strong>제로 트러스트 아키텍처의 7가지 기본 원칙</strong>에 매핑하여 위험 처리 권장 사항을 성공적으로 설계했습니다. 이를 실용적으로 만들기 위해 이러한 ZTA 원칙은 <strong>ISO/IEC 27002:2022</strong>의 기술적 보안 통제(예: 통제 8.12 데이터 유출 방지, 8.22 네트워크 분리, 8.5 보안 인증 등)로 변환되었습니다. 이러한 권장 사항은 구조화된 방식으로 현대적 위협을 완화하기 위해 <strong>5계층 제로 트러스트 방어 모델</strong>을 사용하여 분류됩니다.'
    },
    'ar': {
        'menu_closing': 'الختام',
        'closing_item_zta_title': 'مبادئ ZTA وترجمة ISO 27002',
        'closing_item_zta_desc': 'تم تصميم توصيات معالجة المخاطر بنجاح من خلال تعيين الأسباب الجذرية لمشاكل الحوكمة إلى <strong>المبادئ الأساسية السبعة لهندسة انعدام الثقة (ZTA)</strong>. لجعلها عملية، تمت ترجمة مبادئ ZTA هذه إلى ضوابط أمنية فنية من <strong>ISO/IEC 27002:2022</strong> (مثل التحكم 8.12 منع تسرب البيانات، 8.22 فصل الشبكات، 8.5 المصادقة الآمنة، إلخ). تُصنف هذه التوصيات باستخدام <strong>نموذج دفاع انعدام الثقة المكون من 5 طبقات</strong> للتخفيف من التهديدات الحديثة بطريقة منظمة.'
    },
    'ru': {
        'menu_closing': 'Заключение',
        'closing_item_zta_title': 'Принципы ZTA и Перевод ISO 27002',
        'closing_item_zta_desc': 'Рекомендации по обработке рисков были успешно разработаны путем сопоставления основных причин проблем управления с <strong>7 фундаментальными принципами архитектуры нулевого доверия</strong>. Чтобы сделать их практичными, эти принципы ZTA были переведены в технические средства контроля безопасности из <strong>ISO/IEC 27002:2022</strong> (такие как контроль 8.12 Предотвращение утечки данных, 8.22 Разделение сетей, 8.5 Безопасная аутентификация и т. д.). Эти рекомендации классифицируются с использованием <strong>5-уровневой модели защиты с нулевым доверием</strong> для структурированного снижения современных угроз.'
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

print("Done remaining parts")
