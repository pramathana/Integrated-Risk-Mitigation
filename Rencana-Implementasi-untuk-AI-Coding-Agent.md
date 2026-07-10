# 🛠️ Implementation Plan: Dashboard Skripsi Improvements
### Target file utama: `index.html` (root repo `Integrated-Risk-Mitigation`)
### Ditujukan untuk: AI coding agent (Claude Code / Cursor / Copilot Agent, dll.) yang akan mengeksekusi perubahan langsung di IDE

---

## 0. Cara Membaca Dokumen Ini

Setiap task punya format tetap:

- **ID & Judul** — identifier unik, referensikan di commit message.
- **Prioritas** — 🔴 Tinggi / 🟠 Sedang / 🟡 Rendah.
- **File yang terpengaruh** — path relatif dari root repo.
- **Konteks saat ini** — kondisi kode sekarang (termasuk lokasi kira-kira di `index.html` bila diketahui).
- **Perubahan yang harus dilakukan** — instruksi eksplisit, termasuk contoh kode bila relevan.
- **Kriteria selesai (Acceptance Criteria)** — checklist yang harus lolos sebelum task dianggap selesai.

Kerjakan task **sesuai urutan nomor** kecuali dinyatakan lain — task nomor kecil adalah dependency/low-risk yang membuat task berikutnya lebih aman dikerjakan.

Agent **wajib**:
1. Membuat backup/branch baru sebelum mengedit (`git checkout -b feature/dashboard-polish`).
2. Tidak mengubah isi/struktur data konten (teks skripsi, angka risiko, hasil evaluasi) — task ini murni presentasi/kode, bukan konten riset.
3. Menjalankan pengecekan visual (buka `index.html` di browser, cek dark & light mode, cek lebar layar mobile ~375px) setelah setiap task UI selesai.
4. Tidak menghapus fungsi JS yang sudah ada (`switchView`, `toggleTheme`, `setLanguage`, chart rendering, dsb.) — hanya menambah/merapikan.

---

## 1. TASK-01 — Bersihkan File Development/Debug dari Root Repo

**Prioritas:** 🔴 Tinggi
**File yang terpengaruh:** seluruh root repo

**Konteks saat ini:**
Root repository berisi ±90 file bantuan development yang tidak relevan bagi pembaca akhir, contoh pola nama: `check_*.py` (mis. `check_alignment.py`, `check_css_again.py`, `check_widths.py`, `check_grid.py`, dst.), `add_*.py` / `add_*.js`, `extract_*.js`, `append_translations.js`, `apply_light_mode.py`, `compare_boxes.py`, file dump seperti `chunk_step_133_0.txt`, `evalData.txt`, `evalDataLast.txt`, `evalDataOriginal.txt`, `evalDataTarget.txt`, `evalDataTargetArray.js`, `eval_data.json`.

**Perubahan yang harus dilakukan:**
1. Buat folder baru `dev-archive/` di root.
2. Pindahkan (`git mv`) **semua** file berikut pola ini ke `dev-archive/`:
   - `check_*.py`, `check_*.js`
   - `add_*.py`, `add_*.js`
   - `extract_*.js`
   - `append_*.js`
   - `apply_*.py`
   - `compare_*.py`
   - `chunk_*.txt`
   - `evalData*.txt`, `evalData*.js`, `eval_data.json` — **kecuali** ada file di antaranya yang ternyata masih di-`fetch()` langsung oleh `index.html` saat runtime (cek dengan `grep -n "evalData\|eval_data" index.html` sebelum memindahkan; jika dipakai, JANGAN dipindah, biarkan di root).
3. Root repo setelah dibersihkan idealnya **hanya** berisi:
   - `index.html`
   - Aset gambar (`*.png`) yang benar-benar direferensikan `index.html`
   - File `.md` konten yang di-fetch dashboard via `marked.js` (cek dengan `grep -n "\.md" index.html` untuk memastikan file mana yang benar-benar dipakai, mis. `IT RISK ASSESSMENT.md`, `KRITERIA SKALA RISIKO.md`, `Reseach Overview Menu.md`, `Risk Mitigation After Revision.md`, `ZTA Tenet.md`, `daftar_risiko_prioritas.md`, `artifact_evaluation.md`)
   - `README.md`
   - `LICENSE`
   - `.gitignore`
4. Tambahkan folder `dev-archive/` ke `.gitignore` **atau** biarkan ter-commit tapi beri `dev-archive/README.md` singkat berisi: "Berkas ini adalah skrip bantuan development, tidak digunakan oleh dashboard final."

**Kriteria selesai:**
- [ ] `ls` di root hanya menampilkan file yang benar-benar dipakai oleh `index.html` + file dokumentasi standar.
- [ ] `index.html` dibuka di browser tetap berfungsi 100% normal (semua tab, semua chart, semua markdown ter-load) — pastikan tidak ada file `.md`/`.png`/`.js` yang justru masih dibutuhkan ikut terpindah dan menyebabkan 404.
- [ ] Tidak ada file bernama `check_*`, `chunk_*`, `debug_*`, `tmp_*` tersisa di root.

---

## 2. TASK-02 — Perbarui Judul Tab, Meta Description & Open Graph Tags

**Prioritas:** 🔴 Tinggi
**File yang terpengaruh:** `index.html` (bagian `<head>`, sekitar baris 1–20)

**Konteks saat ini:**
```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Dashboard RMP</title>
<link rel="icon" href="Privacy-Icon.png" type="image/png" />
```
Tidak ada `meta description`, tidak ada Open Graph/Twitter card tags.

**Perubahan yang harus dilakukan:**

Ganti `<title>` menjadi:
```html
<title>Integrated Risk Mitigation Program Dashboard | Stefanus Jesano Pramathana</title>
```

Tambahkan tepat setelah tag `<title>` (sebelum `<link rel="icon" ...>`):
```html
<meta name="description" content="Dashboard interaktif skripsi: Design of a Cyber Security Risk Management Model Based on COBIT 2019 and Zero Trust Architecture for Risk Mitigation in the Aerospace Industry — Studi Kasus Detereco. Oleh Stefanus Jesano Pramathana, Telkom University." />
<meta name="author" content="Stefanus Jesano Pramathana" />

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:title" content="Integrated Risk Mitigation Program Dashboard" />
<meta property="og:description" content="11 Threats mapped with COBIT 2019, ZTA Tenets, and ISO 27002 Controls — Bachelor's Thesis Dashboard, Telkom University 2026." />
<meta property="og:image" content="LOGO UNIVERSITAS TELKOM.png" />
<meta property="og:url" content="https://pramathana.github.io/Integrated-Risk-Mitigation/" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Integrated Risk Mitigation Program Dashboard" />
<meta name="twitter:description" content="Dashboard interaktif skripsi berbasis COBIT 2019 & Zero Trust Architecture untuk mitigasi risiko keamanan siber di industri aerospace." />
```

> Catatan untuk agent: sesuaikan `og:url` dengan URL GitHub Pages/hosting sebenarnya jika berbeda dari asumsi di atas — cari tahu dari README atau tanyakan ke user jika tidak ditemukan referensi URL live demo di repo.

**Kriteria selesai:**
- [ ] Tab browser menampilkan judul persis: `Integrated Risk Mitigation Program Dashboard | Stefanus Jesano Pramathana`
- [ ] Validasi meta tags dengan cara `view-source:` — pastikan tidak ada tag yang tidak tertutup / duplikat `<title>`.
- [ ] Semua tag baru diletakkan di dalam `<head>`, sebelum `</head>`.

---

## 3. TASK-03 — Favicon Custom

**Prioritas:** 🟡 Rendah
**File yang terpengaruh:** `index.html` (head), aset baru

**Konteks saat ini:**
```html
<link rel="icon" href="Privacy-Icon.png" type="image/png" />
```
Memakai ikon gembok generik, bukan identitas khusus proyek.

**Perubahan yang harus dilakukan:**
1. Jika tersedia aset baru dari user (mis. ikon perisai/shield bertema Zero Trust dengan warna aksen dashboard), simpan sebagai `favicon.png` di root, lalu update:
   ```html
   <link rel="icon" href="favicon.png" type="image/png" />
   ```
2. Jika **tidak ada aset baru disediakan user**, task ini **di-skip** — jangan membuat gambar baru secara otomatis tanpa aset sumber. Tandai sebagai "menunggu aset dari user" di commit message/PR description.

**Kriteria selesai:**
- [ ] Favicon baru tampil di tab browser **atau** task ditandai skip dengan alasan tidak ada aset.

---

## 4. TASK-04 — README.md Lengkap + `.gitignore` + `LICENSE`

**Prioritas:** 🔴 Tinggi
**File yang terpengaruh:** `README.md` (root), `.gitignore` (baru), `LICENSE` (baru)

**Konteks saat ini:**
`README.md` hanya berisi 2 baris (judul + 1 kalimat deskripsi). Tidak ada `.gitignore` maupun `LICENSE`.

**Perubahan yang harus dilakukan:**

1. Tulis ulang `README.md` dengan struktur berikut (isi placeholder `[...]` dengan info yang tersedia di `index.html`/konten repo; jika info tidak tersedia — mis. link live demo — tandai sebagai `<!-- TODO: isi link live demo -->` alih-alih mengarang):

```markdown
# Integrated Risk Mitigation Program Dashboard

Dashboard interaktif hasil skripsi (Bachelor's Thesis) — *Design of a Cyber Security Risk Management Model Based on COBIT 2019 and Zero Trust Architecture for Risk Mitigation in the Aerospace Industry: A Case Study of Detereco.*

**Author:** Stefanus Jesano Pramathana — Bachelor's Program in Information Systems, Faculty of Industrial Engineering, Telkom University (2026)

🔗 **Live Demo:** <!-- TODO: isi link GitHub Pages / hosting live -->

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
```

2. Buat file `.gitignore` baru berisi minimal:
```
.DS_Store
Thumbs.db
node_modules/
dev-archive/
*.log
```

3. Buat file `LICENSE` berisi teks standar **MIT License** dengan copyright holder: `Stefanus Jesano Pramathana`, tahun `2026`.

**Kriteria selesai:**
- [ ] `README.md` menampilkan semua section di atas, tidak ada placeholder `[...]` yang tertinggal tanpa penjelasan (boleh berupa `<!-- TODO -->` comment kalau memang datanya tidak tersedia).
- [ ] `LICENSE` valid format MIT, nama & tahun benar.
- [ ] `.gitignore` ter-commit di root.

---

## 5. TASK-05 — Perbaiki Menu Navigasi (10 Tab) untuk Layar Mobile

**Prioritas:** 🟠 Sedang
**File yang terpengaruh:** `index.html` — CSS `.menu-bar` (sekitar baris 468–475) dan `.menu-btn` (sekitar baris 476–498), plus tambahan media query.

**Konteks saat ini:**
```css
.menu-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 1rem;
}
```
10 tombol (`Home Page`, `Research Overview`, `Risk Criteria`, `Risk Assessment`, `Risk Priority`, `Artifact [Before Rev]`, `Artifact Evaluation`, `Artifact [After Rev]`, `Closing`, `Related Publications`, `Acknowledgment`) akan wrap ke banyak baris di layar sempit.

**Perubahan yang harus dilakukan:**

Tambahkan media query berikut setelah blok `.menu-btn.active` (jangan hapus CSS desktop yang sudah ada, ini murni override untuk mobile):

```css
@media (max-width: 768px) {
  .menu-bar {
    flex-wrap: nowrap;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x proximity;
    padding-bottom: 0.75rem;
  }

  .menu-bar::-webkit-scrollbar {
    height: 4px;
  }

  .menu-bar::-webkit-scrollbar-thumb {
    background: var(--border-subtle);
    border-radius: 4px;
  }

  .menu-btn {
    flex: 0 0 auto;
    scroll-snap-align: start;
    white-space: nowrap;
  }
}
```

Selain itu, tambahkan `sticky` positioning pada `.menu-bar` agar tetap terlihat saat halaman panjang di-scroll (berlaku untuk semua ukuran layar, bukan hanya mobile):

```css
.menu-bar {
  position: sticky;
  top: 0;
  background: var(--bg-base);
  z-index: 50;
}
```
> Tambahkan properti `position`, `top`, `background`, `z-index` ini ke dalam rule `.menu-bar` yang sudah ada (jangan buat rule baru terpisah), supaya tidak ada duplikasi selector.

**Kriteria selesai:**
- [ ] Pada viewport ≤768px, menu bar menjadi horizontal scroll (bukan wrap ke banyak baris), tombol tidak terpotong.
- [ ] Pada semua viewport, menu bar tetap terlihat (sticky) saat halaman di-scroll ke bawah, tidak menutupi konten (cek `z-index` tidak bentrok dengan modal/lightbox yang sudah ada — lightbox harus tetap di atas menu bar).
- [ ] Tidak ada regresi tampilan desktop (menu bar desktop tetap terlihat sama seperti sebelumnya).

---

## 6. TASK-06 — Perkuat Identitas Warna (Signature Palette)

**Prioritas:** 🟠 Sedang
**File yang terpengaruh:** `index.html` — `:root` dan `[data-theme="light"]` CSS variables (baris ±8–52)

**Konteks saat ini:**
```css
:root {
  --pub-subtitle-color: #38bdf8;
  --bg-base: #0f172a;
  --bg-surface: rgba(30, 41, 59, 0.7);
  --bg-surface-hover: rgba(51, 65, 85, 0.8);
  --border-subtle: rgba(255, 255, 255, 0.08);
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-tertiary: #64748b;
  --accent-primary: #3b82f6;
  --accent-glow: rgba(59, 130, 246, 0.2);
  ...
}
```
Warna aksen `#3b82f6` (blue-500 Tailwind default) adalah warna paling umum dipakai template dashboard — kurang punya identitas unik.

**Perubahan yang harus dilakukan:**

1. **JANGAN mengganti seluruh sistem warna** (berisiko merusak kontras yang sudah teruji di badge risiko dsb). Fokus hanya mengganti **`--accent-primary`** dan **`--accent-glow`** ke nuansa yang lebih personal, misalnya kombinasi *deep teal/cyan* bertema keamanan siber:

```css
:root {
  --accent-primary: #0ea5b7;   /* teal-cyan, nuansa "security/radar" */
  --accent-glow: rgba(14, 165, 183, 0.25);
}

[data-theme="light"] {
  --accent-primary: #0891a1;
  --accent-glow: rgba(8, 145, 161, 0.2);
}
```

2. Setelah mengganti, **cek manual** semua elemen yang memakai `var(--accent-primary)` (tombol aktif menu, link, badge, kartu kontak, chart) untuk memastikan kontras teks di atasnya (biasanya putih `#fff`) tetap memenuhi rasio kontras minimal 4.5:1 (WCAG AA). Gunakan tool kontrol kontras (mis. WebAIM Contrast Checker) bila perlu penyesuaian shade.

3. **Opsional (skip jika berisiko/tidak yakin):** tambahkan 1 elemen dekoratif SVG tipis (garis grid radar atau pola heksagonal, opacity rendah ~0.05) sebagai background di `<div class="dashboard-container">` atau `<header>` — hanya jika agent yakin tidak akan mengganggu keterbacaan konten di atasnya. Jika ragu, lewati bagian ini dan tandai sebagai "manual design task, butuh review visual designer".

**Kriteria selesai:**
- [ ] `--accent-primary` dan `--accent-glow` berubah di kedua tema (dark & light), seluruh dashboard konsisten memakai warna baru (tidak ada hardcoded `#3b82f6` tersisa — cek dengan `grep -n "#3b82f6" index.html`).
- [ ] Kontras teks putih di atas `--accent-primary` tetap lolos AA (≥4.5:1).
- [ ] Tidak ada perubahan pada warna badge risiko (`--risk-moderate-*`, `--risk-lowmod-*`, `--risk-low-*`) — task ini hanya menyentuh accent color.

---

## 7. TASK-07 — Ekstrak Inline Style Berulang Menjadi CSS Class Reusable

**Prioritas:** 🟠 Sedang
**File yang terpengaruh:** `index.html` — bagian `#view-home` (Contact Card, sekitar baris 2050–2135) dan `<style>` block

**Konteks saat ini:**
Elemen "contact row" (Phone, Email, LinkedIn) di Contact Card menulis style yang sama persis berulang 3 kali secara inline, contoh:
```html
<div style="display: flex; align-items: center; gap: 1.25rem; padding: 1rem 1.25rem; border-radius: 12px; background: var(--bg-base); border: 1px solid var(--border-subtle); transition: background 0.2s;"
  onmouseover="this.style.background='var(--bg-surface-hover)'"
  onmouseout="this.style.background='var(--bg-base)'">
```

**Perubahan yang harus dilakukan:**

1. Tambahkan class baru di `<style>` block:
```css
.contact-row {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 1rem 1.25rem;
  border-radius: 12px;
  background: var(--bg-base);
  border: 1px solid var(--border-subtle);
}

.contact-row:hover {
  background: var(--bg-surface-hover);
}

.contact-icon-badge {
  width: 42px;
  height: 42px;
  background: rgba(59, 130, 246, 0.15);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-primary);
  font-size: 1.25rem;
}
```
> Catatan: nilai `rgba(59, 130, 246, 0.15)` pada `.contact-icon-badge` sebaiknya ikut disesuaikan dengan `--accent-primary` baru dari TASK-06 — ganti menjadi `var(--accent-glow)` agar otomatis konsisten:
```css
.contact-icon-badge {
  background: var(--accent-glow);
}
```

2. Ganti ketiga blok `<div style="...">` contact row di HTML menjadi `<div class="contact-row">`, dan hapus atribut `onmouseover`/`onmouseout` (sudah digantikan `:hover` di CSS — CSS `transition` global sudah ada di selector `*` sehingga hover tetap smooth).

3. Ganti `<div style="width: 42px; height: 42px; ...">` (icon wrapper) menjadi `<div class="contact-icon-badge">`.

4. Lakukan hal serupa untuk pola berulang lain yang teridentifikasi sama persis 2× atau lebih (mis. badge `contact_position`/`contact_focus`/`contact_thesis` yang memakai style pill/badge identik) — buat class `.info-pill` untuk itu.

**Kriteria selesai:**
- [ ] Tidak ada lagi atribut `onmouseover`/`onmouseout` inline untuk efek hover yang sudah digantikan CSS.
- [ ] Visual akhir (warna, spacing, radius, hover effect) identik dengan sebelumnya — task ini refactor murni, tidak boleh mengubah tampilan.
- [ ] Class baru (`.contact-row`, `.contact-icon-badge`, `.info-pill`) didefinisikan sekali di `<style>`, dipakai berulang di HTML.

---

## 8. TASK-08 — Transisi Halus Saat Pindah Tab (View Switch)

**Prioritas:** 🟡 Rendah
**File yang terpengaruh:** `index.html` — fungsi `switchView()` di `<script>` (cari dengan `grep -n "function switchView" index.html`), plus tambahan CSS.

**Konteks saat ini:**
Pergantian tab dilakukan dengan toggle langsung `style.display = "none"` / `"block"` tanpa transisi, sehingga konten "muncul tiba-tiba".

**Perubahan yang harus dilakukan:**

1. Tambahkan CSS animasi baru (manfaatkan `@keyframes slideDown` yang sudah ada sebagai referensi pola, buat versi baru khusus tab content):
```css
@keyframes fadeInView {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.view-active-transition {
  animation: fadeInView 0.25s ease-out;
}
```

2. Di dalam fungsi `switchView(viewId)`, setelah baris yang menampilkan view target (`document.getElementById(viewId).style.display = "..."` atau sejenisnya), tambahkan:
```javascript
const activeView = document.getElementById(viewId);
activeView.classList.remove("view-active-transition"); // reset supaya animasi bisa retrigger
void activeView.offsetWidth; // force reflow agar class removal terdaftar browser
activeView.classList.add("view-active-transition");
```

3. **Jangan ubah logic show/hide yang sudah ada** (mis. logic yang menyembunyikan semua view lain) — task ini hanya menambahkan class animasi pada view yang baru ditampilkan.

**Kriteria selesai:**
- [ ] Setiap kali pindah tab via `.menu-btn`, konten baru muncul dengan fade+slide halus (~250ms), bukan langsung "meloncat".
- [ ] Tidak ada flicker atau delay yang mengganggu (durasi animasi tidak lebih dari 300ms).
- [ ] Fungsi `switchView` tetap berjalan normal untuk semua 11 view yang ada.

---

## 9. TASK-09 — Caption/Insight Singkat di Bawah Setiap Chart

**Prioritas:** 🟡 Rendah
**File yang terpengaruh:** `index.html` — sekitar `#riskDoughnutChart`, `#layerBarChart`, `#sankey-chart` dan versi `-after`-nya (baris ±2199–2300, 2356–2457)

**Konteks saat ini:**
Chart ditampilkan tanpa penjelasan teks pendamping, mis.:
```html
<div class="chart-container">
  <canvas id="riskDoughnutChart"></canvas>
</div>
```

**Perubahan yang harus dilakukan:**

Tambahkan elemen caption setelah setiap chart container, dengan `data-i18n` key baru (ikuti pola i18n yang sudah ada — cari objek translasi di `<script>` dan tambahkan key baru untuk tiap bahasa yang didukung, minimal EN dan ID; bahasa lain boleh menyusul):

```html
<div class="chart-container">
  <canvas id="riskDoughnutChart"></canvas>
  <p class="chart-caption" data-i18n="caption_doughnut_before">
    Distribusi 11 ancaman risiko berdasarkan tingkat keparahan sebelum mitigasi diterapkan.
  </p>
</div>
```

Tambahkan CSS:
```css
.chart-caption {
  font-size: 0.8rem;
  color: var(--text-tertiary);
  text-align: center;
  margin-top: 0.75rem;
  line-height: 1.4;
}
```

Lakukan hal yang sama untuk `layerBarChart`, `sankey-chart`, dan pasangan `-after`-nya, dengan teks caption yang disesuaikan konteks masing-masing (before/after, doughnut/bar/sankey). Tambahkan entry translasi baru ke objek i18n yang sudah ada di `<script>` (cari `const translations = {` atau nama variabel serupa) untuk tiap key caption baru, minimal untuk locale `en` dan `id`.

**Kriteria selesai:**
- [ ] Setiap dari 6 chart (doughnut, bar, sankey × before/after) punya 1 kalimat caption di bawahnya.
- [ ] Caption berubah sesuai bahasa aktif (minimal EN/ID berfungsi, bahasa lain boleh fallback ke EN jika translasi belum lengkap — jangan sampai menampilkan key kosong/`undefined`).
- [ ] Tidak mengubah ukuran/posisi canvas chart yang sudah ada.

---

## 10. TASK-10 — Skeleton Loader untuk Konten Markdown

**Prioritas:** 🟡 Rendah
**File yang terpengaruh:** `index.html` — elemen `.md-content` (`#md-research`, `#md-criteria`, `#md-assessment`, `#md-priority`, `#md-evaluation-*`) dan fungsi `renderMarkdown()`

**Konteks saat ini:**
```html
<div class="md-content" id="md-research">Loading...</div>
```
Teks "Loading..." polos tanpa indikasi visual progres.

**Perubahan yang harus dilakukan:**

1. Tambahkan CSS skeleton:
```css
.skeleton-line {
  height: 14px;
  border-radius: 6px;
  background: linear-gradient(90deg, var(--bg-surface) 25%, var(--bg-surface-hover) 50%, var(--bg-surface) 75%);
  background-size: 200% 100%;
  animation: skeletonShimmer 1.4s ease-in-out infinite;
  margin-bottom: 0.75rem;
}

.skeleton-line:nth-child(2) { width: 90%; }
.skeleton-line:nth-child(3) { width: 75%; }

@keyframes skeletonShimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

2. Ganti teks `Loading...` di setiap `.md-content` placeholder dengan markup skeleton:
```html
<div class="md-content" id="md-research">
  <div class="skeleton-line"></div>
  <div class="skeleton-line"></div>
  <div class="skeleton-line"></div>
</div>
```
Lakukan untuk semua elemen `.md-content` yang defaultnya `Loading...` (`#md-research`, `#md-criteria`, `#md-assessment`, `#md-priority`, `#md-evaluation-top-1`).

3. Pastikan fungsi `renderMarkdown()` (atau fungsi sejenis yang mem-fetch `.md` file lalu memasukkan hasil `marked.parse()` ke elemen ini) melakukan **replace total innerHTML** elemen target (bukan append), sehingga skeleton otomatis hilang begitu konten asli masuk. Cek implementasi saat ini dengan `grep -n "innerHTML" index.html` — jika sudah pakai `element.innerHTML = marked.parse(...)`, tidak perlu ubah logic, cukup pastikan behaviour ini konsisten di semua pemanggilan.

**Kriteria selesai:**
- [ ] Saat halaman pertama kali dimuat / tab markdown pertama kali dibuka, muncul 3 baris skeleton shimmer, bukan teks "Loading...".
- [ ] Skeleton otomatis tergantikan konten asli tanpa perlu refresh manual.
- [ ] Animasi shimmer tidak menyebabkan layout shift (tinggi skeleton mendekati tinggi teks asli).

---

## 11. TASK-11 — Optimasi Loading Script (defer + font preload)

**Prioritas:** 🟡 Rendah
**File yang terpengaruh:** `index.html` — `<head>`

**Konteks saat ini:**
```html
<script src="https://unpkg.com/@phosphor-icons/web"></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2"></script>
<script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```
Tidak ada atribut `defer`, berpotensi memblokir parsing HTML.

**Perubahan yang harus dilakukan:**

1. Tambahkan `defer` pada semua script tag CDN di atas:
```html
<script src="https://unpkg.com/@phosphor-icons/web" defer></script>
<script src="https://cdn.jsdelivr.net/npm/chart.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2" defer></script>
<script src="https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js" defer></script>
```

2. **PENTING — cek dependency order:** karena `defer` mempertahankan urutan eksekusi sesuai urutan tag (bukan sesuai kecepatan load), ini aman selama script custom (`<script>` inline yang memanggil `Chart`, `echarts`, `marked`) juga dijalankan setelah `DOMContentLoaded` (yang sudah jadi pola di file ini — lihat `document.addEventListener("DOMContentLoaded", init)`). Jika ada pemanggilan fungsi dari library ini **di luar** event listener `DOMContentLoaded`/`load`, agent harus membungkusnya juga, karena `defer` menunda eksekusi script sampai HTML selesai di-parse.

3. Tambahkan preload untuk font agar tidak ada flash of unstyled text:
```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" />
```
(letakkan sebelum tag `<link ... rel="stylesheet">` Google Fonts yang sudah ada, tag stylesheet asli tetap dipertahankan).

**Kriteria selesai:**
- [ ] Semua script CDN non-blocking (`defer`).
- [ ] Dashboard tetap berfungsi 100% normal setelah perubahan — **wajib** ditest ulang: buka setiap tab, pastikan semua chart (doughnut, bar, sankey) tetap render, ikon Phosphor tetap muncul, markdown tetap ter-parse.
- [ ] Tidak ada error di browser console terkait `undefined` variable dari library yang telat load.

---

## 12. TASK-12 — Tambahkan `aria-label` dan Dukungan Keyboard Navigation

**Prioritas:** 🟠 Sedang
**File yang terpengaruh:** `index.html` — `<header>` (tombol toggle tema, select bahasa) dan `.menu-btn` di menu bar

**Konteks saat ini:**
- Tombol toggle tema hanya punya `title="Toggle Theme"`, tanpa `aria-label`.
- Tidak ada `role="tablist"`/`role="tab"` pada sistem menu navigasi.
- 0 kemunculan `aria-label` di seluruh file.

**Perubahan yang harus dilakukan:**

1. Tombol toggle tema:
```html
<button id="themeToggleBtn" onclick="toggleTheme()" aria-label="Ganti tema terang/gelap" title="Toggle Theme" style="...">
```

2. Select bahasa:
```html
<select id="langSwitcher" onchange="setLanguage(this.value)" aria-label="Pilih bahasa tampilan" style="...">
```

3. Container menu bar:
```html
<div class="menu-bar" role="tablist" aria-label="Navigasi bagian dashboard">
```

4. Setiap `.menu-btn`, tambahkan `role="tab"` dan `aria-selected` (agent perlu menyesuaikan value `aria-selected` secara dinamis lewat JS di fungsi `switchView()`, defaultnya `"true"` hanya pada tombol dengan class `active`):
```html
<button class="menu-btn active" role="tab" aria-selected="true" data-view="view-home" data-i18n="menu_home" onclick="switchView('view-home')">
```
Untuk tombol lain, `aria-selected="false"`.

5. Di dalam fungsi `switchView()`, tambahkan logic update `aria-selected` setiap kali tab berpindah (sejalan dengan logic `classList` toggle `active` yang sudah ada — cari baris `document.querySelectorAll(".menu-btn").forEach((btn) => {` sebagai titik masuk, tambahkan `btn.setAttribute("aria-selected", btn.classList.contains("active") ? "true" : "false")` di dalam forEach yang sama).

6. Lightbox image viewer (`#lightbox`), tambahkan `role="dialog"` dan `aria-label="Tampilan gambar penuh layar"` pada container-nya, serta pastikan ada cara menutup dengan tombol `Escape` (cek apakah sudah ada listener keyboard; jika belum, tambahkan):
```javascript
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    document.getElementById("lightbox").style.display = "none";
  }
});
```
(sesuaikan dengan cara lightbox ditutup yang sudah ada di kode, jangan duplikasi logic close yang sudah ada — cek dulu fungsi close lightbox eksisting).

**Kriteria selesai:**
- [ ] Tombol tema & select bahasa punya `aria-label` yang deskriptif.
- [ ] Menu bar berperan sebagai `tablist` dengan `aria-selected` yang update dinamis sesuai tab aktif.
- [ ] Lightbox bisa ditutup dengan tombol `Escape` di keyboard.
- [ ] Tidak ada regresi fungsi (semua onclick/onchange yang sudah ada tetap bekerja).

---

## 13. TASK-13 — Perkecil Ukuran & Pisahkan CSS/JS dari HTML (Opsional, Effort Tinggi)

**Prioritas:** 🟡 Rendah — **kerjakan terakhir, hanya jika semua task di atas sudah selesai dan stabil**
**File yang terpengaruh:** `index.html` (8.242 baris) → dipecah menjadi `index.html` + `assets/css/style.css` + `assets/js/app.js`

**Konteks saat ini:**
Seluruh CSS (`<style>` block) dan JS (`<script>` inline, bukan CDN) berada dalam satu file `index.html` berukuran ~737 KB.

**Perubahan yang harus dilakukan:**

1. Buat folder `assets/css/` dan `assets/js/`.
2. Pindahkan **seluruh isi** `<style>...</style>` ke `assets/css/style.css`, ganti tag di `<head>` menjadi:
   ```html
   <link rel="stylesheet" href="assets/css/style.css" />
   ```
3. Pindahkan **seluruh isi** `<script>...</script>` custom (bukan tag `<script src="...">` CDN) ke `assets/js/app.js`, ganti dengan:
   ```html
   <script src="assets/js/app.js" defer></script>
   ```
   Letakkan tag ini **setelah** semua script CDN (Chart.js, ECharts, Marked.js, Phosphor) agar dependency tersedia saat `app.js` dieksekusi.
4. **WAJIB** setelah pemisahan: buka `index.html` di browser dan test **seluruh** fungsi (semua 11 tab, toggle tema, ganti 10 bahasa, semua chart, search & filter tabel, lightbox gambar) — pemisahan file adalah operasi berisiko tinggi untuk regresi jika ada typo saat memindahkan kode.
5. **Jangan minify** di langkah ini (minifikasi adalah task terpisah, opsional, dan tidak wajib untuk keperluan portofolio/sidang).

**Kriteria selesai:**
- [ ] `index.html` menjadi jauh lebih ringkas (hanya struktur HTML + link ke CSS/JS eksternal).
- [ ] Fungsi dashboard 100% identik dengan sebelum pemisahan (regression test manual per tab).
- [ ] Tidak ada script error di console akibat urutan load yang salah.

> **Catatan untuk agent:** Jika task ini terasa berisiko tinggi menjelang deadline sidang, boleh **ditunda/skip** dan cukup laporkan sebagai "not done — high risk near deadline" tanpa mengerjakannya. Tidak mengerjakan task ini tidak menghalangi task lain untuk selesai.

---

## 14. TASK-14 — Tampilan Perbandingan Before/After Mitigasi Berdampingan

**Prioritas:** 🟠 Sedang
**File yang terpengaruh:** `index.html` — tambahan section baru, bisa diletakkan di `#view-dashboard-after` (di bagian akhir, setelah chart existing) atau sebagai sub-section baru di `#view-closing`.

**Konteks saat ini:**
Tab `view-dashboard` (Before) dan `view-dashboard-after` (After) terpisah sepenuhnya — pengguna harus klik bolak-balik untuk membandingkan.

**Perubahan yang harus dilakukan:**

1. Tambahkan section baru di akhir `#view-dashboard-after` (setelah elemen `#sankey-chart-after`):
```html
<div class="comparison-section" style="margin-top: 3rem;">
  <h3 data-i18n="comparison_title" style="margin-bottom: 1.5rem;">Perbandingan Sebelum vs Sesudah Mitigasi</h3>
  <div class="comparison-grid">
    <div class="comparison-col">
      <h4 data-i18n="comparison_before_label">Sebelum Mitigasi</h4>
      <div class="metric-value" id="val-total-compare-before">0</div>
    </div>
    <div class="comparison-col">
      <h4 data-i18n="comparison_after_label">Sesudah Mitigasi</h4>
      <div class="metric-value" id="val-total-compare-after">0</div>
    </div>
  </div>
</div>
```

2. Tambahkan CSS:
```css
.comparison-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

@media (max-width: 768px) {
  .comparison-grid {
    grid-template-columns: 1fr;
  }
}

.comparison-col {
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  padding: 1.5rem;
  text-align: center;
}
```

3. Di JS, setelah data risiko before & after selesai dihitung (cari variabel/fungsi yang menghasilkan `val-total` dan `val-total-after` yang sudah ada — biasanya di fungsi `updateMetrics()` atau sejenis, cek dengan `grep -n "val-total" index.html`), tambahkan assignment nilai yang sama ke elemen baru `val-total-compare-before` dan `val-total-compare-after`, **atau** — lebih baik — render mini bar chart perbandingan total risiko per level (Moderate/Low-Mod/Low) before vs after menggunakan Chart.js grouped bar chart di dalam `.comparison-col`, memanfaatkan data yang sudah ada di variable state existing (jangan hitung ulang dari nol, reuse data source yang sudah dipakai chart before/after yang sudah ada).

4. Tambahkan tombol navigasi cepat di tab `view-dashboard` (Before) yang mengarah ke section komparasi ini:
```html
<button class="menu-btn" onclick="switchView('view-dashboard-after'); document.querySelector('.comparison-section').scrollIntoView({behavior:'smooth'});" data-i18n="btn_view_comparison">
  Lihat Perbandingan Lengkap →
</button>
```

**Kriteria selesai:**
- [ ] Ada 1 section baru yang menampilkan data before & after berdampingan (side-by-side), bisa berupa angka besar atau grouped bar chart.
- [ ] Section ini responsive (2 kolom desktop → 1 kolom mobile).
- [ ] Data yang ditampilkan **akurat**, bersumber dari state/variable yang sama dengan yang dipakai chart before/after existing (tidak boleh hardcode angka baru).
- [ ] Section baru mengikuti visual style (border-radius, warna, spacing) yang konsisten dengan card lain di dashboard.

---

## 15. TASK-15 — Watermark/Badge Identitas Akademik

**Prioritas:** 🟡 Rendah
**File yang terpengaruh:** `index.html` — `<header>` atau posisi fixed baru

**Konteks saat ini:**
Identitas "Bachelor Thesis 2026 · Telkom University" hanya muncul di halaman Home, tidak konsisten di tab lain.

**Perubahan yang harus dilakukan:**

Tambahkan badge kecil, permanen, tidak mengganggu, di pojok kanan bawah viewport (fixed position), muncul di semua tab:
```html
<div class="thesis-badge" aria-hidden="true">
  🎓 Bachelor's Thesis 2026 · Telkom University
</div>
```

CSS:
```css
.thesis-badge {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  backdrop-filter: blur(12px);
  padding: 0.4rem 0.9rem;
  border-radius: 99px;
  font-size: 0.7rem;
  color: var(--text-tertiary);
  z-index: 40;
  pointer-events: none;
}

@media (max-width: 768px) {
  .thesis-badge {
    display: none; /* sembunyikan di mobile agar tidak menutupi konten di layar sempit */
  }
}
```

Letakkan elemen ini **sekali saja**, langsung sebelum `</body>`, di luar semua `<div id="view-...">` sehingga otomatis tampil terus di semua tab tanpa duplikasi.

**Kriteria selesai:**
- [ ] Badge muncul konsisten di semua 11 tab (kecuali di viewport mobile, sesuai desain).
- [ ] Badge tidak menghalangi/menutupi tombol atau konten penting (cek terutama tidak bentrok dengan lightbox/modal — `z-index` badge harus lebih rendah dari lightbox).
- [ ] `pointer-events: none` memastikan badge tidak mengganggu klik ke elemen di belakangnya.

---

## 16. TASK-16 — Badge "10 Languages Supported" di Halaman Home

**Prioritas:** 🟡 Rendah
**File yang terpengaruh:** `index.html` — `#view-home`, dekat Contact Card atau di bawah judul thesis

**Konteks saat ini:**
Dukungan 10 bahasa hanya terlihat lewat dropdown kecil `#langSwitcher` di header — fitur ini tidak "dijual" sebagai nilai lebih di halaman utama.

**Perubahan yang harus dilakukan:**

Tambahkan badge di halaman Home, setelah bagian program/faculty/university (sebelum penutup `</div>` cover section), atau di dalam Contact Card sejajar dengan badge `contact_position`/`contact_focus`/`contact_thesis` yang sudah ada (gunakan style `.info-pill` yang sama, hasil dari TASK-07):

```html
<span class="info-pill">
  <i class="ph ph-globe"></i> <span data-i18n="badge_languages">🌐 Available in 10 Languages</span>
</span>
```

Tambahkan key i18n baru `badge_languages` ke objek translasi untuk semua 10 bahasa yang sudah didukung (bukan hanya EN/ID, karena ini elemen yang tampil di halaman utama — konsistensi penting).

**Kriteria selesai:**
- [ ] Badge muncul di halaman Home, memakai styling pill yang konsisten dengan badge lain di Contact Card.
- [ ] Teks badge berubah sesuai bahasa aktif (test ganti ke minimal 3 bahasa berbeda untuk verifikasi).
- [ ] Tidak merusak layout Contact Card yang sudah ada (cek wrapping di layar sempit).

---

## 17. Urutan Eksekusi yang Disarankan untuk Agent

Kerjakan dalam batch berikut, commit terpisah per batch (memudahkan review/rollback):

**Batch 1 — Repo hygiene (risiko rendah, dampak tinggi):**
TASK-01 → TASK-04 → TASK-02 → TASK-03

**Batch 2 — Aksesibilitas & responsif (risiko rendah-sedang):**
TASK-12 → TASK-05

**Batch 3 — Visual & branding (risiko sedang):**
TASK-06 → TASK-07 → TASK-16 → TASK-15

**Batch 4 — Polish interaksi (risiko rendah):**
TASK-08 → TASK-09 → TASK-10 → TASK-11

**Batch 5 — Fitur baru (risiko sedang-tinggi, test paling ketat):**
TASK-14

**Batch 6 — Opsional, hanya jika waktu memungkinkan:**
TASK-13

Setelah **setiap batch**, agent wajib melaporkan: file apa saja yang berubah, screenshot/deskripsi hasil test manual di dark & light mode, dan konfirmasi tidak ada fungsi existing yang rusak, sebelum lanjut ke batch berikutnya.

---

## 18. Batasan & Hal yang TIDAK Boleh Diubah

- Jangan mengubah konten narasi/data riset (angka risiko, teks assessment, hasil evaluasi pakar) — semua task di atas murni presentasi/kode.
- Jangan mengubah struktur file `.md` konten (`IT RISK ASSESSMENT.md`, `KRITERIA SKALA RISIKO.md`, dll.) kecuali diminta eksplisit di luar dokumen ini.
- Jangan mengganti library (Chart.js, ECharts, Marked.js, Phosphor Icons) dengan library lain.
- Jangan menghapus dukungan bahasa yang sudah ada (10 bahasa harus tetap berfungsi setelah semua task selesai).
- Jangan menambahkan dependency/build tool baru (npm, webpack, dll.) — proyek ini tetap harus bisa dibuka langsung sebagai static HTML tanpa proses build, kecuali diminta lain oleh user.
