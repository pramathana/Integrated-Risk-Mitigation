const fs = require('fs');
const file = 'c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html';
let content = fs.readFileSync(file, 'utf8');

// Use regex to replace the single quotes with backticks for the specific line
// Target: postControlsHtml = '<li class="control-item"><span class="control-text" style="color: var(--text-primary); font-style: italic;">${t('widget_no_changes_req')}</span></li>';

content = content.replace(/postControlsHtml = '<li class="control-item"><span class="control-text" style="color: var\(--text-primary\); font-style: italic;">\${t\('widget_no_changes_req'\)}<\/span><\/li>';/g, 'postControlsHtml = `<li class="control-item"><span class="control-text" style="color: var(--text-primary); font-style: italic;">${t(\'widget_no_changes_req\')}</span></li>`;');

fs.writeFileSync(file, content, 'utf8');
console.log("Syntax error in toggleEvaluationDetails fixed!");
