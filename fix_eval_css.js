const fs = require('fs');

let content = fs.readFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', 'utf8');

// 1 & 3 & 4. Text colors in Dark Mode
const darkThemeAdditions = `
    [data-theme="dark"] .eval-card,
    [data-theme="dark"] .eval-card-title,
    [data-theme="dark"] .eval-detail-panel,
    [data-theme="dark"] .eval-col-content,
    [data-theme="dark"] .control-text,
    [data-theme="dark"] .eval-detail-title {
      color: #FFFFFF !important;
    }
    
    [data-theme="dark"] .eval-col h4 {
      color: #FFFFFF !important;
      border-bottom: 2px solid rgba(255, 255, 255, 0.2) !important;
    }

    [data-theme="dark"] .eval-filter-btn {
      background: #121212 !important;
      border-color: #333 !important;
      color: #FFFFFF !important;
    }
    
    [data-theme="dark"] .eval-filter-btn:hover {
      background: #333 !important;
    }

    [data-theme="dark"] .eval-filter-btn.active {
      background: var(--accent-primary) !important;
      color: #FFFFFF !important;
    }

    [data-theme="dark"] .control-item {
      border-bottom: 1px solid #444 !important;
    }
    
    [data-theme="dark"] .eval-grid::-webkit-scrollbar-thumb {
      background: #444 !important;
    }
    
    [data-theme="dark"] .eval-grid::-webkit-scrollbar-track {
      background: #1e1e1e !important;
    }
`;

// Insert the new dark mode styles right before </style>
if (content.includes(darkThemeAdditions)) {
    console.log("Already added");
} else {
    content = content.replace('</style>', darkThemeAdditions + '\n  </style>');
    fs.writeFileSync('c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html', content, 'utf8');
    console.log("CSS fixes applied!");
}
