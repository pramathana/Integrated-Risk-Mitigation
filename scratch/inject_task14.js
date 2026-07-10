const fs = require('fs');
let c = fs.readFileSync('index.html', 'utf8');

// 1. Add jump button to view-dashboard
const btnHtml = `
      <div style="margin-top: 3rem; text-align: center; margin-bottom: 2rem;">
        <button class="menu-btn" onclick="switchView('view-dashboard-after'); setTimeout(() => { document.querySelector('.comparison-section').scrollIntoView({behavior:'smooth'}); }, 100);" style="padding: 1rem 2rem; font-size: 1rem; border-radius: 99px; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;" data-i18n="btn_view_comparison">
          Lihat Perbandingan Lengkap <i class="ph ph-arrow-right"></i>
        </button>
      </div>
    </div>`;
// Replace the exact closing of view-dashboard
c = c.replace(/          <div id="sankey-chart" style="width: 100%; height: 800px"><\/div>\s*<\/div>\s*<\/div>\s*<\/div>/g, 
`          <div id="sankey-chart" style="width: 100%; height: 800px"></div>
          <p class="chart-caption" data-i18n="caption_sankey_before" style="margin-top: 1rem;">
            Mapping of the 11 priority threats to ISO 27005 risk events, asset targets, and COBIT 2019 governance weaknesses before mitigation.
          </p>
        </div>
      </div>${btnHtml}`);

// 2. Add comparison section CSS -- already added!

// 3. Update updateMetrics in JS
// Find updateMetrics function and append comparison updates
c = c.replace(/(document\.getElementById\("val-low"\s*\+\s*suffix\)\.textContent\s*=\s*low;)/, 
`$1
      if (suffix === "") {
        const cb = document.getElementById("val-total-compare-before");
        if (cb) cb.textContent = rows.length;
      } else if (suffix === "-after") {
        const ca = document.getElementById("val-total-compare-after");
        if (ca) ca.textContent = rows.length;
      }`);

fs.writeFileSync('index.html', c);
console.log('Task 14 injected');
