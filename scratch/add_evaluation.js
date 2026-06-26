const fs = require('fs');
const path = require('path');

const htmlPath = path.join('c:', 'ANTIGRAVITY IDE FOLDER', 'Dashboard Mitigasi Risiko Terintegrasi', 'index.html');
const mdPath = path.join('c:', 'ANTIGRAVITY IDE FOLDER', 'Dashboard Mitigasi Risiko Terintegrasi', 'artifact_evaluation.md');

let html = fs.readFileSync(htmlPath, 'utf8');
const md = fs.readFileSync(mdPath, 'utf8');

// 1. Insert button
const btnMarker = `      <button class="menu-btn" data-view="view-dashboard-after" data-i18n="menu_dashboard_after"`;
const btnInsertion = `      <button class="menu-btn" data-view="view-evaluation" data-i18n="menu_evaluation"
        onclick="switchView('view-evaluation')">
        Artifact Evaluation
      </button>
`;
html = html.replace(btnMarker, btnInsertion + btnMarker);

// 2. Insert div
const divMarker = `    <div id="view-dashboard-after" style="display: none">`;
const divInsertion = `    <div id="view-evaluation" style="display: none">
      <div class="md-content" id="md-evaluation">Loading...</div>
    </div>

`;
html = html.replace(divMarker, divInsertion + divMarker);

// 3. Insert into embeddedMarkdown
const mdMarker = `      priority: {`;
const mdInsertion = `      evaluation: {
        "en": \`${md.replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\$/g, '\\$')}\`
      },
`;
html = html.replace(mdMarker, mdInsertion + mdMarker);

// 4. Insert into renderMarkdown
const renderMarker = `        document.getElementById("md-priority").innerHTML = marked.parse(
          embeddedMarkdown.priority[lang] || embeddedMarkdown.priority.en,
        );`;
const renderInsertion = `
        if (document.getElementById("md-evaluation")) {
          document.getElementById("md-evaluation").innerHTML = marked.parse(
            embeddedMarkdown.evaluation[lang] || embeddedMarkdown.evaluation.en,
          );
        }`;
html = html.replace(renderMarker, renderMarker + renderInsertion);

// 5. Insert translations
const transEnMarker = `    translations.en.menu_dashboard_after = "Artifact [After Rev]";`;
html = html.replace(transEnMarker, transEnMarker + `\n    translations.en.menu_evaluation = "Artifact Evaluation";`);

const transIdMarker = `    translations.id.menu_dashboard_after = "Artefak [Setelah Revisi]";`;
html = html.replace(transIdMarker, transIdMarker + `\n    translations.id.menu_evaluation = "Evaluasi Artefak";`);

const transZhMarker = `    translations.zh.menu_dashboard_after = "工件 [修订后]";`;
html = html.replace(transZhMarker, transZhMarker + `\n    translations.zh.menu_evaluation = "工件评估";`);

const transEsMarker = `      translations.es.menu_dashboard_after = "Artefacto [Después de la Revisión]";`;
html = html.replace(transEsMarker, transEsMarker + `\n      translations.es.menu_evaluation = "Evaluación de Artefactos";`);

const transFrMarker = `      translations.fr.menu_dashboard_after = "Artefact [Après Révision]";`;
html = html.replace(transFrMarker, transFrMarker + `\n      translations.fr.menu_evaluation = "Évaluation des Artefacts";`);

const transDeMarker = `      translations.de.menu_dashboard_after = "Artefakt [Nach Revision]";`;
html = html.replace(transDeMarker, transDeMarker + `\n      translations.de.menu_evaluation = "Artefaktbewertung";`);

const transArMarker = `      translations.ar.menu_dashboard_after = "المنتج [بعد المراجعة]";`;
html = html.replace(transArMarker, transArMarker + `\n      translations.ar.menu_evaluation = "تقييم الأداة";`);

const transRuMarker = `      translations.ru.menu_dashboard_after = "Артефакт [После пересмотра]";`;
html = html.replace(transRuMarker, transRuMarker + `\n      translations.ru.menu_evaluation = "Оценка артефактов";`);

const transKoMarker = `      translations.ko.menu_dashboard_after = "산출물 [수정 후]";`;
html = html.replace(transKoMarker, transKoMarker + `\n      translations.ko.menu_evaluation = "산출물 평가";`);

const transJaMarker = `      translations.ja.menu_dashboard_after = "アーティファクト [改訂後]";`;
html = html.replace(transJaMarker, transJaMarker + `\n      translations.ja.menu_evaluation = "アーティファクトの評価";`);

fs.writeFileSync(htmlPath, html, 'utf8');
console.log('Successfully updated index.html');
