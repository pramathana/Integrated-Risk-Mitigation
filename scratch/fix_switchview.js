const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
let newHtml = html;

// Remove the incorrect one
newHtml = newHtml.replace(`      document.getElementById("view-dashboard").style.display = "none";
      document.getElementById("view-dashboard-after").style.display = "none";
      document.getElementById("view-evaluation").style.display = "none";

      const nodesMap = new Map();`, `      const nodesMap = new Map();`);

// Add the correct one
newHtml = newHtml.replace(`      document.getElementById("view-dashboard").style.display = "none";
      document.getElementById("view-dashboard-after").style.display = "none";

      document.getElementById(viewId).style.display = "block";`, `      document.getElementById("view-dashboard").style.display = "none";
      document.getElementById("view-dashboard-after").style.display = "none";
      document.getElementById("view-evaluation").style.display = "none";

      document.getElementById(viewId).style.display = "block";`);

fs.writeFileSync('index.html', newHtml, 'utf8');
