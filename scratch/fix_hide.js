const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// The problematic line is hiding view-evaluation in renderSankey
// Let's remove it.
html = html.replace('document.getElementById("view-evaluation").style.display = "none";', '');

// Wait! I should ensure I don't remove it from switchView()
// Let's replace ONLY the one inside renderSankey.
// The one in renderSankey is grouped with view-dashboard.

html = html.replace(
  'document.getElementById("view-dashboard-after").style.display = "none";\n      document.getElementById("view-evaluation").style.display = "none";',
  'document.getElementById("view-dashboard-after").style.display = "none";'
);
// Handle CRLF just in case
html = html.replace(
  'document.getElementById("view-dashboard-after").style.display = "none";\r\n      document.getElementById("view-evaluation").style.display = "none";',
  'document.getElementById("view-dashboard-after").style.display = "none";'
);

fs.writeFileSync('index.html', html, 'utf8');
