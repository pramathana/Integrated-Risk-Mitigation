# Integrated Risk Mitigation Program Dashboard

Dashboard interaktif hasil skripsi (Bachelor's Thesis) — *Design of a Cyber Security Risk Management Model Based on COBIT 2019 and Zero Trust Architecture for Risk Mitigation in the Aerospace Industry: A Case Study of Detereco.*

**Author:** Stefanus Jesano Pramathana — Bachelor's Program in Information Systems, Faculty of Industrial Engineering, Telkom University (2026)

🔗 **Live Demo:** https://pramathana.github.io/Integrated-Risk-Mitigation/

## Ringkasan

Dashboard ini memetakan 11 ancaman risiko keamanan siber menggunakan kombinasi framework COBIT 2019, Zero Trust Architecture (ZTA) Tenets, dan ISO 27002 Controls, dilengkapi visualisasi before/after mitigasi risiko.

## Fitur

- Dashboard interaktif dengan tema gelap/terang
- Dukungan 10 bahasa (EN, ID, ZH, ES, FR, DE, AR, RU, KO, JA)
- Visualisasi data: doughnut chart, bar chart, Sankey diagram
- Perbandingan level risiko sebelum & sesudah mitigasi
- Ringkasan evaluasi artifact oleh pakar

## Tech Stack

- HTML5, CSS3 (custom properties/theming), Vanilla JavaScript
- [Chart.js](https://www.chartjs.org/) — grafik doughnut & bar
- [Apache ECharts](https://echarts.apache.org/) — Sankey diagram
- [Marked.js](https://marked.js.org/) — render konten Markdown
- [Phosphor Icons](https://phosphoricons.com/)

## Struktur Repo

```
├── index.html              # Dashboard utama (single-page app)
├── *.md                     # Konten narasi tiap section (di-render via marked.js)
├── *.png                    # Aset gambar (logo, diagram)
├── README.md
├── LICENSE
└── .gitignore
```

## Cara Menjalankan Lokal

```bash
git clone https://github.com/pramathana/Integrated-Risk-Mitigation.git
cd Integrated-Risk-Mitigation
# Buka index.html langsung di browser, atau gunakan local server:
python -m http.server 8000
# lalu akses http://localhost:8000
```

## Kontak

- Email: jesano.pramathana@gmail.com
- LinkedIn: [/in/jesanopramathana](https://www.linkedin.com/in/jesanopramathana/)

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
