const fs = require('fs');
const file = 'c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html';
let content = fs.readFileSync(file, 'utf8');

// Replace the extra } at the end of initEvaluationWidget
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

fs.writeFileSync(file, content, 'utf8');
console.log("Removed extra } syntax error!");
