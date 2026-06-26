const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const target = `      document.getElementById("view-dashboard").style.display = "none";
      document.getElementById("view-dashboard-after").style.display = "none";`;

html = html.replace(target, '');
html = html.replace(target.replace(/\n/g, '\r\n'), '');

fs.writeFileSync('index.html', html, 'utf8');
console.log("Cleaned renderSankey.");
