const fs = require('fs');
const path = require('path');

const filePath = path.resolve(__dirname, '../index.html');
let content = fs.readFileSync(filePath, 'utf8');

const riskLevelTranslations = {
  "id": `## 3. Tingkat Risiko
**Sumber:** ISO 27005:2022 & Prosedur Internal DetereCo (Implementasi Manajemen Risiko TI)

> **Rumus:** Tingkat Risiko = Kemungkinan (P) × Dampak (I)

### 3a. Klasifikasi Tingkat Risiko

| Rentang Skor (P × I) | Tingkat Risiko | Indikator Warna | Tindakan Mitigasi |
|:---:|---|:---:|---|
| **1 – 5** | Rendah | 🟢 Hijau Muda | Risiko dapat diterima. Kontrol keamanan yang ada memadai, pemantauan rutin sudah cukup. |
| **6 – 11** | Rendah ke Sedang | 🟩 Hijau Tua | Risiko membutuhkan kewaspadaan. Tinjauan berkala dan perencanaan untuk kontrol keamanan tambahan. |
| **12 – 15** | Sedang | 🟡 Kuning | Risiko harus dipantau. Tinjauan berkala dan penambahan kontrol preventif skala menengah, biasanya setiap **3–6 bulan**. |
| **16 – 19** | Sedang ke Tinggi | 🟧 Oranye | Risiko tidak dapat diterima. Membutuhkan tindakan mitigasi ZTA komprehensif dalam waktu dekat **(1–3 bulan)** untuk mencegah insiden kritis. |
| **20 – 25** | Tinggi | 🔴 Merah | Prioritas penanganan utama. Kondisi darurat yang membutuhkan mitigasi dan penahanan jaringan komprehensif untuk menurunkan tingkat risiko dalam **< 1 bulan**. |

### 3b. Matriks Tingkat Risiko

|  | **Dampak 1** *(Minor)* | **Dampak 2** *(Signifikan)* | **Dampak 3** *(Serius)* | **Dampak 4** *(Kritis)* | **Dampak 5** *(Bencana)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Kemungkinan 5** *(Hampir Pasti)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Kemungkinan 4** *(Sangat Mungkin)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Kemungkinan 3** *(Mungkin)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Kemungkinan 2** *(Agak Tidak Mungkin)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Kemungkinan 1** *(Tidak Mungkin)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`,
  "zh": `## 3. 风险级别
**来源:** ISO 27005:2022 & DetereCo 内部程序（IT 风险管理实施）

> **公式:** 风险级别 = 可能性 (P) × 影响 (I)

### 3a. 风险级别分类

| 分数范围 (P × I) | 风险级别 | 颜色指示器 | 缓解措施 |
|:---:|---|:---:|---|
| **1 – 5** | 低 | 🟢 浅绿 | 风险可接受。现有安全控制充足，常规监控即可。 |
| **6 – 11** | 低到中等 | 🟩 深绿 | 风险需要警惕。定期审查并计划增加额外的安全控制。 |
| **12 – 15** | 中等 | 🟡 黄色 | 必须监控风险。定期审查并增加中等规模的预防性控制，通常每 **3-6 个月**一次。 |
| **16 – 19** | 中等到高 | 🟧 橙色 | 风险不可接受。要求在不久的将来 **(1-3 个月)** 采取全面的零信任架构 (ZTA) 缓解措施，以防止发生严重事件。 |
| **20 – 25** | 高 | 🔴 红色 | 最高处理优先级。需要采取全面网络缓解和遏制措施以在 **< 1 个月**内降低风险级别的紧急情况。 |

### 3b. 风险级别矩阵

|  | **影响 1** *(轻微)* | **影响 2** *(显著)* | **影响 3** *(严重)* | **影响 4** *(危急)* | **影响 5** *(灾难性)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **可能性 5** *(几乎确定)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **可能性 4** *(很有可能)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **可能性 3** *(可能)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **可能性 2** *(较不可能)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **可能性 1** *(不太可能)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`,
  "es": `## 3. Nivel de Riesgo
**Fuente:** ISO 27005:2022 & Procedimientos Internos de DetereCo (Implementación de Gestión de Riesgos de TI)

> **Fórmula:** Nivel de Riesgo = Probabilidad (P) × Impacto (I)

### 3a. Clasificación del Nivel de Riesgo

| Rango de Puntuación (P × I) | Nivel de Riesgo | Indicador de Color | Acción de Mitigación |
|:---:|---|:---:|---|
| **1 – 5** | Bajo | 🟢 Verde Claro | El riesgo es aceptable. Los controles de seguridad existentes son adecuados, el monitoreo de rutina es suficiente. |
| **6 – 11** | Bajo a Moderado | 🟩 Verde Oscuro | El riesgo requiere vigilancia. Revisión periódica y planificación de controles de seguridad adicionales. |
| **12 – 15** | Moderado | 🟡 Amarillo | El riesgo debe ser monitoreado. Revisión periódica y adición de controles preventivos a mediana escala, típicamente cada **3–6 meses**. |
| **16 – 19** | Moderado a Alto | 🟧 Naranja | El riesgo es inaceptable. Requiere acciones integrales de mitigación de ZTA en el futuro cercano **(1–3 meses)** para prevenir incidentes críticos. |
| **20 – 25** | Alto | 🔴 Rojo | Máxima prioridad de manejo. Condición de emergencia que requiere mitigación y contención integral de la red para reducir el nivel de riesgo en **< 1 mes**. |

### 3b. Matriz de Nivel de Riesgo

|  | **Impacto 1** *(Menor)* | **Impacto 2** *(Significativo)* | **Impacto 3** *(Grave)* | **Impacto 4** *(Crítico)* | **Impacto 5** *(Catastrófico)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Probabilidad 5** *(Casi Seguro)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Probabilidad 4** *(Muy Probable)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Probabilidad 3** *(Probable)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Probabilidad 2** *(Poco Probable)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Probabilidad 1** *(Improbable)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`,
  "fr": `## 3. Niveau de Risque
**Source:** ISO 27005:2022 & Procédures Internes de DetereCo (Mise en Œuvre de la Gestion des Risques Informatiques)

> **Formule:** Niveau de Risque = Probabilité (P) × Impact (I)

### 3a. Classification du Niveau de Risque

| Plage de Score (P × I) | Niveau de Risque | Indicateur de Couleur | Action d'Atténuation |
|:---:|---|:---:|---|
| **1 – 5** | Faible | 🟢 Vert Clair | Le risque est acceptable. Les contrôles de sécurité existants sont adéquats, une surveillance de routine est suffisante. |
| **6 – 11** | Faible à Modéré | 🟩 Vert Foncé | Le risque nécessite de la vigilance. Examen périodique et planification de contrôles de sécurité supplémentaires. |
| **12 – 15** | Modéré | 🟡 Jaune | Le risque doit être surveillé. Examen périodique et ajout de contrôles préventifs à moyenne échelle, typiquement tous les **3 à 6 mois**. |
| **16 – 19** | Modéré à Élevé | 🟧 Orange | Le risque est inacceptable. Nécessite des actions globales d'atténuation ZTA dans un avenir proche **(1 à 3 mois)** pour prévenir les incidents critiques. |
| **20 – 25** | Élevé | 🔴 Rouge | Priorité de traitement absolue. Condition d'urgence nécessitant une atténuation et un confinement complets du réseau pour abaisser le niveau de risque dans les **< 1 mois**. |

### 3b. Matrice du Niveau de Risque

|  | **Impact 1** *(Mineur)* | **Impact 2** *(Significatif)* | **Impact 3** *(Grave)* | **Impact 4** *(Critique)* | **Impact 5** *(Catastrophique)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Probabilité 5** *(Presque Certain)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Probabilité 4** *(Très Probable)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Probabilité 3** *(Probable)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Probabilité 2** *(Peu Probable)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Probabilité 1** *(Improbable)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`,
  "de": `## 3. Risikostufe
**Quelle:** ISO 27005:2022 & Interne Verfahren von DetereCo (Implementierung des IT-Risikomanagements)

> **Formel:** Risikostufe = Wahrscheinlichkeit (P) × Auswirkung (I)

### 3a. Risikostufenklassifizierung

| Punktebereich (P × I) | Risikostufe | Farbindikator | Minderungsmaßnahme |
|:---:|---|:---:|---|
| **1 – 5** | Niedrig | 🟢 Hellgrün | Risiko ist akzeptabel. Bestehende Sicherheitskontrollen sind angemessen, routinemäßige Überwachung ist ausreichend. |
| **6 – 11** | Niedrig bis Mittel | 🟩 Dunkelgrün | Risiko erfordert Wachsamkeit. Regelmäßige Überprüfung und Planung für zusätzliche Sicherheitskontrollen. |
| **12 – 15** | Mittel | 🟡 Gelb | Risiko muss überwacht werden. Regelmäßige Überprüfung und Hinzufügung mittelgroßer präventiver Kontrollen, typischerweise alle **3–6 Monate**. |
| **16 – 19** | Mittel bis Hoch | 🟧 Orange | Risiko ist inakzeptabel. Erfordert in naher Zukunft **(1–3 Monate)** umfassende ZTA-Minderungsmaßnahmen, um kritische Vorfälle zu verhindern. |
| **20 – 25** | Hoch | 🔴 Rot | Höchste Priorität bei der Bearbeitung. Notfallzustand, der eine umfassende Netzwerk-Minderung und Eindämmung erfordert, um die Risikostufe innerhalb von **< 1 Monat** zu senken. |

### 3b. Risikostufenmatrix

|  | **Auswirkung 1** *(Gering)* | **Auswirkung 2** *(Erheblich)* | **Auswirkung 3** *(Ernsthaft)* | **Auswirkung 4** *(Kritisch)* | **Auswirkung 5** *(Katastrophal)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Wahrscheinlichkeit 5** *(Fast Sicher)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Wahrscheinlichkeit 4** *(Sehr Wahrscheinlich)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Wahrscheinlichkeit 3** *(Wahrscheinlich)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Wahrscheinlichkeit 2** *(Eher Unwahrscheinlich)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Wahrscheinlichkeit 1** *(Unwahrscheinlich)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`,
  "ar": `## 3. مستوى الخطر
**المصدر:** ISO 27005:2022 & الإجراءات الداخلية لشركة DetereCo (تنفيذ إدارة مخاطر تكنولوجيا المعلومات)

> **الصيغة:** مستوى الخطر = الاحتمالية (P) × التأثير (I)

### 3a. تصنيف مستوى الخطر

| نطاق النتيجة (P × I) | مستوى الخطر | مؤشر اللون | إجراء التخفيف |
|:---:|---|:---:|---|
| **1 – 5** | منخفض | 🟢 أخضر فاتح | الخطر مقبول. الضوابط الأمنية الحالية كافية، والمراقبة الروتينية كافية. |
| **6 – 11** | منخفض إلى متوسط | 🟩 أخضر غامق | الخطر يتطلب اليقظة. المراجعة الدورية والتخطيط لضوابط أمنية إضافية. |
| **12 – 15** | متوسط | 🟡 أصفر | يجب مراقبة الخطر. المراجعة الدورية وإضافة ضوابط وقائية متوسطة الحجم، عادة كل **3-6 أشهر**. |
| **16 – 19** | متوسط إلى مرتفع | 🟧 برتقالي | الخطر غير مقبول. يتطلب إجراءات تخفيف شاملة لـ ZTA في المستقبل القريب **(1-3 أشهر)** لمنع الحوادث الحرجة. |
| **20 – 25** | مرتفع | 🔴 أحمر | أولوية التعامل القصوى. حالة طوارئ تتطلب تخفيف وتأمين شبكة شامل لخفض مستوى الخطر في غضون **< 1 شهر**. |

### 3b. مصفوفة مستوى الخطر

|  | **التأثير 1** *(طفيف)* | **التأثير 2** *(كبير)* | **التأثير 3** *(خطير)* | **التأثير 4** *(حرج)* | **التأثير 5** *(كارثي)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **الاحتمالية 5** *(شبه مؤكد)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **الاحتمالية 4** *(محتمل جدا)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **الاحتمالية 3** *(محتمل)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **الاحتمالية 2** *(غير محتمل نوعا ما)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **الاحتمالية 1** *(غير محتمل)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`,
  "ru": `## 3. Уровень риска
**Источник:** ISO 27005:2022 & Внутренние процедуры DetereCo (Внедрение управления ИТ-рисками)

> **Формула:** Уровень риска = Вероятность (P) × Воздействие (I)

### 3a. Классификация уровня риска

| Диапазон баллов (P × I) | Уровень риска | Цветовой индикатор | Действия по снижению риска |
|:---:|---|:---:|---|
| **1 – 5** | Низкий | 🟢 Светло-зеленый | Риск приемлем. Существующих средств контроля безопасности достаточно, достаточно регулярного мониторинга. |
| **6 – 11** | От низкого до среднего | 🟩 Темно-зеленый | Риск требует бдительности. Периодический анализ и планирование дополнительных средств контроля безопасности. |
| **12 – 15** | Средний | 🟡 Желтый | Риск необходимо контролировать. Периодический анализ и добавление профилактических мер среднего масштаба, обычно каждые **3–6 месяцев**. |
| **16 – 19** | От среднего до высокого | 🟧 Оранжевый | Риск неприемлем. Требует комплексных мер по снижению рисков архитектуры нулевого доверия (ZTA) в ближайшем будущем **(1–3 месяца)** для предотвращения критических инцидентов. |
| **20 – 25** | Высокий | 🔴 Красный | Наивысший приоритет обработки. Чрезвычайная ситуация, требующая комплексного снижения рисков сети и локализации для снижения уровня риска в течение **< 1 месяца**. |

### 3b. Матрица уровня риска

|  | **Воздействие 1** *(Незначительное)* | **Воздействие 2** *(Существенное)* | **Воздействие 3** *(Серьезное)* | **Воздействие 4** *(Критическое)* | **Воздействие 5** *(Катастрофическое)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **Вероятность 5** *(Почти наверняка)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **Вероятность 4** *(Весьма вероятно)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **Вероятность 3** *(Вероятно)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **Вероятность 2** *(Скорее маловероятно)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **Вероятность 1** *(Маловероятно)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`,
  "ko": `## 3. 위험 수준
**출처:** ISO 27005:2022 & DetereCo 내부 절차 (IT 위험 관리 구현)

> **공식:** 위험 수준 = 발생 가능성 (P) × 영향 (I)

### 3a. 위험 수준 분류

| 점수 범위 (P × I) | 위험 수준 | 색상 표시기 | 완화 조치 |
|:---:|---|:---:|---|
| **1 – 5** | 낮음 | 🟢 연두색 | 위험 수용 가능. 기존 보안 통제가 적절하며 정기적인 모니터링으로 충분함. |
| **6 – 11** | 낮음에서 보통 | 🟩 짙은 녹색 | 위험에 대한 경계 필요. 추가 보안 통제에 대한 주기적인 검토 및 계획. |
| **12 – 15** | 보통 | 🟡 노란색 | 위험을 모니터링해야 함. 일반적으로 **3~6개월**마다 중규모 예방 통제의 주기적인 검토 및 추가. |
| **16 – 19** | 보통에서 높음 | 🟧 주황색 | 위험 수용 불가. 심각한 사고를 예방하기 위해 가까운 시일 내에 **(1~3개월)** 포괄적인 ZTA 완화 조치가 필요함. |
| **20 – 25** | 높음 | 🔴 빨간색 | 처리 우선순위 최상. **< 1개월** 이내에 위험 수준을 낮추기 위해 포괄적인 네트워크 완화 및 억제가 필요한 비상 상황. |

### 3b. 위험 수준 매트릭스

|  | **영향 1** *(미미함)* | **영향 2** *(중요함)* | **영향 3** *(심각함)* | **영향 4** *(치명적)* | **영향 5** *(재앙적)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **발생 가능성 5** *(거의 확실함)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **발생 가능성 4** *(가능성 높음)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **발생 가능성 3** *(가능성 있음)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **발생 가능성 2** *(다소 희박함)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **발생 가능성 1** *(희박함)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`,
  "ja": `## 3. リスクレベル
**出典:** ISO 27005:2022 & DetereCo 内部手順 (ITリスク管理の実装)

> **公式:** リスクレベル = 可能性 (P) × 影響 (I)

### 3a. リスクレベルの分類

| スコア範囲 (P × I) | リスクレベル | カラーインジケーター | 緩和アクション |
|:---:|---|:---:|---|
| **1 – 5** | 低 | 🟢 薄緑 | リスクは許容範囲内です。既存のセキュリティコントロールは適切であり、定期的な監視で十分です。 |
| **6 – 11** | 低から中 | 🟩 濃緑 | リスクには警戒が必要です。追加のセキュリティコントロールの定期的なレビューと計画。 |
| **12 – 15** | 中 | 🟡 黄色 | リスクを監視する必要があります。定期的なレビューと、中規模の予防的コントロールの追加（通常は **3～6 か月** ごと）。 |
| **16 – 19** | 中から高 | 🟧 オレンジ | リスクは許容できません。重大なインシデントを防ぐために、近い将来 **(1～3 か月)** に包括的なZTA緩和アクションが必要です。 |
| **20 – 25** | 高 | 🔴 赤 | 最優先の対応が必要です。**1 か月未満** でリスクレベルを下げるために、包括的なネットワーク緩和と封じ込めを必要とする緊急事態。 |

### 3b. リスクレベルマトリックス

|  | **影響 1** *(軽微)* | **影響 2** *(著しい)* | **影響 3** *(深刻)* | **影響 4** *(致命的)* | **影響 5** *(壊滅的)* |
|---|:---:|:---:|:---:|:---:|:---:|
| **可能性 5** *(ほぼ確実)* | 🟩 7 | 🟡 12 | 🟧 17 | 🔴 22 | 🔴 25 |
| **可能性 4** *(可能性が高い)* | 🟢 4 | 🟩 9 | 🟡 14 | 🟧 19 | 🔴 24 |
| **可能性 3** *(起こり得る)* | 🟢 3 | 🟩 8 | 🟡 13 | 🟧 18 | 🔴 23 |
| **可能性 2** *(あまり起こりそうにない)* | 🟢 2 | 🟩 6 | 🟩 11 | 🟧 16 | 🔴 21 |
| **可能性 1** *(起こりそうにない)* | 🟢 1 | 🟢 5 | 🟩 10 | 🟡 15 | 🔴 20 |
`
};

const criteriaMatch = content.match(/criteria:\s*(\{[\s\S]+?\n      \}),/);
if (criteriaMatch) {
  let criteriaStr = criteriaMatch[1];
  for (const [lang, newRiskLevel] of Object.entries(riskLevelTranslations)) {
    // Isolate language string
    const langRegex = new RegExp(`"${lang}"\\s*:\\s*"([\\s\\S]*?)"(?=\\n\\s*(?:,\\s*"|\\}))`, 'g');
    criteriaStr = criteriaStr.replace(langRegex, (match, mdStr) => {
      // Find `## 3. [Title] ... ` to the end and replace it.
      const replacedMd = mdStr.replace(/## 3\.[^]*/, newRiskLevel.replace(/\n/g, '\\n'));
      return `"${lang}": "${replacedMd}"`;
    });
  }
  content = content.replace(criteriaMatch[1], criteriaStr);
  fs.writeFileSync(filePath, content, 'utf8');
  console.log("Successfully updated Risk Level translations!");
} else {
  console.log("Could not find criteria object");
}
