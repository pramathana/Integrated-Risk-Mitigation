const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Replace single-quoted string containing template literal with backtick-quoted string
let targetStr = "'<li class=\"control-item\"><span class=\"control-text\" style=\"color: var(--text-muted, #999); font-style: italic;\">${t(\\'widget_no_changes_req\\')}</span></li>'";
let replacementStr = "`<li class=\"control-item\"><span class=\"control-text\" style=\"color: var(--text-muted, #999); font-style: italic;\">${t('widget_no_changes_req')}</span></li>`";

html = html.replace(targetStr, replacementStr);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Replaced successfully!');
