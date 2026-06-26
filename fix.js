const fs = require('fs');
const file = 'c:/ANTIGRAVITY IDE FOLDER/Dashboard Mitigasi Risiko Terintegrasi/index.html';
let content = fs.readFileSync(file, 'utf8');

// 1. Fix the syntax error in toggleEvaluationDetails and restore my color fixes
content = content.replace(
  `postControlsHtml = '<li class="control-item"><span class="control-text" style="color: var(--text-muted, #999); font-style: italic;">\${t('widget_no_changes_req')}</span></li>';`,
  "postControlsHtml = `<li class=\"control-item\"><span class=\"control-text\" style=\"color: var(--text-primary); font-style: italic;\">${t('widget_no_changes_req')}</span></li>`;"
);

// Fix PRE-CONTROLS and POST-CONTROLS colors which were reverted
content = content.replace(
  `<div style="font-size: 0.85rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text-muted, #777);">\${t('widget_pre_controls')}</div>`,
  `<div style="font-size: 0.85rem; font-weight: 600; margin-bottom: 0.5rem; color: var(--text-primary);">\${t('widget_pre_controls')}</div>`
);

content = content.replace(
  `<div style="font-size: 0.85rem; font-weight: 600; margin: 1rem 0 0.5rem 0; color: var(--text-muted, #777);">\${t('widget_post_controls')}</div>`,
  `<div style="font-size: 0.85rem; font-weight: 600; margin: 1rem 0 0.5rem 0; color: var(--text-primary);">\${t('widget_post_controls')}</div>`
);

// 2. Fix the CSS block. The user pasted a hardcoded block that breaks dark mode.
const oldCssBlock = `.eval-widget { font-family: system-ui, -apple-system, sans-serif; color: var(--text, #333); margin-top: 2rem; margin-bottom: 2rem; }
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
  .badge-rejected { background: #dc2626; color: white; }`;

const newCssBlock = `.eval-widget { font-family: system-ui, -apple-system, sans-serif; color: var(--text-primary); margin-top: 2rem; margin-bottom: 2rem; }
  .eval-filter-bar { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
  .eval-filter-btn { padding: 0.5rem 1rem; border: 1px solid var(--border-subtle); border-radius: 999px; background: var(--bg-base); color: var(--text-primary); cursor: pointer; font-size: 0.9rem; transition: all 0.2s; }
  .eval-filter-btn:hover { background: rgba(29, 158, 117, 0.1); border-color: var(--accent-primary); }
  .eval-filter-btn.active { background: var(--accent-primary); color: #fff; border-color: var(--accent-primary); }
  .eval-grid { display: flex; overflow-x: auto; gap: 1rem; margin-bottom: 1.5rem; padding-bottom: 1rem; }
  .eval-grid::-webkit-scrollbar { height: 8px; }
  .eval-grid::-webkit-scrollbar-track { background: transparent; }
  .eval-grid::-webkit-scrollbar-thumb { background: var(--text-tertiary); border-radius: 4px; }
  .eval-grid::-webkit-scrollbar-thumb:hover { background: var(--text-secondary); }
  .eval-card { background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 8px; padding: 1.25rem; cursor: pointer; transition: all 0.2s ease; position: relative; min-width: 300px; max-width: 350px; flex-shrink: 0; display: flex; flex-direction: column; justify-content: space-between; gap: 1rem;}
  .eval-card:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
  .eval-card.active { border-color: var(--accent-primary); box-shadow: 0 0 0 2px rgba(29, 158, 117, 0.2); }
  .eval-card-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem; }
  .eval-card-id { font-weight: 700; color: var(--accent-primary); font-size: 1.1rem; }
  .eval-card-title { font-size: 1.1rem; font-weight: 600; line-height: 1.3; color: var(--text-primary); }
  .eval-badge { padding: 0.25rem 0.6rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600; }
  .badge-mode { background: var(--bg-alt); color: var(--text-secondary); }
  .badge-changes { background: rgba(29, 158, 117, 0.15); color: var(--accent-primary); }
  .eval-card-badges { display: flex; gap: 0.5rem; flex-wrap: wrap; }
  
  .eval-detail-panel { background: var(--bg-surface); border: 1px solid var(--accent-primary); border-radius: 8px; padding: 1.5rem; margin-top: 1rem; animation: slideDown 0.3s ease-out; }
  .eval-detail-header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 1rem; margin-bottom: 1.5rem; border-bottom: 1px solid var(--border-subtle); }
  .eval-detail-title { font-size: 1.2rem; font-weight: 700; color: var(--text-primary); }
  .eval-close-btn { background: none; border: none; color: var(--text-secondary); cursor: pointer; transition: color 0.2s; padding: 0.5rem; border-radius: 4px; }
  .eval-close-btn:hover { color: var(--text-primary); background: rgba(255, 255, 255, 0.1); }
  .eval-detail-cols { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1.5rem; }
  .eval-detail-col h4 { margin-top: 0; color: var(--accent-primary); font-size: 1rem; margin-bottom: 1rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 0.5rem; }
  .eval-detail-text { font-size: 0.95rem; line-height: 1.6; color: var(--text-primary); }
  
  .control-list { list-style: none; padding: 0; margin: 0; }
  .control-item { padding: 0.5rem; border-bottom: 1px solid var(--border-subtle); display: flex; gap: 0.5rem; justify-content: space-between; align-items: center; }
  .control-item:last-child { border-bottom: none; }
  .badge-status { padding: 0.2rem 0.5rem; border-radius: 999px; font-size: 0.75rem; }
  .badge-added { background: rgba(29, 158, 117, 0.2); color: #20c997; font-weight: 600; border: 1px solid rgba(29, 158, 117, 0.3); padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; }
  .badge-rejected { background: rgba(220, 38, 38, 0.2); color: #f87171; font-weight: 600; border: 1px solid rgba(220, 38, 38, 0.3); padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; }`;

content = content.replace(oldCssBlock, newCssBlock);

// 3. Fix the `evaluation: { "en": ... }` to correctly represent languages without question marks.
const enEvalMatch = content.match(/"en": \`# Artifact Evaluation\n## Metodologi Evaluasi[\s\S]*?`\n\s*}/);

const enText = `# 3-Stage Validation Roadmap
## Evaluation Methodology

The Evaluation Phase is conducted through a series of structured activities involving evaluations from Experts (Internal and External) with the following detailed stages:

**1. Expert Judgment (Likert Scale)**
: The first step is to present the conceptual artifacts to the experts. The experts are asked to provide a descriptive quantitative assessment of the model's relevance using a Likert Scale questionnaire with a 4-point range to avoid midpoint ambivalence bias. The scale used consists of:
- **(1)** Highly Irrelevant
- **(2)** Irrelevant
- **(3)** Relevant
- **(4)** Highly Relevant

**2. Focus Group Discussion (FGD)**
: The results of the descriptive quantitative assessment that are deemed highly irrelevant and irrelevant by the experts are then discussed in more depth through guided discussions. This discussion aims to explore the underlying reasons behind the assessment, such as *"why is the component considered irrelevant?"* or *"Where does the model fall short?"*, to obtain concrete narrative qualitative feedback.

**3. Participant Validation**
: The final validation stage is to review the revised artifacts. This activity involves the same experts to review the improvements and reach a final agreement that the revised artifacts are relevant for use as cybersecurity risk management guidelines in the DetereCo environment. After an agreement is reached, the research proceeds to drawing Conclusions and Recommendations.

---

## Expert Judgment Questionnaire Results

| Threat Type | Scale 1 | Scale 2 | Scale 3 | Scale 4 | Scale Mode | Interpretation |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T.10 Industrial Espionage | 0 | 0 | 3 | 6 | **4** | ✅ Highly Relevant |
| T.11 Disaster | 0 | 0 | 4 | 5 | **4** | ✅ Highly Relevant |
| T.09 Ransomware & Malware Injection | 0 | 0 | 4 | 5 | **4** | ✅ Highly Relevant |
| T.04 API & Integration Vulnerabilities | 0 | 0 | 5 | 4 | **3** | ✅ Relevant |
| T.07 Replay Attacks | 0 | 0 | 2 | 7 | **4** | ✅ Highly Relevant |
| T.02 Insider Threats | 0 | 1 | 6 | 2 | **3** | ✅ Relevant |
| T.03 Supply Chain Attacks | 0 | 0 | 5 | 4 | **3** | ✅ Relevant |
| T.05 Lateral Movement | 0 | 0 | 4 | 5 | **4** | ✅ Highly Relevant |
| T.08 Advanced Persistent Threats (APT) | 0 | 0 | 4 | 5 | **4** | ✅ Highly Relevant |
| T.01 Compromised Credentials | 0 | 0 | 3 | 6 | **4** | ✅ Highly Relevant |
| T.06 IoT/OT Vulnerabilities | 0 | 0 | 5 | 4 | **3** | ✅ Relevant |

<!-- WIDGET_PLACEHOLDER -->

## Participant Validation Results

| Threat Type | Validation Result |
|---|:---:|
| T.10 Industrial Espionage | ✅ Agreed |
| T.11 Disaster | ✅ Agreed |
| T.09 Ransomware & Malware Injection | ✅ Agreed |
| T.04 API & Integration Vulnerabilities | ✅ Agreed |
| T.07 Replay Attacks | ✅ Agreed |
| T.02 Insider Threats | ✅ Agreed |
| T.03 Supply Chain Attacks | ✅ Agreed |
| T.05 Lateral Movement | ✅ Agreed |
| T.08 Advanced Persistent Threats (APT) | ✅ Agreed |
| T.01 Compromised Credentials | ✅ Agreed |
| T.06 IoT/OT Vulnerabilities | ✅ Agreed |

> **All 11 threats were AGREED UPON** by the experts after the Expert Judgment, FGD, and Participant Validation processes.

---

## Summary of ISO 27002:2022 Control Changes

| ID | Threat Type | Controls Added |
|---|---|---|
| T.10 | Industrial Espionage | 8.1 User endpoint devices |
| T.11 | Disaster | *(no changes)* |
| T.09 | Ransomware & Malware Injection | 8.15 Logging |
| T.04 | API & Integration Vulnerabilities | 8.27 Secure System Architecture · 5.12 Classification of Information |
| T.07 | Replay Attacks | *(no changes)* |
| T.02 | Insider Threats | 6.2 Terms and conditions of employment · 5.32 Intellectual Property Rights · 7.2 Physical Entry |
| T.03 | Supply Chain Attacks | 5.20 Supplier agreements · 6.7 Remote Working |
| T.05 | Lateral Movement | 8.16 Monitoring activities · 8.7 Protection against malware |
| T.08 | APT | 5.7 Threat intelligence |
| T.01 | Compromised Credentials | *(no changes)* |
| T.06 | IoT/OT Vulnerabilities | 5.14 Information Transfer · 5.15 Access Control · 8.22 Segregation of Networks |
`;

if (enEvalMatch) {
  const indonesianText = enEvalMatch[0].replace(/"en": `/, '').replace(/`\n\s*}$/, '');
  const replacement = `"en": \`${enText}\`,\n        "id": \`${indonesianText}\`,\n        "zh": \`${enText}\`,\n        "es": \`${enText}\`,\n        "fr": \`${enText}\`,\n        "de": \`${enText}\`,\n        "ar": \`${enText}\`,\n        "ru": \`${enText}\`,\n        "ko": \`${enText}\`,\n        "ja": \`${enText}\`\n      }`;
  content = content.replace(enEvalMatch[0], replacement);
}

fs.writeFileSync(file, content, 'utf8');
console.log("Done fixing syntax error, restoring CSS, and fixing question marks!");
