const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// 1. Fix Light/Dark mode colors for md-evaluation-top and md-evaluation-bottom
const oldCSS = `#md-evaluation, 
    #md-evaluation * {
      color: #FFFFFF !important;
    }

    [data-theme="light"] #md-evaluation, 
    [data-theme="light"] #md-evaluation * {
      color: #000000 !important;
    }`;

const newCSS = `#md-evaluation-top, #md-evaluation-bottom,
    #md-evaluation-top *, #md-evaluation-bottom * {
      color: #FFFFFF !important;
    }

    [data-theme="light"] #md-evaluation-top, 
    [data-theme="light"] #md-evaluation-bottom,
    [data-theme="light"] #md-evaluation-top *,
    [data-theme="light"] #md-evaluation-bottom * {
      color: #000000 !important;
    }`;

if (html.includes(oldCSS)) {
    html = html.replace(oldCSS, newCSS);
} else {
    // If not exact match, just try to replace the first part
    html = html.replace(/#md-evaluation,\s*#md-evaluation \*\s*\{\s*color:\s*#FFFFFF !important;\s*\}/g, `#md-evaluation-top, #md-evaluation-top *, #md-evaluation-bottom, #md-evaluation-bottom * { color: #FFFFFF !important; }`);
    html = html.replace(/\[data-theme="light"\] #md-evaluation,\s*\[data-theme="light"\] #md-evaluation \*\s*\{\s*color:\s*#000000 !important;\s*\}/g, `[data-theme="light"] #md-evaluation-top, [data-theme="light"] #md-evaluation-top *, [data-theme="light"] #md-evaluation-bottom, [data-theme="light"] #md-evaluation-bottom * { color: #000000 !important; }`);
}

// 2. Inject Widget CSS
const widgetCSS = `
  /* Artifact Evaluation Interactive Widget */
  .eval-widget { font-family: system-ui, -apple-system, sans-serif; color: var(--text, #333); margin-top: 2rem; margin-bottom: 2rem; }
  .eval-filter-bar { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
  .eval-filter-btn { padding: 0.5rem 1rem; border: 1px solid var(--border-color, #ccc); border-radius: 999px; background: var(--card-bg, #fff); color: var(--text, #333); cursor: pointer; font-size: 0.9rem; transition: all 0.2s; }
  .eval-filter-btn:hover { background: #e0f2ec; border-color: #1D9E75; }
  .eval-filter-btn.active { background: #1D9E75; color: white; border-color: #1D9E75; }
  .eval-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; margin-bottom: 1.5rem; }
  .eval-card { border: 1px solid var(--border-color, #e0e0e0); border-radius: 12px; padding: 1.5rem; background: var(--card-bg, #fff); cursor: pointer; transition: all 0.2s; display: flex; flex-direction: column; justify-content: space-between; gap: 1rem; position: relative; }
  .eval-card:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
  .eval-card.active { border-color: #1D9E75; box-shadow: 0 0 0 2px rgba(29, 158, 117, 0.2); }
  .eval-card-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem; }
  .eval-card-id { font-weight: 700; color: #1D9E75; font-size: 1.1rem; }
  .eval-card-title { font-size: 1.1rem; font-weight: 600; line-height: 1.3; color: var(--text, #333); }
  .eval-badge { padding: 0.25rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }
  .badge-mode { background: #f3f4f6; color: #4b5563; }
  [data-theme="dark"] .badge-mode { background: #374151; color: #d1d5db; }
  .badge-changes { background: #e0f2ec; color: #1D9E75; }
  .eval-card-badges { display: flex; gap: 0.5rem; flex-wrap: wrap; }
  
  .eval-detail-panel { background: var(--card-bg, #fff); border: 1px solid #1D9E75; border-radius: 12px; padding: 1.5rem; margin-top: 1rem; animation: slideDown 0.3s ease-out; }
  .eval-detail-cols { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; }
  .eval-detail-col h4 { margin-top: 0; color: #1D9E75; font-size: 1rem; margin-bottom: 1rem; border-bottom: 1px solid #e0e0e0; padding-bottom: 0.5rem; }
  [data-theme="dark"] .eval-detail-col h4 { border-bottom-color: #444; }
  .eval-detail-text { font-size: 0.95rem; line-height: 1.6; color: var(--text, #333); }
  
  .control-list { list-style: none; padding: 0; margin: 0; }
  .control-list li { padding: 0.75rem; margin-bottom: 0.5rem; border-radius: 8px; font-size: 0.9rem; display: flex; justify-content: space-between; align-items: center; border: 1px solid var(--border-color, #e0e0e0); }
  .status-added { color: #1D9E75; background: rgba(29, 158, 117, 0.1); border-color: rgba(29, 158, 117, 0.2) !important; font-weight: 600; }
  .status-rejected { color: #dc2626; background: rgba(220, 38, 38, 0.1); border-color: rgba(220, 38, 38, 0.2) !important; font-weight: 600; }
  .badge-status { padding: 0.2rem 0.5rem; border-radius: 999px; font-size: 0.75rem; }
  .badge-added { background: #1D9E75; color: white; }
  .badge-rejected { background: #dc2626; color: white; }
  
  @keyframes slideDown { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }
  
  @media (max-width: 1024px) {
    .eval-detail-cols { grid-template-columns: 1fr; gap: 1rem; }
  }
`;

if (!html.includes('.eval-widget { font-family:')) {
    html = html.replace('</style>', widgetCSS + '\n  </style>');
}

fs.writeFileSync('index.html', html, 'utf8');
