const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const targetStr = `    .md-content img {
      max-width: 100%;
      height: auto;
      border-radius: 12px;
      margin: 1.5rem auto;
      display: block;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
      border: 1px solid var(--border-subtle);
    }

    <header>`;

const replacementStr = `    .md-content img {
      max-width: 100%;
      height: auto;
      border-radius: 12px;
      margin: 1.5rem auto;
      display: block;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
      border: 1px solid var(--border-subtle);
    }

    #md-research p,
    #md-research ul,
    #md-research ol,
    #md-research li,
    #md-research td,
    #md-research th,
    #md-research blockquote {
      color: var(--text-primary) !important;
    }

    #md-evaluation, 
    #md-evaluation * {
      color: #FFFFFF !important;
    }

    [data-theme="light"] #md-evaluation, 
    [data-theme="light"] #md-evaluation * {
      color: #000000 !important;
    }
  </style>
</head>

<body>
  <div class="dashboard-container">
    <header>`;

html = html.replace(targetStr, replacementStr);
fs.writeFileSync('index.html', html, 'utf8');
console.log('Restored broken HTML and added CSS correctly.');
