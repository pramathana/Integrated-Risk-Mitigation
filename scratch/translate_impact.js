const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, '../index.html');
let content = fs.readFileSync(filePath, 'utf8');

const impactTranslations = {
  "id": `## 2. Skala Dampak
**Sumber:** ISO 27005:2022; Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI); dan Templat Formulir Penilaian Aset TI DetereCo

> **Nilai Buku Aset** = Harga Perolehan Aset − Akumulasi Penyusutan/Penurunan Nilai
> Dihitung dari aset yang terdampak langsung.

| Skala | Kategori | Infrastruktur & Sistem Aplikasi | Dampak Finansial | Dampak Operasional |
|:---:|---|---|---|---|
| **1** | Minor | Aplikasi & infrastruktur pendukung yang kurang kritis<br>tidak berfungsi selama **1 hari**<br>*(mis., absensi karyawan, situs web, printer, portal SDM)* | < 1% dari nilai buku aset | Operasi berjalan pada 97% ≤ X < 100%.<br>Pulih pada hari yang sama.<br>Konsekuensi dampak dapat diabaikan.<br>Perusahaan dapat mengatasinya tanpa banyak kesulitan. |
| **2** | Signifikan | Aplikasi & infrastruktur pendukung yang kurang kritis<br>tidak berfungsi selama **lebih dari 1 hari hingga 3 hari**<br>*(mis., absensi karyawan, situs web, printer, portal SDM)* | 1% hingga 5% dari nilai buku aset | Operasi berjalan pada 93% ≤ X < 97%.<br>Pemulihan penuh dalam maksimum 2 hari kerja.<br>Mempengaruhi kinerja aktivitas.<br>Perusahaan menghadapi beberapa kesulitan. |
| **3** | Serius | Aplikasi dan infrastruktur vital yang penting<br>tidak berfungsi (Downtime) selama **< 1 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | 5.1% hingga 10% dari nilai buku aset | Operasi berjalan pada 90% ≤ X < 93%.<br>Pemulihan penuh antara 2–7 hari kerja.<br>Penurunan kinerja utama terkait keamanan data penting.<br>Perusahaan menghadapi komplikasi yang dapat dikelola. |
| **4** | Kritis | Aplikasi dan infrastruktur vital yang penting<br>tidak berfungsi (Downtime) selama **> 1 jam hingga 6 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | 11% hingga 15% dari nilai buku aset | Operasi berjalan pada 80% ≤ X < 90%.<br>Pemulihan penuh dalam 8–15 hari kerja.<br>Dampak serius dan hilangnya sebagian data rahasia kritis.<br>Perusahaan mengalami kesulitan serius. |
| **5** | Bencana | Infrastruktur vital yang penting tidak berfungsi (Downtime)<br>selama **lebih dari 6 jam**<br>*(mis., listrik, air, jaringan komunikasi, sistem keamanan & sistem online)* | > 15% dari nilai buku aset | Operasi berjalan pada X < 80%.<br>Pemulihan penuh > 15 hari kerja.<br>Dampak yang sangat parah dan hilangnya semua data rahasia kritis.<br>Perusahaan mengalami kesulitan yang sangat parah dan fatal. |

---`,
  "zh": `## 2. 影响等级
**来源:** ISO 27005:2022; DetereCo 内部程序 (IT 风险管理实施); 以及 DetereCo IT 资产评估表模板

> **资产账面价值** = 资产收购价格 − 累计折旧/减值
> 根据直接受影响的资产计算。

| 等级 | 类别 | 基础设施和应用系统 | 财务影响 | 运营影响 |
|:---:|---|---|---|---|
| **1** | 轻微 | 较不关键的支持应用和基础设施<br>停止运行 **1天**<br>*(例如：员工考勤，网站，打印机，人力资源门户)* | < 资产账面价值的 1% | 运营保持在 97% ≤ X < 100%。<br>当天恢复。<br>影响后果可以忽略不计。<br>公司可以毫不费力地克服它。 |
| **2** | 显著 | 较不关键的支持应用和基础设施<br>停止运行 **1天以上至3天**<br>*(例如：员工考勤，网站，打印机，人力资源门户)* | 资产账面价值的 1% 至 5% | 运营保持在 93% ≤ X < 97%。<br>最多2个工作日内全面恢复。<br>影响活动表现。<br>公司面临一些困难。 |
| **3** | 严重 | 重要的关键应用和基础设施<br>停止运行（停机）**< 1小时**<br>*(例如：电力，水，通信网络，安全系统和在线系统)* | 资产账面价值的 5.1% 至 10% | 运营保持在 90% ≤ X < 93%。<br>在2-7个工作日内全面恢复。<br>涉及重要数据安全的性能大幅下降。<br>公司面临可控的并发症。 |
| **4** | 危急 | 重要的关键应用和基础设施<br>停止运行（停机）**> 1小时至6小时**<br>*(例如：电力，水，通信网络，安全系统和在线系统)* | 资产账面价值的 11% 至 15% | 运营保持在 80% ≤ X < 90%。<br>在8-15个工作日内全面恢复。<br>严重影响并丢失部分关键机密数据。<br>公司遇到严重困难。 |
| **5** | 灾难性 | 重要的关键基础设施停止运行（停机）<br>**超过6小时**<br>*(例如：电力，水，通信网络，安全系统和在线系统)* | > 资产账面价值的 15% | 运营保持在 X < 80%。<br>全面恢复 > 15个工作日。<br>极其严重的影响并丢失所有关键机密数据。<br>公司遇到非常严重和致命的困难。 |

---`,
  "es": `## 2. Escala de Impacto
**Fuente:** ISO 27005:2022; Procedimientos Internos de DetereCo (Implementación de Gestión de Riesgos de TI); y la Plantilla del Formulario de Evaluación de Activos de TI de DetereCo

> **Valor Contable del Activo** = Precio de Adquisición del Activo − Depreciación/Deterioro Acumulado
> Calculado a partir de los activos directamente afectados.

| Escala | Categoría | Infraestructura y Sistemas de Aplicaciones | Impacto Financiero | Impacto Operativo |
|:---:|---|---|---|---|
| **1** | Menor | Aplicaciones de soporte e infraestructura menos críticas<br>sin funcionar durante **1 día**<br>*(por ejemplo, asistencia de empleados, sitio web, impresora, portal de recursos humanos)* | < 1% del valor contable del activo | Las operaciones funcionan al 97% ≤ X < 100%.<br>Se recupera el mismo día.<br>Las consecuencias del impacto son insignificantes.<br>La empresa puede superarlo sin mucha dificultad. |
| **2** | Significativo | Aplicaciones de soporte e infraestructura menos críticas<br>sin funcionar durante **más de 1 día hasta 3 días**<br>*(por ejemplo, asistencia de empleados, sitio web, impresora, portal de recursos humanos)* | 1% a 5% del valor contable del activo | Las operaciones funcionan al 93% ≤ X < 97%.<br>Recuperación total en un máximo de 2 días hábiles.<br>Afecta el rendimiento de la actividad.<br>La empresa enfrenta algunas dificultades. |
| **3** | Grave | Aplicaciones e infraestructura vitales importantes<br>sin funcionar (Tiempo de inactividad) por **< 1 hora**<br>*(por ejemplo, electricidad, agua, redes de comunicación, sistemas de seguridad y sistemas en línea)* | 5.1% a 10% del valor contable del activo | Las operaciones funcionan al 90% ≤ X < 93%.<br>Recuperación total entre 2 y 7 días hábiles.<br>Fuerte caída del rendimiento en relación con la seguridad de datos importantes.<br>La empresa enfrenta complicaciones manejables. |
| **4** | Crítico | Aplicaciones e infraestructura vitales importantes<br>sin funcionar (Tiempo de inactividad) por **> 1 hora hasta 6 horas**<br>*(por ejemplo, electricidad, agua, redes de comunicación, sistemas de seguridad y sistemas en línea)* | 11% a 15% del valor contable del activo | Las operaciones funcionan al 80% ≤ X < 90%.<br>Recuperación total en 8-15 días hábiles.<br>Impacto grave y pérdida parcial de datos confidenciales críticos.<br>La empresa experimenta graves dificultades. |
| **5** | Catastrófico | Infraestructura vital importante sin funcionar (Tiempo de inactividad)<br>por **más de 6 horas**<br>*(por ejemplo, electricidad, agua, redes de comunicación, sistemas de seguridad y sistemas en línea)* | > 15% del valor contable del activo | Las operaciones funcionan a X < 80%.<br>Recuperación total > 15 días hábiles.<br>Impacto extremadamente grave y pérdida de todos los datos confidenciales críticos.<br>La empresa experimenta dificultades muy graves y fatales. |

---`,
  "fr": `## 2. Échelle d'Impact
**Source :** ISO 27005:2022 ; Procédures Internes de DetereCo (Mise en Œuvre de la Gestion des Risques Informatiques) ; et le Modèle de Formulaire d'Évaluation des Actifs Informatiques de DetereCo

> **Valeur Comptable de l'Actif** = Prix d'Acquisition de l'Actif − Amortissement/Dépréciation Cumulé
> Calculé à partir des actifs directement impactés.

| Échelle | Catégorie | Infrastructure et Systèmes d'Application | Impact Financier | Impact Opérationnel |
|:---:|---|---|---|---|
| **1** | Mineur | Applications de support et infrastructure moins critiques<br>ne fonctionnant pas pendant **1 jour**<br>*(ex., présence des employés, site web, imprimante, portail RH)* | < 1% de la valeur comptable de l'actif | Les opérations fonctionnent à 97% ≤ X < 100%.<br>Récupère le même jour.<br>Les conséquences de l'impact sont négligeables.<br>L'entreprise peut le surmonter sans grande difficulté. |
| **2** | Significatif | Applications de support et infrastructure moins critiques<br>ne fonctionnant pas pendant **plus d'1 jour jusqu'à 3 jours**<br>*(ex., présence des employés, site web, imprimante, portail RH)* | 1% à 5% de la valeur comptable de l'actif | Les opérations fonctionnent à 93% ≤ X < 97%.<br>Récupération complète en 2 jours ouvrables maximum.<br>Affecte les performances des activités.<br>L'entreprise fait face à certaines difficultés. |
| **3** | Grave | Applications et infrastructures vitales importantes<br>ne fonctionnant pas (Temps d'arrêt) pendant **< 1 heure**<br>*(ex., électricité, eau, réseaux de communication, systèmes de sécurité & systèmes en ligne)* | 5.1% à 10% de la valeur comptable de l'actif | Les opérations fonctionnent à 90% ≤ X < 93%.<br>Récupération complète entre 2 et 7 jours ouvrables.<br>Baisse majeure des performances concernant la sécurité des données importantes.<br>L'entreprise fait face à des complications gérables. |
| **4** | Critique | Applications et infrastructures vitales importantes<br>ne fonctionnant pas (Temps d'arrêt) pendant **> 1 heure jusqu'à 6 heures**<br>*(ex., électricité, eau, réseaux de communication, systèmes de sécurité & systèmes en ligne)* | 11% à 15% de la valeur comptable de l'actif | Les opérations fonctionnent à 80% ≤ X < 90%.<br>Récupération complète en 8 à 15 jours ouvrables.<br>Impact grave et perte partielle de données confidentielles critiques.<br>L'entreprise connaît de graves difficultés. |
| **5** | Catastrophique | Infrastructure vitale importante ne fonctionnant pas (Temps d'arrêt)<br>pendant **plus de 6 heures**<br>*(ex., électricité, eau, réseaux de communication, systèmes de sécurité & systèmes en ligne)* | > 15% de la valeur comptable de l'actif | Les opérations fonctionnent à X < 80%.<br>Récupération complète > 15 jours ouvrables.<br>Impact extrêmement sévère et perte de toutes les données confidentielles critiques.<br>L'entreprise connaît des difficultés très graves et fatales. |

---`,
  "de": `## 2. Auswirkungsskala
**Quelle:** ISO 27005:2022; Interne Verfahren von DetereCo (Implementierung des IT-Risikomanagements); und die Vorlage für das IT-Asset-Bewertungsformular von DetereCo

> **Buchwert der Anlage** = Anschaffungspreis der Anlage − Kumulierte Abschreibung/Wertminderung
> Berechnet aus direkt betroffenen Anlagen.

| Skala | Kategorie | Infrastruktur & Anwendungssysteme | Finanzielle Auswirkung | Betriebliche Auswirkung |
|:---:|---|---|---|---|
| **1** | Gering | Weniger kritische unterstützende Anwendungen und Infrastruktur<br>funktionieren für **1 Tag** nicht<br>*(z. B. Mitarbeiteranwesenheit, Website, Drucker, HR-Portal)* | < 1% des Buchwerts der Anlage | Betrieb läuft bei 97% ≤ X < 100%.<br>Erholt sich noch am selben Tag.<br>Auswirkungsfolgen sind vernachlässigbar.<br>Das Unternehmen kann dies ohne große Schwierigkeiten bewältigen. |
| **2** | Erheblich | Weniger kritische unterstützende Anwendungen und Infrastruktur<br>funktionieren für **mehr als 1 Tag bis zu 3 Tagen** nicht<br>*(z. B. Mitarbeiteranwesenheit, Website, Drucker, HR-Portal)* | 1% bis 5% des Buchwerts der Anlage | Betrieb läuft bei 93% ≤ X < 97%.<br>Vollständige Wiederherstellung in maximal 2 Werktagen.<br>Beeinflusst die Aktivitätsleistung.<br>Das Unternehmen hat einige Schwierigkeiten. |
| **3** | Ernsthaft | Wichtige vitale Anwendungen und Infrastruktur<br>funktionieren (Ausfallzeit) für **< 1 Stunde** nicht<br>*(z. B. Strom, Wasser, Kommunikationsnetze, Sicherheitssysteme & Online-Systeme)* | 5.1% bis 10% des Buchwerts der Anlage | Betrieb läuft bei 90% ≤ X < 93%.<br>Vollständige Wiederherstellung zwischen 2–7 Werktagen.<br>Erheblicher Leistungsabfall in Bezug auf wichtige Datensicherheit.<br>Das Unternehmen steht vor überschaubaren Komplikationen. |
| **4** | Kritisch | Wichtige vitale Anwendungen und Infrastruktur<br>funktionieren (Ausfallzeit) für **> 1 Stunde bis zu 6 Stunden** nicht<br>*(z. B. Strom, Wasser, Kommunikationsnetze, Sicherheitssysteme & Online-Systeme)* | 11% bis 15% des Buchwerts der Anlage | Betrieb läuft bei 80% ≤ X < 90%.<br>Vollständige Wiederherstellung in 8–15 Werktagen.<br>Schwerwiegende Auswirkung und Verlust eines Teils kritischer vertraulicher Daten.<br>Das Unternehmen hat ernsthafte Schwierigkeiten. |
| **5** | Katastrophal | Wichtige vitale Infrastruktur funktioniert (Ausfallzeit)<br>für **mehr als 6 Stunden** nicht<br>*(z. B. Strom, Wasser, Kommunikationsnetze, Sicherheitssysteme & Online-Systeme)* | > 15% des Buchwerts der Anlage | Betrieb läuft bei X < 80%.<br>Vollständige Wiederherstellung > 15 Werktage.<br>Extrem schwere Auswirkung und Verlust aller kritischer vertraulicher Daten.<br>Das Unternehmen erlebt sehr schwere und fatale Schwierigkeiten. |

---`,
  "ar": `## 2. مقياس التأثير
**المصدر:** ISO 27005:2022؛ الإجراءات الداخلية لشركة DetereCo (تنفيذ إدارة مخاطر تكنولوجيا المعلومات)؛ ونموذج تقييم أصول تكنولوجيا المعلومات لشركة DetereCo

> **القيمة الدفترية للأصل** = سعر اقتناء الأصل − الاستهلاك المتراكم/انخفاض القيمة
> تُحسب من الأصول المتأثرة بشكل مباشر.

| المقياس | الفئة | أنظمة البنية التحتية والتطبيقات | التأثير المالي | التأثير التشغيلي |
|:---:|---|---|---|---|
| **1** | طفيف | التطبيقات الداعمة والبنية التحتية الأقل أهمية<br>لا تعمل لمدة **يوم واحد**<br>*(على سبيل المثال، حضور الموظفين، موقع الويب، الطابعة، بوابة الموارد البشرية)* | < 1% من القيمة الدفترية للأصل | تسير العمليات بنسبة 97% ≤ X < 100%.<br>تتعافى في نفس اليوم.<br>عواقب التأثير ضئيلة.<br>يمكن للشركة التغلب عليها دون صعوبة كبيرة. |
| **2** | كبير | التطبيقات الداعمة والبنية التحتية الأقل أهمية<br>لا تعمل لمدة **أكثر من يوم واحد حتى 3 أيام**<br>*(على سبيل المثال، حضور الموظفين، موقع الويب، الطابعة، بوابة الموارد البشرية)* | 1% إلى 5% من القيمة الدفترية للأصل | تسير العمليات بنسبة 93% ≤ X < 97%.<br>تعافي كامل خلال يومي عمل كحد أقصى.<br>يؤثر على أداء النشاط.<br>تواجه الشركة بعض الصعوبات. |
| **3** | خطير | التطبيقات والبنية التحتية الحيوية الهامة<br>لا تعمل (فترة التوقف) لمدة **< 1 ساعة**<br>*(على سبيل المثال، الكهرباء، المياه، شبكات الاتصالات، أنظمة الأمان والأنظمة عبر الإنترنت)* | 5.1% إلى 10% من القيمة الدفترية للأصل | تسير العمليات بنسبة 90% ≤ X < 93%.<br>تعافي كامل بين 2–7 أيام عمل.<br>انخفاض كبير في الأداء فيما يتعلق بأمن البيانات المهمة.<br>تواجه الشركة مضاعفات يمكن إدارتها. |
| **4** | حرج | التطبيقات والبنية التحتية الحيوية الهامة<br>لا تعمل (فترة التوقف) لمدة **> 1 ساعة حتى 6 ساعات**<br>*(على سبيل المثال، الكهرباء، المياه، شبكات الاتصالات، أنظمة الأمان والأنظمة عبر الإنترنت)* | 11% إلى 15% من القيمة الدفترية للأصل | تسير العمليات بنسبة 80% ≤ X < 90%.<br>تعافي كامل خلال 8–15 يوم عمل.<br>تأثير خطير وفقدان جزئي للبيانات السرية الحرجة.<br>تواجه الشركة صعوبات بالغة. |
| **5** | كارثي | البنية التحتية الحيوية الهامة لا تعمل (فترة التوقف)<br>لمدة **أكثر من 6 ساعات**<br>*(على سبيل المثال، الكهرباء، المياه، شبكات الاتصالات، أنظمة الأمان والأنظمة عبر الإنترنت)* | > 15% من القيمة الدفترية للأصل | تسير العمليات بنسبة X < 80%.<br>تعافي كامل > 15 يوم عمل.<br>تأثير شديد للغاية وفقدان كامل للبيانات السرية الحرجة.<br>تواجه الشركة صعوبات شديدة ومميتة. |

---`,
  "ru": `## 2. Шкала воздействия
**Источник:** ISO 27005:2022; Внутренние процедуры DetereCo (Внедрение управления ИТ-рисками); и Шаблон формы оценки ИТ-активов DetereCo

> **Балансовая стоимость актива** = Цена приобретения актива − Накопленная амортизация/Обесценение
> Рассчитывается на основе непосредственно затронутых активов.

| Шкала | Категория | Инфраструктура и прикладные системы | Финансовое воздействие | Эксплуатационное воздействие |
|:---:|---|---|---|---|
| **1** | Незначительное | Менее критически важные вспомогательные приложения и инфраструктура<br>не функционируют в течение **1 дня**<br>*(например, посещаемость сотрудников, веб-сайт, принтер, кадровый портал)* | < 1% от балансовой стоимости актива | Операции выполняются на 97% ≤ X < 100%.<br>Восстанавливается в тот же день.<br>Последствия воздействия незначительны.<br>Компания может преодолеть это без особых трудностей. |
| **2** | Существенное | Менее критически важные вспомогательные приложения и инфраструктура<br>не функционируют в течение **более 1 дня и до 3 дней**<br>*(например, посещаемость сотрудников, веб-сайт, принтер, кадровый портал)* | от 1% до 5% от балансовой стоимости актива | Операции выполняются на 93% ≤ X < 97%.<br>Полное восстановление максимум за 2 рабочих дня.<br>Влияет на эффективность деятельности.<br>Компания сталкивается с некоторыми трудностями. |
| **3** | Серьезное | Важные жизненно важные приложения и инфраструктура<br>не функционируют (время простоя) в течение **< 1 часа**<br>*(например, электричество, вода, сети связи, системы безопасности и онлайн-системы)* | от 5.1% до 10% от балансовой стоимости актива | Операции выполняются на 90% ≤ X < 93%.<br>Полное восстановление от 2 до 7 рабочих дней.<br>Значительное снижение производительности, касающееся безопасности важных данных.<br>Компания сталкивается с управляемыми осложнениями. |
| **4** | Критическое | Важные жизненно важные приложения и инфраструктура<br>не функционируют (время простоя) в течение **> 1 часа и до 6 часов**<br>*(например, электричество, вода, сети связи, системы безопасности и онлайн-системы)* | от 11% до 15% от балансовой стоимости актива | Операции выполняются на 80% ≤ X < 90%.<br>Полное восстановление от 8 до 15 рабочих дней.<br>Серьезное воздействие и потеря части критических конфиденциальных данных.<br>Компания испытывает серьезные трудности. |
| **5** | Катастрофическое | Важная жизненно важная инфраструктура не функционирует (время простоя)<br>в течение **более 6 часов**<br>*(например, электричество, вода, сети связи, системы безопасности и онлайн-системы)* | > 15% от балансовой стоимости актива | Операции выполняются при X < 80%.<br>Полное восстановление > 15 рабочих дней.<br>Крайне тяжелые последствия и потеря всех критически важных конфиденциальных данных.<br>Компания испытывает очень серьезные и фатальные трудности. |

---`,
  "ko": `## 2. 영향 척도
**출처:** ISO 27005:2022; DetereCo 내부 절차 (IT 위험 관리 구현); 및 DetereCo IT 자산 평가 양식 템플릿

> **자산 장부 금액** = 자산 취득 가격 − 감가상각누계액/손상차손
> 직접적인 영향을 받는 자산을 기준으로 계산합니다.

| 척도 | 범주 | 인프라 및 애플리케이션 시스템 | 재무적 영향 | 운영적 영향 |
|:---:|---|---|---|---|
| **1** | 미미함 | 덜 중요한 지원 애플리케이션 및 인프라가<br>**1일 동안** 작동하지 않음<br>*(예: 직원 근태 관리, 웹사이트, 프린터, HR 포털)* | 자산 장부 금액의 < 1% | 운영이 97% ≤ X < 100% 수준으로 실행됨.<br>당일 복구됨.<br>영향의 결과는 무시할 수 있음.<br>회사는 큰 어려움 없이 이를 극복할 수 있음. |
| **2** | 중요함 | 덜 중요한 지원 애플리케이션 및 인프라가<br>**1일 초과 3일 이하 동안** 작동하지 않음<br>*(예: 직원 근태 관리, 웹사이트, 프린터, HR 포털)* | 자산 장부 금액의 1% ~ 5% | 운영이 93% ≤ X < 97% 수준으로 실행됨.<br>최대 2영업일 이내에 완전히 복구됨.<br>활동 수행에 영향을 미침.<br>회사는 몇 가지 어려움에 직면함. |
| **3** | 심각함 | 중요하고 핵심적인 애플리케이션 및 인프라가<br>**< 1시간 동안** 작동하지 않음(다운타임)<br>*(예: 전기, 수도, 통신 네트워크, 보안 시스템 및 온라인 시스템)* | 자산 장부 금액의 5.1% ~ 10% | 운영이 90% ≤ X < 93% 수준으로 실행됨.<br>2~7영업일 이내에 완전히 복구됨.<br>중요한 데이터 보안과 관련된 주요 성능 저하.<br>회사는 관리 가능한 합병증에 직면함. |
| **4** | 치명적 | 중요하고 핵심적인 애플리케이션 및 인프라가<br>**> 1시간 초과 6시간 이하 동안** 작동하지 않음(다운타임)<br>*(예: 전기, 수도, 통신 네트워크, 보안 시스템 및 온라인 시스템)* | 자산 장부 금액의 11% ~ 15% | 운영이 80% ≤ X < 90% 수준으로 실행됨.<br>8~15영업일 이내에 완전히 복구됨.<br>심각한 영향 및 일부 핵심 기밀 데이터 손실.<br>회사는 심각한 어려움을 겪음. |
| **5** | 재앙적 | 중요하고 핵심적인 인프라가 **6시간 초과 동안**<br>작동하지 않음(다운타임)<br>*(예: 전기, 수도, 통신 네트워크, 보안 시스템 및 온라인 시스템)* | 자산 장부 금액의 > 15% | 운영이 X < 80% 수준으로 실행됨.<br>완전 복구 > 15영업일.<br>극도로 심각한 영향 및 모든 핵심 기밀 데이터 손실.<br>회사는 매우 심각하고 치명적인 어려움을 겪음. |

---`,
  "ja": `## 2. 影響スケール
**出典:** ISO 27005:2022。DetereCo 内部手順 (ITリスク管理の実装)。および DetereCo IT資産評価フォームテンプレート

> **資産帳簿価額** = 資産取得価格 − 減価償却累計額/減損損失
> 直接影響を受ける資産から計算されます。

| スケール | カテゴリ | インフラストラクチャおよびアプリケーションシステム | 財務的影響 | 運用的影響 |
|:---:|---|---|---|---|
| **1** | 軽微 | 重要度の低いサポートアプリケーションとインフラストラクチャが<br>**1日間**機能しない<br>*(例: 従業員の勤怠管理、ウェブサイト、プリンター、HRポータル)* | 資産帳簿価額の < 1% | オペレーションは 97% ≤ X < 100% で実行されます。<br>同日中に回復します。<br>影響の結果は無視できます。<br>会社は大きな困難なくこれを克服できます。 |
| **2** | 著しい | 重要度の低いサポートアプリケーションとインフラストラクチャが<br>**1日を超え3日間**機能しない<br>*(例: 従業員の勤怠管理、ウェブサイト、プリンター、HRポータル)* | 資産帳簿価額の 1% ～ 5% | オペレーションは 93% ≤ X < 97% で実行されます。<br>最大2営業日以内に完全に回復します。<br>活動パフォーマンスに影響を与えます。<br>会社はいくつかの困難に直面します。 |
| **3** | 深刻 | 重要な不可欠なアプリケーションとインフラストラクチャが<br>**< 1時間**機能しない（ダウンタイム）<br>*(例: 電気、水道、通信ネットワーク、セキュリティシステム、オンラインシステム)* | 資産帳簿価額の 5.1% ～ 10% | オペレーションは 90% ≤ X < 93% で実行されます。<br>2～7営業日以内に完全に回復します。<br>重要なデータセキュリティに関する大幅なパフォーマンス低下。<br>会社は管理可能な複雑さに直面します。 |
| **4** | 致命的 | 重要な不可欠なアプリケーションとインフラストラクチャが<br>**> 1時間を超え6時間まで**機能しない（ダウンタイム）<br>*(例: 電気、水道、通信ネットワーク、セキュリティシステム、オンラインシステム)* | 資産帳簿価額の 11% ～ 15% | オペレーションは 80% ≤ X < 90% で実行されます。<br>8～15営業日以内に完全に回復します。<br>深刻な影響と一部の重要な機密データの損失。<br>会社は深刻な困難を経験します。 |
| **5** | 壊滅的 | 重要な不可欠なインフラストラクチャが<br>**6時間を超えて**機能しない（ダウンタイム）<br>*(例: 電気、水道、通信ネットワーク、セキュリティシステム、オンラインシステム)* | 資産帳簿価額の > 15% | オペレーションは X < 80% で実行されます。<br>完全な回復 > 15営業日。<br>極めて深刻な影響とすべての重要な機密データの損失。<br>会社は非常に深刻で致命的な困難を経験します。 |

---`
};

const criteriaMatch = content.match(/criteria:\s*(\{[\s\S]+?\n      \}),/);
if (criteriaMatch) {
  let criteriaStr = criteriaMatch[1];
  for (const [lang, newImpact] of Object.entries(impactTranslations)) {
    // We isolate each language string inside criteria
    const langRegex = new RegExp(`"${lang}"\\s*:\\s*"([\\s\\S]*?)"(?=\\n\\s*(?:,\\s*"|\\}))`, 'g');
    criteriaStr = criteriaStr.replace(langRegex, (match, mdStr) => {
      // Find `## 2. [Title] ... ---` and replace it
      // `[^]*?` is non-greedy match.
      // Since some languages might already have `---` right after, we will match up to `\n---` or `\n## 3.`
      // Wait, in `en`, `---` appears. Let's just match from `## 2.` to just before `\n## 3.`
      const replacedMd = mdStr.replace(/## 2\.[^]*?(?=\\n## 3\.)/, newImpact.replace(/\n/g, '\\n') + '\\n');
      return `"${lang}": "${replacedMd}"`;
    });
  }
  content = content.replace(criteriaMatch[1], criteriaStr);
  fs.writeFileSync(filePath, content, 'utf8');
  console.log("Successfully updated Impact Scale translations!");
} else {
  console.log("Could not find criteria object");
}
