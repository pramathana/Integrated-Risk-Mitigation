const fs = require('fs');
const file = 'c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html';
let content = fs.readFileSync(file, 'utf8');

// 1. Fix the extra closing brace before renderEvaluationGrid
content = content.replace(`        renderEvaluationGrid('all');
        if (typeof currentLang !== 'undefined') applyLanguage(currentLang);
      }
    }
    }

    function renderEvaluationGrid(filter) {`, `        renderEvaluationGrid('all');
        if (typeof currentLang !== 'undefined') applyLanguage(currentLang);
      }
    }

    function renderEvaluationGrid(filter) {`);

// 2. Fix the syntax error in toggleEvaluationDetails (single quotes -> backticks)
content = content.replace(`      if (item.postControls.length === 0) {
        postControlsHtml = '<li class="control-item"><span class="control-text" style="color: var(--text-primary); font-style: italic;">\${t('widget_no_changes_req')}</span></li>';
      }`, `      if (item.postControls.length === 0) {
        postControlsHtml = \`<li class="control-item"><span class="control-text" style="color: var(--text-primary); font-style: italic;">\${t('widget_no_changes_req')}</span></li>\`;
      }`);

fs.writeFileSync(file, content, 'utf8');
console.log("Syntax errors fixed!");
