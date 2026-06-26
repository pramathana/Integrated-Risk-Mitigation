const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const regex = /(document\.getElementById\("md-priority"\)\.innerHTML = marked\.parse\([\s\S]*?embeddedMarkdown\.priority\.en,\s*\);)/;

const replacement = `$1
        if (document.getElementById("md-evaluation")) {
          document.getElementById("md-evaluation").innerHTML = marked.parse(
            embeddedMarkdown.evaluation[lang] || embeddedMarkdown.evaluation.en,
          );
        }`;

if (!html.includes('md-evaluation").innerHTML')) {
    html = html.replace(regex, replacement);
    fs.writeFileSync('index.html', html, 'utf8');
    console.log('Fixed renderMarkdown successfully');
} else {
    console.log('Already fixed.');
}
