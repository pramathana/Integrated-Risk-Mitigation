const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// 1. Remove the injected switchView and restore translations
const badInjection = `"fr": "5.9 Inventaire des informations et autres actifs associés",
"ko": "5.9 정보 및 기타 관련 자산 목록",
        "ja": "5.9 情報およびその他の関連資産のインベントリ"
      }
    };

    function switchView(viewName) {
      document.getElementById("view-home").style.display = "none";
      document.getElementById("view-research").style.display = "none";
      document.getElementById("view-criteria").style.display = "none";
      document.getElementById("view-assessment").style.display = "none";
      document.getElementById("view-priority").style.display = "none";
      document.getElementById("view-dashboard").style.display = "none";
      document.getElementById("view-evaluation").style.display = "none";
      document.getElementById("view-dashboard-after").style.display = "none";

      document.getElementById(viewName).style.display = "block";
    }`;

const goodOriginal = `"fr": "5.9 Inventaire des informations et autres actifs associés",
        "de": "5.9 Inventar von Informationen und anderen damit verbundenen Vermögenswerten",
        "ar": "5.9 جرد المعلومات والأصول المرتبطة الأخرى",
        "ru": "5.9 Инвентаризация информации и других связанных активов",
        "ko": "5.9 정보 및 기타 관련 자산 목록",
        "ja": "5.9 情報およびその他の関連資産のインベントリ"
      }
    };`;

html = html.replace(badInjection, goodOriginal);
html = html.replace(badInjection.replace(/\n/g, '\r\n'), goodOriginal.replace(/\n/g, '\r\n'));

// 2. Patch the REAL switchView
const oldSwitch = `    function switchView(viewId) {
      document.getElementById("view-home").style.display = "none";
      document.getElementById("view-research").style.display = "none";
      document.getElementById("view-criteria").style.display = "none";
      document.getElementById("view-assessment").style.display = "none";
      document.getElementById("view-priority").style.display = "none";
      document.getElementById("view-dashboard").style.display = "none";
      document.getElementById("view-dashboard-after").style.display = "none";`;

const newSwitch = `    function switchView(viewId) {
      document.getElementById("view-home").style.display = "none";
      document.getElementById("view-research").style.display = "none";
      document.getElementById("view-criteria").style.display = "none";
      document.getElementById("view-assessment").style.display = "none";
      document.getElementById("view-priority").style.display = "none";
      document.getElementById("view-dashboard").style.display = "none";
      document.getElementById("view-evaluation").style.display = "none";
      document.getElementById("view-dashboard-after").style.display = "none";`;

html = html.replace(oldSwitch, newSwitch);
html = html.replace(oldSwitch.replace(/\n/g, '\r\n'), newSwitch.replace(/\n/g, '\r\n'));

fs.writeFileSync('index.html', html, 'utf8');
console.log("Done.");
