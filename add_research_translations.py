import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

en_text = """# Research Overview

---

## Research Questions

1. How can a cybersecurity risk profile for critical corporate assets at DetereCo be developed by conducting a gap analysis based on the company's existing mitigation measures?
2. How can an integrated risk management model be designed by mapping identified priority cybersecurity risks to COBIT 2019 governance practices (APO12 & EDM03) using the standard process flow of ISO 27005?
3. How can risk treatment recommendations be designed based on the technical principles of Zero Trust Architecture and the security controls of ISO 27002 to effectively mitigate modern threats in the aerospace industry?

---

## Research Objectives

1. To produce a comprehensive cybersecurity risk profile for critical corporate assets at DetereCo. This profile is compiled based on the results of a gap analysis between existing mitigation measures and the cyber threat landscape faced by the defense and aerospace industries.
2. To develop a risk mitigation model that conceptually maps identified priority risks to COBIT 2019 governance practices (APO12 & EDM03).
3. Develop recommendations for a risk treatment model based on the technical principles of Zero Trust Architecture and mapped to the ISO/IEC 27002:2022 security controls to mitigate the priority risks that have been identified.

---

## Company / *Industry*

**DetereCo** / *Aerospace Manufacturing Industry*

---

## Frameworks Used

| Framework | Reference |
|---|---|
| COBIT 2019 | [Link Access](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [Link Access](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [Link Access](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [Link Access](https://www.iso.org/standard/80585.html) |

---

## Problem-Solving Methodology

**Design Science Research** by Peffers et al., 2007 — [Link Access](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## List of Expert Judgments

- IT Planning & Strategy Manager at DetereCo
- IT Governance & Risk Supervisor at DetereCo
- IT Infrastructure & Security Manager at DetereCo
- IT Security Supervisor at DetereCo
- Infrastructure Management Supervisor at DetereCo
- Researcher at Telkom University
- Consulting Manager at PT. Perisai Digital Indonesia (Cisometric)
- IT Security Risk at PT. Citilink Indonesia
- Sr. IT GRC Consultant at PT. Perisai Digital Indonesia (Cisometric)

---

## The 5-Layer Zero Trust Defense Model

![The 5-Layer Zero Trust Defense Model](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### Layer Descriptions

| Components | Description |
|---|---|
| **ZTA Control Plane** | The "brain" of the architecture that aggregates real-time telemetry to calculate dynamic risk scores and issue adaptive access decisions. |
| **Identity Layer** | The outermost defense that establishes trust using PKI-based MFA and continuous device health checks to mitigate identity-based threats. |
| **Application Layer** | Secures critical workloads such as ERP systems by strictly enforcing the Principle of Least Privilege to prevent unauthorized horizontal access. |
| **Network Layer** | Enforces micro-segmentation, mTLS encryption, and IT/OT boundary inspection to prevent ransomware spread and lateral movement. |
| **Infrastructure Layer** | Applies strict host isolation to separate environments and maintains a hardened runtime for VMs, containers, and IoT devices. |
| **Data Layer** | Protects the "Crown Jewels" (ERP records, access rights, CAD designs) from exfiltration through robust encryption and strict access controls. |"""

id_text = """# Tinjauan Penelitian

---

## Pertanyaan Penelitian

1. Bagaimana profil risiko keamanan siber untuk aset perusahaan penting di DetereCo dapat dikembangkan dengan melakukan analisis kesenjangan berdasarkan langkah-langkah mitigasi yang ada di perusahaan?
2. Bagaimana model manajemen risiko terintegrasi dapat dirancang dengan memetakan risiko keamanan siber prioritas yang diidentifikasi ke praktik tata kelola COBIT 2019 (APO12 & EDM03) menggunakan alur proses standar ISO 27005?
3. Bagaimana rekomendasi penanganan risiko dapat dirancang berdasarkan prinsip teknis Zero Trust Architecture dan kontrol keamanan ISO 27002 untuk secara efektif memitigasi ancaman modern di industri kedirgantaraan?

---

## Tujuan Penelitian

1. Untuk menghasilkan profil risiko keamanan siber yang komprehensif untuk aset perusahaan penting di DetereCo. Profil ini disusun berdasarkan hasil analisis kesenjangan antara langkah-langkah mitigasi yang ada dan lanskap ancaman siber yang dihadapi oleh industri pertahanan dan kedirgantaraan.
2. Untuk mengembangkan model mitigasi risiko yang secara konseptual memetakan risiko prioritas yang diidentifikasi ke praktik tata kelola COBIT 2019 (APO12 & EDM03).
3. Mengembangkan rekomendasi untuk model penanganan risiko berdasarkan prinsip teknis Zero Trust Architecture dan dipetakan ke kontrol keamanan ISO/IEC 27002:2022 untuk memitigasi risiko prioritas yang telah diidentifikasi.

---

## Perusahaan / *Industri*

**DetereCo** / *Industri Manufaktur Kedirgantaraan*

---

## Kerangka Kerja yang Digunakan

| Kerangka Kerja | Referensi |
|---|---|
| COBIT 2019 | [Akses Tautan](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [Akses Tautan](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [Akses Tautan](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [Akses Tautan](https://www.iso.org/standard/80585.html) |

---

## Metodologi Pemecahan Masalah

**Design Science Research** oleh Peffers dkk., 2007 — [Akses Tautan](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## Daftar Penilaian Ahli

- Manajer Perencanaan & Strategi TI di DetereCo
- Supervisor Tata Kelola & Risiko TI di DetereCo
- Manajer Infrastruktur & Keamanan TI di DetereCo
- Supervisor Keamanan TI di DetereCo
- Supervisor Manajemen Infrastruktur di DetereCo
- Peneliti di Universitas Telkom
- Manajer Konsultan di PT. Perisai Digital Indonesia (Cisometric)
- Risiko Keamanan TI di PT. Citilink Indonesia
- Konsultan Senior GRC TI di PT. Perisai Digital Indonesia (Cisometric)

---

## Model Pertahanan 5 Lapis Zero Trust

![Model Pertahanan 5 Lapis Zero Trust](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### Deskripsi Lapis

| Komponen | Deskripsi |
|---|---|
| **Control Plane ZTA** | "Otak" dari arsitektur yang mengumpulkan telemetri waktu nyata untuk menghitung skor risiko dinamis dan mengeluarkan keputusan akses adaptif. |
| **Lapisan Identitas** | Pertahanan terluar yang membangun kepercayaan menggunakan MFA berbasis PKI dan pemeriksaan kesehatan perangkat berkelanjutan untuk memitigasi ancaman berbasis identitas. |
| **Lapisan Aplikasi** | Mengamankan beban kerja kritis seperti sistem ERP dengan secara ketat menegakkan Prinsip Hak Istimewa Terkecil (Principle of Least Privilege) untuk mencegah akses horizontal yang tidak sah. |
| **Lapisan Jaringan** | Menegakkan segmentasi mikro, enkripsi mTLS, dan inspeksi batas IT/OT untuk mencegah penyebaran ransomware dan pergerakan lateral. |
| **Lapisan Infrastruktur** | Menerapkan isolasi host yang ketat untuk memisahkan lingkungan dan memelihara runtime yang diperkeras untuk VM, kontainer, dan perangkat IoT. |
| **Lapisan Data** | Melindungi "Permata Mahkota" (catatan ERP, hak akses, desain CAD) dari eksfiltrasi melalui enkripsi yang kuat dan kontrol akses yang ketat. |"""

zh_text = """# 研究概述

---

## 研究问题

1. 如何通过基于公司现有缓解措施进行差距分析，为DetereCo的关键企业资产制定网络安全风险状况？
2. 如何通过使用ISO 27005的标准流程，将识别出的优先网络安全风险映射到COBIT 2019治理实践（APO12和EDM03），从而设计集成风险管理模型？
3. 如何基于零信任架构的技术原则和ISO 27002的安全控制设计风险处理建议，以有效缓解航空航天行业的现代威胁？

---

## 研究目标

1. 为DetereCo的关键企业资产制定全面的网络安全风险状况。该概况基于现有缓解措施与国防和航空航天行业面临的网络威胁格局之间的差距分析结果编制。
2. 开发一个风险缓解模型，在概念上将识别出的优先风险映射到COBIT 2019治理实践（APO12和EDM03）。
3. 制定基于零信任架构技术原则的风险处理模型建议，并将其映射到ISO/IEC 27002:2022安全控制，以缓解已识别的优先风险。

---

## 公司 / *行业*

**DetereCo** / *航空航天制造行业*

---

## 使用的框架

| 框架 | 参考 |
|---|---|
| COBIT 2019 | [链接访问](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [链接访问](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [链接访问](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [链接访问](https://www.iso.org/standard/80585.html) |

---

## 解决问题的方法

Peffers等人的**设计科学研究**，2007年 — [链接访问](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## 专家评审名单

- DetereCo IT规划与战略经理
- DetereCo IT治理与风险主管
- DetereCo IT基础设施与安全经理
- DetereCo IT安全主管
- DetereCo 基础设施管理主管
- 泰尔科姆大学研究员
- PT. Perisai Digital Indonesia (Cisometric) 咨询经理
- PT. Citilink Indonesia IT安全风险
- PT. Perisai Digital Indonesia (Cisometric) 高级IT GRC顾问

---

## 5层零信任防御模型

![5层零信任防御模型](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### 层描述

| 组件 | 描述 |
|---|---|
| **ZTA控制平面** | 架构的“大脑”，聚合实时遥测数据以计算动态风险评分并发布自适应访问决策。 |
| **身份层** | 最外层防御，使用基于PKI的MFA和连续设备健康检查建立信任，以缓解基于身份的威胁。 |
| **应用层** | 通过严格执行最小特权原则保护关键工作负载（如ERP系统），以防止未经授权的横向访问。 |
| **网络层** | 执行微分段、mTLS加密和IT/OT边界检查，以防止勒索软件传播和横向移动。 |
| **基础设施层** | 应用严格的主机隔离来分离环境，并为VM、容器和IoT设备维护强化的运行环境。 |
| **数据层** | 通过强大的加密和严格的访问控制保护“皇冠明珠”（ERP记录、访问权限、CAD设计）免遭数据泄露。 |"""

es_text = """# Resumen de la Investigación

---

## Preguntas de Investigación

1. ¿Cómo se puede desarrollar un perfil de riesgo de ciberseguridad para los activos corporativos críticos en DetereCo realizando un análisis de brechas basado en las medidas de mitigación existentes de la empresa?
2. ¿Cómo se puede diseñar un modelo de gestión de riesgos integrado mapeando los riesgos de ciberseguridad prioritarios identificados con las prácticas de gobierno de COBIT 2019 (APO12 y EDM03) utilizando el flujo de proceso estándar de ISO 27005?
3. ¿Cómo se pueden diseñar recomendaciones de tratamiento de riesgos basadas en los principios técnicos de la Arquitectura Zero Trust y los controles de seguridad de ISO 27002 para mitigar eficazmente las amenazas modernas en la industria aeroespacial?

---

## Objetivos de la Investigación

1. Producir un perfil de riesgo de ciberseguridad integral para los activos corporativos críticos en DetereCo. Este perfil se elabora a partir de los resultados de un análisis de brechas entre las medidas de mitigación existentes y el panorama de amenazas cibernéticas que enfrentan las industrias de defensa y aeroespacial.
2. Desarrollar un modelo de mitigación de riesgos que mapee conceptualmente los riesgos prioritarios identificados con las prácticas de gobierno de COBIT 2019 (APO12 y EDM03).
3. Desarrollar recomendaciones para un modelo de tratamiento de riesgos basado en los principios técnicos de la Arquitectura Zero Trust y mapeado con los controles de seguridad ISO/IEC 27002:2022 para mitigar los riesgos prioritarios que han sido identificados.

---

## Empresa / *Industria*

**DetereCo** / *Industria de Fabricación Aeroespacial*

---

## Marcos Utilizados

| Marco | Referencia |
|---|---|
| COBIT 2019 | [Acceso al Enlace](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [Acceso al Enlace](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [Acceso al Enlace](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [Acceso al Enlace](https://www.iso.org/standard/80585.html) |

---

## Metodología de Resolución de Problemas

**Design Science Research** por Peffers et al., 2007 — [Acceso al Enlace](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## Lista de Juicios de Expertos

- Gerente de Planificación y Estrategia de TI en DetereCo
- Supervisor de Gobierno y Riesgo de TI en DetereCo
- Gerente de Infraestructura y Seguridad de TI en DetereCo
- Supervisor de Seguridad de TI en DetereCo
- Supervisor de Gestión de Infraestructura en DetereCo
- Investigador en Telkom University
- Gerente de Consultoría en PT. Perisai Digital Indonesia (Cisometric)
- Riesgo de Seguridad de TI en PT. Citilink Indonesia
- Consultor Sr. de TI GRC en PT. Perisai Digital Indonesia (Cisometric)

---

## El Modelo de Defensa Zero Trust de 5 Capas

![El Modelo de Defensa Zero Trust de 5 Capas](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### Descripciones de Capas

| Componentes | Descripción |
|---|---|
| **Plano de Control ZTA** | El "cerebro" de la arquitectura que agrega telemetría en tiempo real para calcular puntuaciones de riesgo dinámicas y emitir decisiones de acceso adaptativas. |
| **Capa de Identidad** | La defensa más externa que establece la confianza utilizando MFA basado en PKI y verificaciones continuas del estado del dispositivo para mitigar amenazas basadas en identidad. |
| **Capa de Aplicación** | Asegura cargas de trabajo críticas, como sistemas ERP, aplicando estrictamente el Principio de Privilegio Mínimo para evitar accesos horizontales no autorizados. |
| **Capa de Red** | Impone microsegmentación, cifrado mTLS e inspección de límites IT/OT para evitar la propagación de ransomware y movimientos laterales. |
| **Capa de Infraestructura** | Aplica un aislamiento de host estricto para separar entornos y mantiene un tiempo de ejecución fortalecido para máquinas virtuales, contenedores y dispositivos IoT. |
| **Capa de Datos** | Protege las "Joyas de la Corona" (registros ERP, derechos de acceso, diseños CAD) de la exfiltración a través de un cifrado sólido y controles de acceso estrictos. |"""

fr_text = """# Aperçu de la Recherche

---

## Questions de Recherche

1. Comment développer un profil de risque de cybersécurité pour les actifs de l'entreprise critiques chez DetereCo en effectuant une analyse des écarts basée sur les mesures d'atténuation existantes de l'entreprise ?
2. Comment concevoir un modèle de gestion intégrée des risques en associant les risques de cybersécurité prioritaires identifiés aux pratiques de gouvernance COBIT 2019 (APO12 & EDM03) en utilisant le flux de processus standard d'ISO 27005 ?
3. Comment concevoir des recommandations de traitement des risques basées sur les principes techniques de l'Architecture Zero Trust et les contrôles de sécurité d'ISO 27002 pour atténuer efficacement les menaces modernes dans l'industrie aérospatiale ?

---

## Objectifs de Recherche

1. Produire un profil complet des risques de cybersécurité pour les actifs de l'entreprise critiques chez DetereCo. Ce profil est compilé sur la base des résultats d'une analyse des écarts entre les mesures d'atténuation existantes et le paysage des cybermenaces auquel sont confrontées les industries de la défense et de l'aérospatiale.
2. Développer un modèle d'atténuation des risques qui associe conceptuellement les risques prioritaires identifiés aux pratiques de gouvernance COBIT 2019 (APO12 & EDM03).
3. Élaborer des recommandations pour un modèle de traitement des risques basé sur les principes techniques de l'Architecture Zero Trust et associé aux contrôles de sécurité ISO/IEC 27002:2022 pour atténuer les risques prioritaires qui ont été identifiés.

---

## Entreprise / *Industrie*

**DetereCo** / *Industrie de Fabrication Aérospatiale*

---

## Cadres Utilisés

| Cadre | Référence |
|---|---|
| COBIT 2019 | [Accès au Lien](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [Accès au Lien](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [Accès au Lien](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [Accès au Lien](https://www.iso.org/standard/80585.html) |

---

## Méthodologie de Résolution de Problèmes

**Design Science Research** par Peffers et al., 2007 — [Accès au Lien](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## Liste des Jugements d'Experts

- Responsable Planification & Stratégie Informatique chez DetereCo
- Superviseur Gouvernance & Risque Informatique chez DetereCo
- Responsable Infrastructure & Sécurité Informatique chez DetereCo
- Superviseur Sécurité Informatique chez DetereCo
- Superviseur Gestion des Infrastructures chez DetereCo
- Chercheur à l'Université de Telkom
- Responsable Conseil chez PT. Perisai Digital Indonesia (Cisometric)
- Risque Sécurité Informatique chez PT. Citilink Indonesia
- Consultant Senior IT GRC chez PT. Perisai Digital Indonesia (Cisometric)

---

## Le Modèle de Défense Zero Trust à 5 Couches

![Le Modèle de Défense Zero Trust à 5 Couches](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### Descriptions des Couches

| Composants | Description |
|---|---|
| **Plan de Contrôle ZTA** | Le "cerveau" de l'architecture qui regroupe la télémétrie en temps réel pour calculer des scores de risque dynamiques et émettre des décisions d'accès adaptatives. |
| **Couche d'Identité** | La défense la plus externe qui établit la confiance à l'aide de l'AMF basée sur l'IGC et de contrôles continus de l'état des appareils pour atténuer les menaces liées à l'identité. |
| **Couche d'Application** | Sécurise les charges de travail critiques telles que les systèmes ERP en appliquant strictement le Principe du Moindre Privilège pour empêcher tout accès horizontal non autorisé. |
| **Couche Réseau** | Applique la micro-segmentation, le cryptage mTLS et l'inspection des limites IT/OT pour empêcher la propagation de ransomwares et les mouvements latéraux. |
| **Couche d'Infrastructure** | Applique une isolation stricte des hôtes pour séparer les environnements et maintient un environnement d'exécution renforcé pour les machines virtuelles, les conteneurs et les appareils IoT. |
| **Couche de Données** | Protège les "Joyaux de la Couronne" (enregistrements ERP, droits d'accès, conceptions CAO) de l'exfiltration via un cryptage robuste et des contrôles d'accès stricts. |"""

de_text = """# Forschungsüberblick

---

## Forschungsfragen

1. Wie kann ein Cybersicherheitsrisikoprofil für kritische Unternehmenswerte bei DetereCo durch Durchführung einer Lückenanalyse basierend auf den bestehenden Minderungsmaßnahmen des Unternehmens entwickelt werden?
2. Wie kann ein integriertes Risikomanagementmodell entworfen werden, indem identifizierte priorisierte Cybersicherheitsrisiken auf COBIT 2019-Governance-Praktiken (APO12 & EDM03) unter Verwendung des Standardprozessablaufs nach ISO 27005 abgebildet werden?
3. Wie können Empfehlungen zur Risikobehandlung basierend auf den technischen Prinzipien der Zero Trust-Architektur und den Sicherheitskontrollen nach ISO 27002 entworfen werden, um moderne Bedrohungen in der Luft- und Raumfahrtindustrie wirksam zu mindern?

---

## Forschungsziele

1. Erstellung eines umfassenden Cybersicherheitsrisikoprofils für kritische Unternehmenswerte bei DetereCo. Dieses Profil wird basierend auf den Ergebnissen einer Lückenanalyse zwischen bestehenden Minderungsmaßnahmen und der Cyber-Bedrohungslandschaft der Verteidigungs- und Raumfahrtindustrie erstellt.
2. Entwicklung eines Risikominderungsmodells, das identifizierte priorisierte Risiken konzeptionell auf COBIT 2019-Governance-Praktiken (APO12 & EDM03) abbildet.
3. Entwicklung von Empfehlungen für ein Risikobehandlungsmodell basierend auf den technischen Prinzipien der Zero Trust-Architektur und Abbildung auf die ISO/IEC 27002:2022-Sicherheitskontrollen, um die identifizierten priorisierten Risiken zu mindern.

---

## Unternehmen / *Branche*

**DetereCo** / *Luft- und Raumfahrtfertigungsindustrie*

---

## Verwendete Frameworks

| Framework | Referenz |
|---|---|
| COBIT 2019 | [Link-Zugriff](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [Link-Zugriff](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [Link-Zugriff](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [Link-Zugriff](https://www.iso.org/standard/80585.html) |

---

## Problemlösungsmethodik

**Design Science Research** von Peffers et al., 2007 — [Link-Zugriff](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## Liste der Expertenurteile

- IT Planungs- & Strategiemanager bei DetereCo
- IT Governance & Risikosupervisor bei DetereCo
- IT Infrastruktur- & Sicherheitsmanager bei DetereCo
- IT Sicherheitssupervisor bei DetereCo
- Infrastrukturmanagement-Supervisor bei DetereCo
- Forscher an der Universität Telkom
- Beratungsmanager bei PT. Perisai Digital Indonesia (Cisometric)
- IT Sicherheitsrisiko bei PT. Citilink Indonesia
- Sr. IT GRC Berater bei PT. Perisai Digital Indonesia (Cisometric)

---

## Das 5-Schichten Zero Trust Verteidigungsmodell

![Das 5-Schichten Zero Trust Verteidigungsmodell](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### Schichtbeschreibungen

| Komponenten | Beschreibung |
|---|---|
| **ZTA-Kontrollebene** | Das "Gehirn" der Architektur, das Echtzeit-Telemetrie aggregiert, um dynamische Risikobewertungen zu berechnen und adaptive Zugriffsentscheidungen zu treffen. |
| **Identitätsschicht** | Die äußerste Verteidigung, die durch PKI-basierte MFA und kontinuierliche Zustandsprüfungen von Geräten Vertrauen aufbaut, um identitätsbasierte Bedrohungen zu mindern. |
| **Anwendungsschicht** | Sichert kritische Workloads wie ERP-Systeme durch strikte Durchsetzung des Prinzips der geringsten Privilegien, um unbefugten horizontalen Zugriff zu verhindern. |
| **Netzwerkschicht** | Erzwingt Mikrosegmentierung, mTLS-Verschlüsselung und IT/OT-Grenzkontrollen, um die Ausbreitung von Ransomware und laterale Bewegungen zu verhindern. |
| **Infrastrukturschicht** | Wendet strikte Host-Isolation zur Trennung von Umgebungen an und unterhält eine gehärtete Laufzeit für VMs, Container und IoT-Geräte. |
| **Datenschicht** | Schützt die "Kronjuwelen" (ERP-Aufzeichnungen, Zugriffsrechte, CAD-Designs) vor Exfiltration durch robuste Verschlüsselung und strikte Zugriffskontrollen. |"""

ar_text = """# نظرة عامة على البحث

---

## أسئلة البحث

1. كيف يمكن تطوير ملف تعريف مخاطر الأمن السيبراني للأصول المؤسسية الحيوية في DetereCo عن طريق إجراء تحليل الفجوات استنادًا إلى تدابير التخفيف الحالية للشركة؟
2. كيف يمكن تصميم نموذج متكامل لإدارة المخاطر عن طريق تعيين مخاطر الأمن السيبراني ذات الأولوية المحددة لممارسات حوكمة COBIT 2019 (APO12 و EDM03) باستخدام تدفق العمليات القياسي لـ ISO 27005؟
3. كيف يمكن تصميم توصيات معالجة المخاطر استنادًا إلى المبادئ الفنية لبنية انعدام الثقة (Zero Trust Architecture) وضوابط الأمان الخاصة بـ ISO 27002 للتخفيف بشكل فعال من التهديدات الحديثة في صناعة الطيران؟

---

## أهداف البحث

1. إنتاج ملف تعريف شامل لمخاطر الأمن السيبراني للأصول المؤسسية الحيوية في DetereCo. يتم تجميع هذا الملف الشخصي بناءً على نتائج تحليل الفجوات بين تدابير التخفيف الحالية ومشهد التهديدات السيبرانية الذي تواجهه صناعات الدفاع والطيران.
2. تطوير نموذج للتخفيف من المخاطر يعين مفاهيميًا المخاطر ذات الأولوية المحددة لممارسات حوكمة COBIT 2019 (APO12 و EDM03).
3. تطوير توصيات لنموذج معالجة المخاطر بناءً على المبادئ الفنية لبنية انعدام الثقة (Zero Trust Architecture) وتعيينها لضوابط أمان ISO/IEC 27002:2022 للتخفيف من المخاطر ذات الأولوية التي تم تحديدها.

---

## الشركة / *الصناعة*

**DetereCo** / *صناعة تصنيع الطيران والفضاء*

---

## الأطر المستخدمة

| الإطار | المرجع |
|---|---|
| COBIT 2019 | [رابط الوصول](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [رابط الوصول](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [رابط الوصول](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [رابط الوصول](https://www.iso.org/standard/80585.html) |

---

## منهجية حل المشكلات

**Design Science Research** بواسطة Peffers et al., 2007 — [رابط الوصول](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## قائمة أحكام الخبراء

- مدير التخطيط الاستراتيجي وتكنولوجيا المعلومات في DetereCo
- مشرف حوكمة تقنية المعلومات والمخاطر في DetereCo
- مدير البنية التحتية وأمن تكنولوجيا المعلومات في DetereCo
- مشرف أمن تكنولوجيا المعلومات في DetereCo
- مشرف إدارة البنية التحتية في DetereCo
- باحث في جامعة Telkom
- مدير الاستشارات في PT. Perisai Digital Indonesia (Cisometric)
- مخاطر أمن تكنولوجيا المعلومات في PT. Citilink Indonesia
- مستشار أول لتكنولوجيا المعلومات GRC في PT. Perisai Digital Indonesia (Cisometric)

---

## نموذج الدفاع المكون من 5 طبقات لانعدام الثقة

![نموذج الدفاع المكون من 5 طبقات لانعدام الثقة](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### أوصاف الطبقات

| المكونات | الوصف |
|---|---|
| **مستوى التحكم ZTA** | "عقل" البنية الذي يجمع بيانات القياس عن بُعد في الوقت الفعلي لحساب درجات المخاطر الديناميكية وإصدار قرارات وصول تكيفية. |
| **طبقة الهوية** | الدفاع الخارجي الذي يؤسس الثقة باستخدام المصادقة متعددة العوامل القائمة على PKI والفحوصات المستمرة لصحة الجهاز للتخفيف من التهديدات القائمة على الهوية. |
| **طبقة التطبيقات** | تؤمن أعباء العمل الحرجة مثل أنظمة ERP من خلال فرض مبدأ الامتياز الأقل بصرامة لمنع الوصول الأفقي غير المصرح به. |
| **طبقة الشبكة** | تفرض التجزئة الدقيقة، وتشفير mTLS، وفحص حدود IT/OT لمنع انتشار برامج الفدية والحركة الجانبية. |
| **طبقة البنية التحتية** | تطبق عزلاً صارمًا للمضيف لفصل البيئات وتحافظ على بيئة تشغيل مقواة للأجهزة الافتراضية والحاويات وأجهزة إنترنت الأشياء. |
| **طبقة البيانات** | تحمي "جواهر التاج" (سجلات ERP، حقوق الوصول، تصميمات CAD) من التسريب من خلال التشفير القوي وضوابط الوصول الصارمة. |"""

ru_text = """# Обзор исследования

---

## Исследовательские вопросы

1. Как можно разработать профиль риска кибербезопасности для критически важных корпоративных активов в DetereCo путем проведения анализа пробелов на основе существующих мер по снижению рисков компании?
2. Как можно разработать интегрированную модель управления рисками путем сопоставления выявленных приоритетных рисков кибербезопасности с практиками управления COBIT 2019 (APO12 и EDM03) с использованием стандартного процесса ISO 27005?
3. Как можно разработать рекомендации по обработке рисков на основе технических принципов Архитектуры нулевого доверия и средств управления безопасностью ISO 27002 для эффективного снижения современных угроз в аэрокосмической промышленности?

---

## Цели исследования

1. Создать всеобъемлющий профиль риска кибербезопасности для критически важных корпоративных активов в DetereCo. Этот профиль составлен на основе результатов анализа пробелов между существующими мерами по снижению рисков и ландшафтом киберугроз, с которыми сталкиваются оборонная и аэрокосмическая отрасли.
2. Разработать модель снижения рисков, которая концептуально сопоставляет выявленные приоритетные риски с практиками управления COBIT 2019 (APO12 и EDM03).
3. Разработать рекомендации для модели обработки рисков на основе технических принципов Архитектуры нулевого доверия (Zero Trust Architecture) и сопоставить их со средствами управления безопасностью ISO/IEC 27002:2022 для снижения приоритетных рисков, которые были выявлены.

---

## Компания / *Отрасль*

**DetereCo** / *Аэрокосмическая промышленность*

---

## Используемые фреймворки

| Фреймворк | Ссылка |
|---|---|
| COBIT 2019 | [Доступ по ссылке](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [Доступ по ссылке](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [Доступ по ссылке](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [Доступ по ссылке](https://www.iso.org/standard/80585.html) |

---

## Методология решения проблем

**Design Science Research** от Peffers et al., 2007 — [Доступ по ссылке](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## Список экспертных оценок

- Менеджер по ИТ-планированию и стратегии в DetereCo
- Руководитель по ИТ-управлению и рискам в DetereCo
- Менеджер по ИТ-инфраструктуре и безопасности в DetereCo
- Руководитель ИТ-безопасности в DetereCo
- Руководитель по управлению инфраструктурой в DetereCo
- Исследователь в Университете Telkom
- Менеджер по консалтингу в PT. Perisai Digital Indonesia (Cisometric)
- ИТ-риски безопасности в PT. Citilink Indonesia
- Старший ИТ GRC Консультант в PT. Perisai Digital Indonesia (Cisometric)

---

## 5-уровневая модель защиты нулевого доверия

![5-уровневая модель защиты нулевого доверия](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### Описание уровней

| Компоненты | Описание |
|---|---|
| **Уровень управления ZTA** | «Мозг» архитектуры, который собирает телеметрию в реальном времени для расчета динамических оценок риска и принятия адаптивных решений о доступе. |
| **Уровень идентификации** | Внешняя защита, которая устанавливает доверие с использованием MFA на основе PKI и непрерывных проверок работоспособности устройств для снижения угроз, основанных на идентификации. |
| **Прикладной уровень** | Защищает критические рабочие нагрузки, такие как системы ERP, путем строгого соблюдения принципа наименьших привилегий для предотвращения несанкционированного горизонтального доступа. |
| **Сетевой уровень** | Применяет микросегментацию, шифрование mTLS и проверку границ IT/OT для предотвращения распространения программ-вымогателей и бокового перемещения. |
| **Инфраструктурный уровень** | Применяет строгую изоляцию хостов для разделения сред и поддерживает защищенную среду выполнения для ВМ, контейнеров и устройств Интернета вещей. |
| **Уровень данных** | Защищает «Королевские драгоценности» (записи ERP, права доступа, проекты CAD) от эксфильтрации с помощью надежного шифрования и строгого контроля доступа. |"""

ko_text = """# 연구 개요

---

## 연구 질문

1. 회사의 기존 완화 조치를 기반으로 격차 분석을 수행하여 DetereCo의 중요한 기업 자산에 대한 사이버 보안 위험 프로필을 어떻게 개발할 수 있습니까?
2. ISO 27005의 표준 프로세스 흐름을 사용하여 파악된 우선순위 사이버 보안 위험을 COBIT 2019 거버넌스 관행(APO12 및 EDM03)에 매핑하여 통합 위험 관리 모델을 어떻게 설계할 수 있습니까?
3. 항공 우주 산업의 현대적 위협을 효과적으로 완화하기 위해 제로 트러스트 아키텍처(Zero Trust Architecture)의 기술 원칙과 ISO 27002의 보안 통제를 기반으로 위험 처리 권장 사항을 어떻게 설계할 수 있습니까?

---

## 연구 목표

1. DetereCo의 중요한 기업 자산에 대한 포괄적인 사이버 보안 위험 프로필을 생성합니다. 이 프로필은 기존 완화 조치와 국방 및 항공 우주 산업이 직면한 사이버 위협 환경 간의 격차 분석 결과를 바탕으로 작성됩니다.
2. 식별된 우선순위 위험을 COBIT 2019 거버넌스 관행(APO12 및 EDM03)에 개념적으로 매핑하는 위험 완화 모델을 개발합니다.
3. 식별된 우선순위 위험을 완화하기 위해 제로 트러스트 아키텍처의 기술 원칙에 기반하고 ISO/IEC 27002:2022 보안 통제에 매핑된 위험 처리 모델에 대한 권장 사항을 개발합니다.

---

## 회사 / *산업*

**DetereCo** / *항공 우주 제조 산업*

---

## 사용된 프레임워크

| 프레임워크 | 참조 |
|---|---|
| COBIT 2019 | [링크 액세스](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [링크 액세스](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [링크 액세스](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [링크 액세스](https://www.iso.org/standard/80585.html) |

---

## 문제 해결 방법론

**Design Science Research** by Peffers et al., 2007 — [링크 액세스](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## 전문가 판단 목록

- DetereCo의 IT 기획 및 전략 관리자
- DetereCo의 IT 거버넌스 및 위험 감독관
- DetereCo의 IT 인프라 및 보안 관리자
- DetereCo의 IT 보안 감독관
- DetereCo의 인프라 관리 감독관
- 텔콤 대학교 연구원
- PT. Perisai Digital Indonesia (Cisometric)의 컨설팅 관리자
- PT. Citilink Indonesia의 IT 보안 위험
- PT. Perisai Digital Indonesia (Cisometric)의 수석 IT GRC 컨설턴트

---

## 5계층 제로 트러스트 방어 모델

![5계층 제로 트러스트 방어 모델](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### 계층 설명

| 구성 요소 | 설명 |
|---|---|
| **ZTA 제어 평면** | 실시간 원격 분석을 집계하여 동적 위험 점수를 계산하고 적응형 액세스 결정을 내리는 아키텍처의 "두뇌"입니다. |
| **ID 계층** | PKI 기반 MFA 및 지속적인 디바이스 상태 확인을 사용하여 신뢰를 구축하여 ID 기반 위협을 완화하는 최외곽 방어선입니다. |
| **애플리케이션 계층** | 최소 권한의 원칙을 엄격하게 시행하여 무단 수평 액세스를 방지함으로써 ERP 시스템과 같은 중요한 워크로드를 보호합니다. |
| **네트워크 계층** | 마이크로 세분화, mTLS 암호화 및 IT/OT 경계 검사를 적용하여 랜섬웨어 확산 및 측면 이동을 방지합니다. |
| **인프라 계층** | 엄격한 호스트 격리를 적용하여 환경을 분리하고 VM, 컨테이너 및 IoT 디바이스에 대해 강화된 런타임을 유지합니다. |
| **데이터 계층** | 강력한 암호화 및 엄격한 액세스 제어를 통해 데이터 유출로부터 "크라운 주얼"(ERP 기록, 액세스 권한, CAD 설계)을 보호합니다. |"""

ja_text = """# 研究概要

---

## 研究の課題

1. 自社の既存の緩和策に基づいたギャップ分析を実施することにより、DetereCoの重要な企業資産に対するサイバーセキュリティリスクプロファイルをどのように構築できるか。
2. ISO 27005の標準プロセスフローを使用して、特定された優先サイバーセキュリティリスクをCOBIT 2019ガバナンス実践 (APO12およびEDM03) にマッピングすることにより、統合リスク管理モデルをどのように設計できるか。
3. 航空宇宙産業における現代の脅威を効果的に緩和するために、ゼロトラストアーキテクチャの技術原則とISO 27002のセキュリティコントロールに基づいて、リスク対応の推奨事項をどのように設計できるか。

---

## 研究の目的

1. DetereCoの重要な企業資産の包括的なサイバーセキュリティリスクプロファイルを作成すること。このプロファイルは、既存の緩和策と防衛および航空宇宙産業が直面するサイバー脅威の状況との間のギャップ分析の結果に基づいて作成されます。
2. 特定された優先リスクをCOBIT 2019ガバナンス実践 (APO12およびEDM03) に概念的にマッピングするリスク緩和モデルを開発すること。
3. 特定された優先リスクを緩和するために、ゼロトラストアーキテクチャの技術原則に基づいており、ISO/IEC 27002:2022のセキュリティコントロールにマッピングされたリスク対応モデルの推奨事項を作成すること。

---

## 会社 / *業界*

**DetereCo** / *航空宇宙製造業*

---

## 使用されたフレームワーク

| フレームワーク | 参考 |
|---|---|
| COBIT 2019 | [リンクアクセス](https://www.isaca.org/resources/cobit) |
| NIST SP 800-207 | [リンクアクセス](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf) |
| ISO/IEC 27002:2022 | [リンクアクセス](https://www.iso.org/standard/75652.html) |
| ISO/IEC 27005:2022 | [リンクアクセス](https://www.iso.org/standard/80585.html) |

---

## 問題解決手法

Peffersらによる**Design Science Research**、2007年 — [リンクアクセス](https://www.researchgate.net/publication/284503626_A_design_science_research_methodology_for_information_systems_research)

---

## 専門家判断のリスト

- DetereCoのIT企画＆戦略マネージャー
- DetereCoのITガバナンス＆リスクスーパーバイザー
- DetereCoのITインフラ＆セキュリティマネージャー
- DetereCoのITセキュリティスーパーバイザー
- DetereCoのインフラ管理スーパーバイザー
- テルコム大学の研究者
- PT. Perisai Digital Indonesia (Cisometric) のコンサルティングマネージャー
- PT. Citilink IndonesiaのITセキュリティリスク
- PT. Perisai Digital Indonesia (Cisometric) のシニアIT GRCコンサルタント

---

## 5層ゼロトラスト防御モデル

![5層ゼロトラスト防御モデル](5%20Layer%20ZTA%20PNG%20BAG.drawio.png)

### 各層の説明

| コンポーネント | 説明 |
|---|---|
| **ZTAコントロールプレーン** | リアルタイムのテレメトリを集約して動的なリスクスコアを計算し、適応型のアクセス決定を下すアーキテクチャの「頭脳」。 |
| **アイデンティティ層** | PKIベースのMFAと継続的なデバイスヘルスチェックを使用して信頼を確立し、アイデンティティに基づく脅威を緩和する最前線の防御。 |
| **アプリケーション層** | 許可されていない水平アクセスを防止するために、最小権限の原則を厳格に適用することにより、ERPシステムなどの重要なワークロードを保護します。 |
| **ネットワーク層** | マイクロセグメンテーション、mTLS暗号化、およびIT/OT境界検査を適用して、ランサムウェアの拡散とラテラルムーブメントを防止します。 |
| **インフラストラクチャ層** | 環境を分離するために厳密なホスト分離を適用し、VM、コンテナ、およびIoTデバイスの強化されたランタイムを維持します。 |
| **データ層** | 強固な暗号化と厳格なアクセス制御を通じて、「クラウンジュエル」 (ERPレコード、アクセス権、CAD設計) を外部への持ち出しから保護します。 |"""


all_texts = {
    "en": en_text,
    "id": id_text,
    "zh": zh_text,
    "es": es_text,
    "fr": fr_text,
    "de": de_text,
    "ar": ar_text,
    "ru": ru_text,
    "ko": ko_text,
    "ja": ja_text
}

# The embeddedMarkdown format requires it to be serialized as a JSON string inside the JS object?
# No, in index.html, it's defined like this:
#     const embeddedMarkdown = {
#       research: {
#         "en": `...`
#       },
# We can format it nicely.
new_research_block = "      research: {\n"
for lang, txt in all_texts.items():
    # Make sure we don't break template literals by escaping backticks
    txt = txt.replace('`', '\\`')
    new_research_block += f'        "{lang}": `{txt}`,\n'
new_research_block += "      },"

# Find the block and replace it
match = re.search(r'      research: \{\n        "en": `.*?`\n      \},', content, re.DOTALL)
if match:
    content = content[:match.start()] + new_research_block + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added all 10 language translations for research block.")
else:
    print("Could not find the research block to replace.")

