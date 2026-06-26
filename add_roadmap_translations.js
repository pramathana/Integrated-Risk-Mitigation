const fs = require('fs');

const id_eval = `        "id": \`# Peta Jalan Validasi 3 Tahap
## Metodologi Evaluasi

Fase Evaluasi dilakukan melalui serangkaian aktivitas terstruktur yang melibatkan evaluasi dari Pakar (Internal dan Eksternal) dengan tahapan detail sebagai berikut:

**1. Penilaian Pakar (Skala Likert)**
: Langkah pertama adalah menyajikan artefak konseptual kepada para pakar. Para pakar diminta untuk memberikan penilaian kuantitatif deskriptif terkait relevansi model menggunakan kuesioner Skala Likert dengan rentang 4 poin untuk menghindari bias ambivalensi nilai tengah. Skala yang digunakan terdiri dari:
- **(1)** Sangat Tidak Relevan
- **(2)** Tidak Relevan
- **(3)** Relevan
- **(4)** Sangat Relevan

**2. Focus Group Discussion (FGD)**
: Hasil penilaian kuantitatif deskriptif yang dianggap sangat tidak relevan dan tidak relevan oleh pakar kemudian didiskusikan lebih mendalam melalui diskusi terarah. Diskusi ini bertujuan untuk menggali alasan yang mendasari penilaian tersebut, seperti *"mengapa komponen tersebut dianggap tidak relevan?"* atau *"Di mana letak kekurangan model tersebut?"*, guna memperoleh umpan balik kualitatif naratif yang konkret.

**3. Validasi Partisipan**
: Tahap validasi akhir adalah meninjau artefak yang telah direvisi. Aktivitas ini melibatkan pakar yang sama untuk meninjau perbaikan dan mencapai kesepakatan akhir bahwa artefak yang direvisi relevan digunakan sebagai pedoman manajemen risiko keamanan siber di lingkungan DetereCo. Setelah kesepakatan tercapai, penelitian dilanjutkan dengan menarik Kesimpulan dan Rekomendasi.

---

## Hasil Kuesioner Penilaian Pakar\`,`;

const ru_eval = `        "ru": \`# 3-Этапная Дорожная Карта Валидации
## Методология Оценки

Фаза оценки проводится через серию структурированных мероприятий с привлечением экспертов (внутренних и внешних) со следующими подробными этапами:

**1. Экспертная Оценка (Шкала Ликерта)**
: Первый шаг — представить концептуальные артефакты экспертам. Экспертам предлагается дать описательную количественную оценку релевантности модели, используя анкету со шкалой Ликерта с 4-балльным диапазоном, чтобы избежать предвзятости средних значений. Используемая шкала состоит из:
- **(1)** Совершенно нерелевантно
- **(2)** Нерелевантно
- **(3)** Релевантно
- **(4)** Очень релевантно

**2. Фокус-групповая дискуссия (FGD)**
: Результаты описательной количественной оценки, которые эксперты сочли совершенно нерелевантными или нерелевантнными, затем более подробно обсуждаются в ходе направленных дискуссий. Эта дискуссия направлена на выяснение основных причин такой оценки, например *"почему компонент считается нерелевантным?"* или *"В чем недостатки модели?"*, чтобы получить конкретную повествовательную качественную обратную связь.

**3. Валидация Участниками**
: Заключительный этап валидации — рассмотрение пересмотренных артефактов. В этой деятельности участвуют те же эксперты для рассмотрения улучшений и достижения окончательного согласия в том, что пересмотренные артефакты релевантны для использования в качестве руководящих принципов управления рисками кибербезопасности в среде DetereCo. После достижения согласия исследование переходит к формулированию Выводов и Рекомендаций.

---

## Результаты Анкеты Экспертной Оценки\`,`;

const ko_eval = `        "ko": \`# 3단계 검증 로드맵
## 평가 방법론

평가 단계는 다음의 상세한 단계와 함께 전문가(내부 및 외부)의 평가를 포함하는 일련의 구조화된 활동을 통해 수행됩니다:

**1. 전문가 평가 (리커트 척도)**
: 첫 번째 단계는 개념적 아티팩트를 전문가에게 제시하는 것입니다. 전문가들은 중간값의 양가적 편향을 피하기 위해 4점 척도의 리커트 척도 설문지를 사용하여 모델의 관련성에 대한 기술적 정량적 평가를 제공하도록 요청받습니다. 사용된 척도는 다음과 같습니다:
- **(1)** 전혀 관련 없음
- **(2)** 관련 없음
- **(3)** 관련 있음
- **(4)** 매우 관련 있음

**2. 초점 그룹 토론 (FGD)**
: 전문가들이 전혀 관련 없거나 관련 없다고 판단한 기술적 정량적 평가 결과는 이후 안내된 토론을 통해 더 깊이 논의됩니다. 이 토론은 *"왜 해당 구성 요소가 관련이 없는 것으로 간주되는가?"* 또는 *"모델의 부족한 점은 무엇인가?"*와 같은 평가 이면의 근본적인 이유를 탐구하여 구체적인 서술적 정성적 피드백을 얻는 것을 목표로 합니다.

**3. 참여자 검증**
: 최종 검증 단계는 수정된 아티팩트를 검토하는 것입니다. 이 활동에는 동일한 전문가가 참여하여 개선 사항을 검토하고, 수정된 아티팩트가 DetereCo 환경의 사이버 보안 위험 관리 지침으로 사용하기에 관련성이 있다는 최종 합의에 도달합니다. 합의에 도달한 후, 연구는 결론 및 권장 사항 도출로 이어집니다.

---

## 전문가 평가 설문지 결과\`,`;

const ja_eval = `        "ja": \`# 3段階の検証ロードマップ
## 評価方法論

評価フェーズは、以下の詳細な段階を伴う、専門家（内部および外部）による評価を含む一連の構造化された活動を通じて実施されます：

**1. 専門家の判断（リッカート尺度）**
: 最初のステップは、概念的な成果物を専門家に提示することです。専門家は、中間値の曖昧なバイアスを避けるために4点満点のリッカート尺度アンケートを使用して、モデルの関連性に関する記述的かつ定量的な評価を提供するよう求められます。使用される尺度は以下の通りです：
- **(1)** 全く関連がない
- **(2)** 関連がない
- **(3)** 関連がある
- **(4)** 非常に重要である

**2. フォーカスグループディスカッション（FGD）**
: 専門家によって全く関連がない、または関連がないと判断された記述的および定量的評価の結果は、その後、ガイド付きの議論を通じてさらに深く議論されます。この議論は、*"なぜそのコンポーネントは関連性がないと見なされるのか？"* または *"モデルの欠点はどこにあるのか？"*といった評価の背後にある根本的な理由を探り、具体的な物語的な定性的フィードバックを得ることを目的としています。

**3. 参加者による検証**
: 最終検証段階は、改訂された成果物をレビューすることです。この活動には同じ専門家が関与し、改善点を確認して、改訂された成果物がDetereCo環境におけるサイバーセキュリティリスク管理のガイドラインとして使用するのに関連しているという最終的な合意に達します。合意に達した後、研究は結論と推奨事項の導出に進みます。

---

## 専門家評価アンケート結果\`
      },`;

let content = fs.readFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', 'utf8');

const regex = /(evaluation: \{\s*"en": `[\s\S]*?## Expert Judgment Questionnaire Results`\s*),/;
const replacement = `$1,\n${id_eval}\n${ru_eval}\n${ko_eval}\n${ja_eval}`;

if (!content.match(regex)) {
    console.log("Could not match the evaluation object!");
} else if (content.includes('## Hasil Kuesioner Penilaian Pakar')) {
    console.log("Already added");
} else {
    content = content.replace(regex, replacement);
    fs.writeFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', content, 'utf8');
    console.log("Translations added for validation roadmap!");
}
