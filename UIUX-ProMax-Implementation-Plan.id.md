# 🎨 Rencana Implementasi UI/UX — Integrated Risk Mitigation Program Dashboard
### Dihasilkan menggunakan skill design-intelligence **UI/UX Pro Max**
### Repo target: `pramathana/Integrated-Risk-Mitigation` · File target: `index.html` (single-page app, root repo)
### Ditujukan untuk: AI coding agent (Claude Code, Cursor, Copilot Agent, Windsurf, dll.) yang akan mengeksekusi langsung di IDE

---

## 0. Cara Membaca Dokumen Ini

Rencana ini disusun dengan terlebih dahulu mengaudit `index.html` yang live (8.515 baris: ±2.000 baris CSS dalam satu blok `<style>`, sisanya markup + JS vanilla), lalu melakukan query ke database skill **UI/UX Pro Max** (domain `style`, `color`, `typography`, `ux`, `chart`, `product`) untuk mendapatkan rekomendasi berbasis bukti yang dicocokkan dengan arketipe asli dashboard ini: **dashboard analitik/BI bergaya dark-glassmorphism** untuk artifact skripsi risk-assessment keamanan siber.

Setiap task di bawah mengikuti struktur tetap:

| Field | Arti |
|---|---|
| **ID** | Identifier unik — referensikan di commit message dan judul PR, mis. `feat(TASK-04): restore visible focus states` |
| **Prioritas** | 🔴 Tinggi (wajib sebelum rilis) / 🟠 Sedang (sebaiknya dikerjakan) / 🟡 Rendah (nice-to-have, eksplisit opsional) |
| **Bukti dari Skill** | Domain pencarian UI/UX Pro Max + temuan spesifik yang menjadi dasar task ini (agar agent — dan reviewer manusia — bisa melihat ini bukan opini gaya, tapi pola yang cocok/matched) |
| **File Terpengaruh** | Path + kira-kira rentang baris di `index.html` saat ini yang relevan |
| **Kondisi Saat Ini** | Apa yang ada sekarang, diverifikasi lewat inspeksi langsung ke repo |
| **Perubahan yang Diperlukan** | Instruksi eksplisit, disertai kode bila membantu |
| **Kriteria Selesai** | Checklist — task dianggap "selesai" hanya jika semua poin terpenuhi |

### Urutan membaca
Kerjakan **Fase 0 → Fase 6 secara berurutan**. Fase-fase ini disusun sedemikian rupa sehingga task belakangan bergantung pada token/utility yang dibuat di task sebelumnya (mis. tidak bisa memperbaiki warna focus-ring di Fase 2 dengan benar sebelum set token yang diperluas dari Fase 1 ada). Task *dalam* satu fase yang diberi sub-huruf sama (mis. `TASK-05a` / `TASK-05b`) boleh dikerjakan paralel/urutan bebas. Fase 7 secara eksplisit opsional dan boleh dilewati atau ditunda ke PR terpisah.

### Sebelum mulai (wajib untuk agent)
1. `git checkout -b feature/uiux-promax-polish` — jangan pernah commit langsung ke `main`.
2. Baca `Rencana-Implementasi-untuk-AI-Coding-Agent.md` yang sudah ada di root repo — dokumen itu membahas **file hygiene, meta tags, dan cleanup terkait konten**. Rencana ini melengkapi dan hanya membahas **desain visual / UX**. Jangan duplikasi atau bentrok dengan task yang sudah selesai dari dokumen tersebut; cek checkbox-nya dulu.
3. Jalankan server lokal sebelum/sesudah setiap task: `python -m http.server 8000` → `http://localhost:8000`.
4. Matriks pengujian untuk **setiap** task visual, sebelum menandai selesai dan sebelum lanjut ke task berikutnya:
   - Mode gelap **dan** mode terang (`toggleTheme()`)
   - Lebar desktop (≥1600px, `max-width` dari `.dashboard-container`)
   - Lebar tablet (~768–1024px, breakpoint yang sudah ada)
   - Lebar mobile (~375px)
   - Minimal 2 dari 10 bahasa, termasuk salah satu bahasa dengan panjang string rata-rata lebih panjang (Jerman `de` atau Rusia `ru` bagus untuk stress test overflow)
5. Jangan pernah cuma membuka dev tools lalu "kira-kira" kontras — gunakan contrast checker sungguhan (accessibility inspector browser, atau WebAIM Contrast Checker) untuk setiap pasangan warna yang disentuh.

---

## 1. Audit Desain Berbasis Skill (Temuan Baseline)

Berikut hasil query skill UI/UX Pro Max terhadap karakteristik asli dashboard ini, dan yang terungkap saat disilangkan dengan kode live:

| # | Temuan | Domain Skill / Match | Severity |
|---|---|---|---|
| F1 | Dashboard saat ini sudah cocok dengan arketipe **Modern Dark / Financial-Dashboard glass style** (kartu frosted, `backdrop-filter: blur`, aksen teal, base family `#0f172a`) — ini fondasi yang *bagus*, bukan kandidat redesign. Konfirmasi-dan-perhalus, bukan ganti total. | Domain `style` — "Modern Dark (Cinema)" + "Financial Dashboard" keduanya cocok dengan overlap keyword tinggi | Info |
| F2 | Ditemukan **3 instance `outline: none` tanpa pengganti indikator focus** di `index.html` (baris ±2045, ±2364, ±2533 — tombol theme toggle, language switcher, dan satu kontrol interaktif lain). | Domain `ux` — aturan "Focus States": *"Don't: Remove focus outline without replacement." Severity: High* | 🔴 Tinggi |
| F3 | **Token desain severity risiko belum lengkap.** Hanya 3 tier di CSS (`--risk-moderate-*`, `--risk-lowmod-*`, `--risk-low-*`), padahal `KRITERIA SKALA RISIKO.md` milik proyek ini sendiri mendefinisikan **5 tier severity**, termasuk "Moderate-to-High" (🟠, skor 16–19) dan "High" (🔴, skor 20–25). Tidak ada kelas CSS/badge untuk dua tier teratas. | Domain `color` — pola status-color Financial memerlukan ramp severity lengkap agar data-viz robust | 🟠 Sedang |
| F4 | **10 tab navigasi flat** (`.menu-bar`) memakai `flex-wrap`, yang fungsional tapi menghasilkan tangga multi-baris tidak rapi di viewport sempit. | Domain `ux` — kategori Navigation; pattern-matching untuk nav dengan banyak tab (`>7` destinasi utama) idealnya pakai scroll-with-fade atau pola grouped/priority+overflow | 🟠 Sedang |
| F5 | Diagram Sankey (ECharts) adalah **satu-satunya visualisasi** untuk pemetaan threat→control di view before/after. Domain `chart` skill memberi rating **Accessibility Grade: C** untuk Sankey dan secara eksplisit merekomendasikan *"Structural flow charts cannot be conveyed by color alone. Provide flow table."* Saat ini belum ada fallback teks/tabel. | Domain `chart` — entri Sankey | 🟠 Sedang |
| F6 | Chart doughnut/bar (Chart.js) mengandalkan plugin `chartjs-plugin-datalabels` (bagus — ini sudah memenuhi panduan a11y "value labels visible" untuk bar chart), tapi warna masih jadi pembeda **utama** untuk severity di legend doughnut chart. | Domain `chart` — entri Bar Chart (terpenuhi) vs aturan umum color-only (gap sebagian) | 🟡 Rendah |
| F7 | Tipografi hanya **satu family** (Inter) untuk heading maupun body, tanpa secondary/mono accent untuk data label, nilai numerik, atau eyebrow section — fungsional tapi terasa datar secara visual untuk dashboard yang data-heavy. | Domain `typography` — pairing "Dashboard Data" (Fira Code + Fira Sans) dan "SaaS Mobile Boutique" sama-sama merekomendasikan secondary face untuk angka/label di konteks analitik | 🟡 Rendah (opsional) |
| F8 | Tidak ada loading/skeleton state saat `marked.js` fetch dan render tujuh file `.md` eksternal, atau saat Chart.js/ECharts inisialisasi pada kunjungan pertama ke suatu tab — konten bisa muncul mendadak, terutama di koneksi lambat (GitHub Pages + banyak script CDN eksternal). | Domain `ux` — "Loading States": *"Don't: Leave UI frozen with no feedback. Severity: High"* | 🟠 Sedang |
| F9 | Tiga aset gambar statis berukuran cukup besar untuk delivery web: `5 Layer ZTA PNG BAG.drawio.png` (380K), `5 Layer ZTA PNG.png` (376K), `LOGO UNIVERSITAS TELKOM.png` (268K), `Sankey Diagram Before Revision.png` (1.4M). Tidak ada yang pakai `loading="lazy"`. | Domain `ux` — "Lazy Loading": *"Do: Lazy load below-fold images and content."* | 🟡 Rendah |
| F10 | Metric card, hover state, dan elevasi kartu sudah diimplementasikan dengan baik (`transform: translateY(-2px)` + shadow saat hover) — sudah sangat cocok dengan panduan interaksi glass-card dari skill. Tidak perlu perubahan di luar konsistensi token (Fase 1). | Domain `style` | Info (tidak perlu aksi) |

**Kesimpulan umum:** dashboard ini tidak butuh redesign. Yang dibutuhkan adalah (a) pembenahan aksesibilitas, (b) perbaikan skala navigasi untuk menu 10-tab, (c) penyelesaian sistem token warna, dan (d) polish/konsistensi. Rencana di bawah disusun sesuai itu — ini **rencana penyempurnaan (refinement)**, bukan rebuild.

---

## 2. Sistem Desain yang Direkomendasikan (Diperhalus, Bukan Diganti)

Domain `color` skill mengembalikan palet dashboard gelap (mis. entri "Financial Dashboard" dan "Smart Home/IoT Dashboard") yang secara struktural sangat dekat dengan yang sudah diimplementasikan (base family `#0f172a`/`#020617`, border slate, warna status semantik). **Rekomendasi: jangan ganti palet brand yang sudah ada** — aksen teal (`--accent-primary: #0ea5b7`) adalah identitas visual proyek ini dan sudah cukup berbeda dari dashboard generik ber-Tailwind-blue. Sebaliknya, perluas cakupannya.

### 2.1 Token warna yang diperluas (aditif — jangan hapus variabel yang sudah ada)

Tambahkan ke `:root` (gelap, default) — sisipkan tepat setelah deklarasi `--risk-low-text` yang sudah ada:

```css
/* Ramp severity risiko yang diperluas — melengkapi skala 5-tier yang
   didefinisikan di KRITERIA SKALA RISIKO.md (saat ini baru 3 dari 5 tier ada tokennya) */
--risk-modhigh-bg: rgba(249, 115, 22, 0.15);   /* Orange — "Moderate to High" 16–19 */
--risk-modhigh-text: #fb923c;
--risk-high-bg: rgba(239, 68, 68, 0.15);        /* Red — "High" 20–25 */
--risk-high-text: #f87171;

/* Skala elevasi (memformalkan nilai shadow yang selama ini ad-hoc) */
--elevation-1: 0 4px 12px -2px rgba(0, 0, 0, 0.2);
--elevation-2: 0 10px 25px -5px rgba(0, 0, 0, 0.3);   /* sesuai .metric-card:hover yang sudah ada */
--elevation-3: 0 20px 40px -8px rgba(0, 0, 0, 0.4);

/* Focus ring (dipakai di sepanjang Fase 2) */
--focus-ring: 0 0 0 3px var(--accent-glow);
--focus-ring-color: var(--accent-primary);
```

Dan padanan light-theme di dalam `[data-theme="light"]`:

```css
--risk-modhigh-bg: rgba(249, 115, 22, 0.18);
--risk-modhigh-text: #c2410c;
--risk-high-bg: rgba(239, 68, 68, 0.18);
--risk-high-text: #b91c1c;

--elevation-1: 0 4px 12px -2px rgba(0, 0, 0, 0.08);
--elevation-2: 0 10px 25px -5px rgba(0, 0, 0, 0.12);
--elevation-3: 0 20px 40px -8px rgba(0, 0, 0, 0.16);
```

> ⚠️ Token baru ini **tidak boleh** dipakai untuk mengubah klasifikasi severity threat mana pun yang sudah ada. Fungsinya agar komponen badge (`.badge.modhigh`, `.badge.high`) tersedia jika/ketika konten suatu saat membutuhkannya, dan agar skala warna chart lengkap/robust. Lihat Batasan §5.

### 2.2 Tipografi (opsional — lihat Task 13)
Tetap gunakan **Inter** sebagai satu-satunya face wajib (risiko nol, tanpa network request baru). Jika tim ingin peningkatan hierarki data opsional dari Fase 6, pairing "Dashboard Data" dari skill (Fira Code untuk angka/label + Inter untuk body, karena Inter sudah dimuat) adalah penambahan paling minim risiko — tidak perlu mengganti Inter, cukup menambah satu mono face dengan weight terbatas untuk nilai metrik dan angka tabel.

### 2.3 Motion
Panduan UX dari skill secara eksplisit memperingatkan: *"Animate 1-2 key elements per view maximum... Don't: Animate everything that moves."* Rule global `* { transition: ... }` yang sudah ada memang sudah meng-animasikan color/background/border/shadow di setiap elemen — ini disengaja dan wajar untuk kehalusan theme-toggle, tapi **jangan menambah elemen ber-animasi baru di luar yang ditentukan di Fase 4** (count-up pada nilai metrik, slide indikator tab). Jangan tambahkan scroll-triggered reveal, parallax, atau stagger entrance per-kartu — ini artifact akademik/profesional untuk sidang skripsi, bukan situs marketing; motion harus tetap minimal dan profesional.

---

## 3. Rencana Task

### Fase 0 — Setup

**TASK-00 · 🔴 Tinggi**
**File:** tidak ada (hanya git/environment)
**Perubahan:** Buat branch `feature/uiux-promax-polish`. Pastikan server lokal berjalan dan semua 10 tab saat ini load tanpa error console sebelum melakukan perubahan apa pun (menetapkan baseline yang bersih).
**Kriteria Selesai:**
- [ ] Branch dibuat dari `main` terbaru.
- [ ] Screenshot baseline diambil untuk masing-masing dari 10 view (mode gelap) untuk perbandingan before/after — simpan di `dev-archive/screenshots/before/` (di-gitignore atau diarsipkan sesuai konvensi `Rencana-Implementasi` yang sudah ada).
- [ ] Nol error console saat load di sesi browser baru.

---

### Fase 1 — Fondasi Token Desain

**TASK-01 · 🔴 Tinggi**
**Bukti dari Skill:** F3 (§1)
**File:** `index.html`, blok `:root` dan `[data-theme="light"]` (±baris 35–82)
**Kondisi Saat Ini:** Sistem warna risiko 3-tier (`moderate`, `lowmod`, `low`).
**Perubahan yang Diperlukan:** Tambahkan 4 token baru (`--risk-modhigh-*`, `--risk-high-*`) plus token elevasi dan focus-ring persis seperti spesifikasi §2.1, di **kedua** blok `:root` (gelap) dan `[data-theme="light"]`.
**Kriteria Selesai:**
- [ ] Semua 8 custom property baru ada di kedua blok tema.
- [ ] Tidak ada token yang sudah ada yang di-rename atau dihapus.
- [ ] Halaman tetap render identik dengan baseline (token baru bersifat aditif/belum dipakai sampai Task 02).

---

**TASK-02 · 🟠 Sedang**
**Bukti dari Skill:** F3, F6 (§1)
**File:** `index.html`, dekat rule `.badge.moderate/.lowmod/.low` yang sudah ada (±baris 364–378)
**Kondisi Saat Ini:** Kelas badge hanya ada untuk 3 tier.
**Perubahan yang Diperlukan:** Tambahkan kelas CSS yang sepadan:
```css
.badge.modhigh {
  background: var(--risk-modhigh-bg);
  color: var(--risk-modhigh-text);
}
.badge.high {
  background: var(--risk-high-bg);
  color: var(--risk-high-text);
}
```
Tambahkan juga ikon (Phosphor `ph-warning` untuk modhigh, `ph-warning-octagon` untuk high) di dalam pola markup badge yang sudah dipakai untuk 3 tier lainnya, sehingga severity tidak pernah hanya disampaikan lewat warna saja (langsung menjawab F6/aturan skill "Color Only").
**Kriteria Selesai:**
- [ ] `.badge.modhigh` dan `.badge.high` render dengan benar dalam test terisolasi (tambahkan sementara satu badge uji di dev tools, verifikasi visual, lalu hapus — jangan tinggalkan markup uji di file yang di-commit).
- [ ] Setiap badge yang sudah ada (`moderate`, `lowmod`, `low`) juga mendapat ikon kecil di depan untuk konsistensi, tidak hanya dua tier baru.
- [ ] Kelas/badge severity yang sudah ditetapkan untuk threat mana pun tidak berubah. Task ini hanya menambah kapabilitas.

---

### Fase 2 — Aksesibilitas (wajib sebelum rilis)

**TASK-03 · 🔴 Tinggi**
**Bukti dari Skill:** F2 (§1)
**File:** `index.html`, baris ±2045, ±2364, ±2533 (tombol theme toggle, `<select>` bahasa, dan kontrol ketiga yang ditandai — verifikasi selector persisnya via `grep -n "outline: none" index.html` sebelum mengedit)
**Kondisi Saat Ini:** `outline: none;` tanpa pengganti apa pun — pengguna keyboard yang tab melalui kontrol header tidak mendapat indikasi visual focus.
**Perubahan yang Diperlukan:** Ganti setiap `outline: none;` yang telanjang dengan:
```css
outline: none;
```
```css
/* tambahkan sebagai rule baru yang menarget selector yang sama, memakai
   :focus-visible agar pengguna mouse tidak melihat ring saat klik,
   hanya pengguna keyboard yang tab */
#themeToggleBtn:focus-visible,
#langSwitcher:focus-visible {
  outline: none;
  box-shadow: var(--focus-ring);
}
```
Terapkan pola `:focus-visible { box-shadow: var(--focus-ring); }` yang sama ke `.menu-btn` dan elemen interaktif lain yang saat ini belum punya style focus (audit dengan `grep -n "outline: none" index.html` untuk menangkap instance ketiga secara presisi).
**Kriteria Selesai:**
- [ ] Tab melalui halaman dengan keyboard saja (tanpa mouse) menampilkan ring yang jelas terlihat di setiap kontrol interaktif: theme toggle, language switcher, semua 10 tab menu, tombol apa pun di dalam konten hasil render markdown.
- [ ] Klik dengan mouse **tidak** menampilkan ring (mengonfirmasi `:focus-visible`, bukan `:focus`, yang dipakai).
- [ ] Ring terlihat di mode gelap maupun terang (memakai `--accent-glow`/`--accent-primary` yang sudah punya varian light/dark).

---

**TASK-04 · 🟠 Sedang**
**Bukti dari Skill:** F2 (§1), aturan Navigation "Skip Links" secara umum
**File:** `index.html`, tepat setelah `<body>` (±baris 2007)
**Kondisi Saat Ini:** Tidak ada skip-to-content link. Dengan 10 tab nav plus dropdown bahasa sebelum konten utama, pengguna keyboard harus tab melalui ±12 kontrol setiap kali halaman dimuat untuk mencapai konten.
**Perubahan yang Diperlukan:** Tambahkan sebagai elemen pertama di dalam `<body>`:
```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```
```css
.skip-link {
  position: absolute;
  top: -48px;
  left: 1rem;
  background: var(--accent-primary);
  color: #fff;
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  z-index: 100;
  transition: top 0.2s ease;
}
.skip-link:focus {
  top: 1rem;
}
```
Beri container yang membungkus semua section `#view-*` (atau tambahkan wrapper jika belum ada) `id="main-content"` dan `tabindex="-1"`.
**Kriteria Selesai:**
- [ ] Link tersembunyi secara visual sampai di-focus (penekanan Tab pertama saat halaman dimuat memunculkannya di kiri-atas).
- [ ] Mengaktifkannya memindahkan focus ke area konten utama, melewati header/nav/kontrol bahasa.
- [ ] Tidak muncul secara visual pada browsing normal (non-keyboard).

---

**TASK-05 · 🟠 Sedang**
**Bukti dari Skill:** F2 (§1), aturan kontras warna (minimum 4.5:1)
**File:** `index.html`, token warna teks `:root`/`[data-theme="light"]`, plus penggunaan inline `style="color: ..."` mana pun yang ditemukan via `grep -n "color: var(--text-tertiary)" index.html`
**Kondisi Saat Ini:** `--text-tertiary` (`#64748b` gelap / `#6b7280` terang) dipakai untuk teks yang di-de-emphasize; perlu diverifikasi terhadap background `--bg-base` dan `--bg-surface` tempat token ini benar-benar dipakai.
**Perubahan yang Diperlukan:** Jalankan setiap pasangan (foreground, background) token yang benar-benar dipakai bersama melalui contrast checker. Minimal verifikasi:
- `--text-secondary` di atas `--bg-surface` (kedua tema)
- `--text-tertiary` di atas `--bg-surface` (kedua tema)
- `--risk-modhigh-text` / `--risk-high-text` (baru, Task 01) di atas token `-bg` masing-masing
- `--btn-compare-text` / `--comparison-desc-text` di atas background container asli tempat mereka berada

Di mana pun pasangan tersebut jatuh di bawah 4.5:1 untuk teks normal (atau 3:1 untuk teks besar ≥24px/18.66px bold), gelapkan (mode terang) atau terangkan (mode gelap) hanya token tersebut — jangan ubah layout atau token mana yang dipakai di mana.
**Kriteria Selesai:**
- [ ] Setiap pasangan teks/background yang diaudit memiliki rasio kontras terdokumentasi ≥4.5:1 (teks normal) atau ≥3:1 (teks besar/ikon).
- [ ] Token mana pun yang disesuaikan diubah hanya di definisi CSS variable-nya (single source of truth), tidak pernah lewat inline override.
- [ ] Verifikasi ulang badge baru dari Task 02 terhadap standar yang sama ini.

---

### Fase 3 — Perbaikan Skala Navigasi

**TASK-06 · 🟠 Sedang**
**Bukti dari Skill:** F4 (§1)
**File:** `index.html`, rule `.menu-bar` / `.menu-btn` (±baris 525–552), plus blok `@media (max-width: 768px)` yang sudah ada
**Kondisi Saat Ini:** `.menu-bar { display: flex; flex-wrap: wrap; }` — 10 tombol wrap menjadi tangga tidak rapi di layar sempit; tidak ada petunjuk visual bahwa masih ada item di luar layar pada lebar mana pun.
**Perubahan yang Diperlukan:** Ubah menjadi strip tab yang bisa di-scroll horizontal dengan petunjuk fade di tepi, **tanpa mengubah handler `onclick="switchView(...)"`, atribut `data-view`, atau fungsi JS `switchView()`**:
```css
.menu-bar {
  display: flex;
  flex-wrap: nowrap;           /* sebelumnya wrap */
  overflow-x: auto;
  scroll-snap-type: x proximity;
  -webkit-overflow-scrolling: touch;
  gap: 0.75rem;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 1rem;
  scrollbar-width: thin;
}
.menu-btn {
  scroll-snap-align: start;
  flex-shrink: 0;               /* mencegah tombol terkompres */
}
```
Tambahkan wrapper container dengan `position: relative` dan dua gradient fade pseudo-element (`::before`/`::after`, `pointer-events: none`) di tepi kiri/kanan `.menu-bar` yang memakai `var(--bg-base)` memudar ke transparan, agar pengguna sadar masih ada yang bisa di-scroll. Pertahankan `flex-wrap: wrap` **hanya** sebagai fallback di dalam blok `@media (max-width: 768px)` yang sudah ada jika user testing menunjukkan scroll lebih sulit daripada wrap di layar sangat kecil — defaultkan ke scroll di semua ukuran dulu dan validasi.
**Kriteria Selesai:**
- [ ] Semua 10 tab tetap dalam satu baris di setiap lebar viewport mulai dari 375px; tidak ada yang wrap ke baris kedua secara default.
- [ ] Tab aktif (`.menu-btn.active`) dapat dijangkau lewat scroll/swipe horizontal di mobile dan terindikasi secara visual.
- [ ] Gradient fade di tepi muncul hanya saat masih ada konten untuk di-scroll ke arah itu (atau boleh statis jika implementasi murni CSS lebih sederhana — catat penyederhanaan ini di deskripsi PR).
- [ ] Pemanggilan `switchView('view-home')` dst. dan atribut `data-view` identik byte-per-byte dengan sebelum task ini — konfirmasi dengan `git diff` yang menunjukkan hanya CSS/wrapper yang berubah, bukan logika markup tombol.
- [ ] Navigasi tombol panah keyboard atau Tab antar tab tetap berfungsi dan men-scroll tab aktif ke dalam pandangan (`scrollIntoView({inline: 'nearest'})` boleh ditambahkan di dalam fungsi `switchView` yang sudah ada jika belum ada — aditif saja).

---

**TASK-07 · 🟡 Rendah**
**Bukti dari Skill:** F4 (§1), aturan Navigation "Active State" (sudah terpenuhi sebagian)
**File:** `index.html`, rule `.menu-btn.active` (±baris 551)
**Kondisi Saat Ini:** Tab aktif memakai background solid + shadow glow — sudah memenuhi panduan "Active State" dari skill (`Do: Highlight active nav item with color/underline`). Task ini hanya penghalusan, bukan perbaikan.
**Perubahan yang Diperlukan:** Opsional menambahkan transisi `transform`/`background-position` yang halus saat berpindah tab agar perubahan active-state terasa sebagai satu cue motion yang minimal (memenuhi aturan motion "1–2 elemen kunci" — ini satu-satunya budget animasi navigasi untuk seluruh aplikasi). Jangan implementasikan jika bertentangan atau mempersulit implementasi scroll-snap Task 06 — task ini boleh sepenuhnya dilewati tanpa memblokir apa pun.
**Kriteria Selesai:**
- [ ] Jika diimplementasikan: durasi transisi ≤200ms, memakai `--accent-primary`/`--accent-glow` yang sudah ada, tanpa layout shift.
- [ ] Jika dilewati: tidak perlu aksi, tandai sebagai sengaja ditunda di catatan PR.

---

### Fase 4 — Polish Komponen & Data-Viz

**TASK-08 · 🟠 Sedang**
**Bukti dari Skill:** F5 (§1)
**File:** `index.html`, container diagram Sankey di `view-dashboard` dan `view-dashboard-after` (cari `echarts.init` ±baris 6361/6366 untuk sisi JS; container HTML ada tepat di atasnya di masing-masing view)
**Kondisi Saat Ini:** Diagram Sankey adalah satu-satunya presentasi pemetaan threat→ISO27005-event→asset→COBIT-weakness; belum ada alternatif teks.
**Perubahan yang Diperlukan:** Tepat di bawah masing-masing container `<div>` Sankey, tambahkan elemen `<details>` yang dilipat (collapsed) berisi tabel data yang accessible dengan struktur source→target→value yang sama dengan yang sudah memberi makan `series.data` ECharts:
```html
<details class="sankey-table-fallback">
  <summary data-i18n="sankey_table_toggle">View this diagram as a table</summary>
  <div class="table-wrap">
    <table>
      <thead>
        <tr><th data-i18n="sankey_col_source">Source (Threat)</th>
            <th data-i18n="sankey_col_target">Target</th>
            <th data-i18n="sankey_col_value">Value</th></tr>
      </thead>
      <tbody><!-- generate dari array data yang sama yang dipakai echarts, jangan duplikasi angka manual --></tbody>
    </table>
  </div>
</details>
```
Isi `<tbody>` **secara programatik dari struktur data/array JS yang persis sama yang sudah dikirim ke `echarts.init(...).setOption(...)`** — jangan ketik ulang angka secara manual sebagai salinan kedua, untuk menghindari kedua representasi menjadi tidak sinkron. Tambahkan i18n key yang sepadan (`sankey_table_toggle`, `sankey_col_source`, `sankey_col_target`, `sankey_col_value`) ke **semua 10** kamus bahasa di objek `translations`.
**Kriteria Selesai:**
- [ ] Tabel dihasilkan dari struktur data in-memory yang sama dengan chart (diverifikasi dengan membaca kode, bukan hanya visual).
- [ ] `<details>` collapsed secara default agar tidak mengganggu layout visual yang sudah ada.
- [ ] Tabel ada untuk kedua instance Sankey `view-dashboard` (before) dan `view-dashboard-after` (after).
- [ ] Semua 10 bahasa punya string terjemahan untuk 4 i18n key baru — verifikasi dengan `setLanguage()` untuk minimal 3 bahasa.
- [ ] Screen reader (atau accessibility tree inspector browser) mengonfirmasi tabel dapat dijangkau dan dibaca terlepas dari chart canvas/SVG.

---

**TASK-09 · 🟡 Rendah**
**Bukti dari Skill:** F10 (§1, mengonfirmasi tidak perlu perbaikan) + pola "Number animations (count-up)" Financial Dashboard
**File:** `index.html`, elemen `.metric-value` dan JS inisialisasinya
**Kondisi Saat Ini:** Nilai metrik di-render sebagai angka final statis saat load.
**Perubahan yang Diperlukan:** Tambahkan count-up sederhana tanpa dependency (mis. `requestAnimationFrame` easing dari 0 ke nilai target selama ±600ms) yang dipicu sekali saat setiap view menjadi visible via `switchView`. Ini adalah **satu-satunya** budget motion data-viz sesuai aturan "maks 1–2 elemen" — jangan sekaligus animasikan entrance chart, entrance kartu, DAN counter; pilih counter saja, karena paling bernilai untuk dashboard yang metrics-first.
**Kriteria Selesai:**
- [ ] Counter beranimasi hanya saat reveal pertama suatu view, bukan setiap re-render/theme toggle/ganti bahasa.
- [ ] Menghormati `prefers-reduced-motion: reduce` — langsung ke nilai final untuk pengguna dengan setting OS tersebut.
- [ ] Tidak ada dependency baru yang ditambahkan (JS murni, tanpa library animasi).
- [ ] Angka yang ditampilkan identik dengan nilai statis saat ini — task ini hanya mengubah timing presentasi, tidak pernah mengubah angkanya.

---

**TASK-10 · 🟡 Rendah (opsional)**
**Bukti dari Skill:** F7 (§1)
**File:** `index.html`, `<head>` (import font, jika dilanjutkan), `.metric-value`, sel numerik tabel
**Kondisi Saat Ini:** Satu family Inter di seluruh dashboard.
**Perubahan yang Diperlukan (hanya jika disetujui — lihat §6 Batasan tentang network request eksternal baru):** Tambahkan JetBrains Mono atau Fira Code (pairing "Dashboard Data" dari skill) dengan **satu weight saja** (500) via pola Google Fonts yang sudah ada, diterapkan hanya ke `.metric-value`, sel numerik tabel, dan label axis chart lewat token baru `--font-mono`. Jangan terapkan ke heading atau body copy — Inter tetap primer di tempat lain.
**Kriteria Selesai:**
- [ ] Jika diimplementasikan: hanya satu weight Google Fonts/`@font-face` baru yang ditambahkan; verifikasi penambahan berat halaman aktual (target: <15KB) sebelum commit.
- [ ] Jika diimplementasikan: `font-display: swap` dipakai untuk menghindari layout-blocking.
- [ ] Jika dilewati (rekomendasi default mengingat batasan di §6): ditandai eksplisit "Ditunda — belum diimplementasikan" di PR, bukan dihapus diam-diam.

---

### Fase 5 — Loading State & Perceived Performance

**TASK-11 · 🟠 Sedang**
**Bukti dari Skill:** F8 (§1)
**File:** `index.html`, di mana pun `marked.js` fetch/render setiap file `.md` ke container `.md-content`-nya, dan di mana pun instance Chart.js/ECharts pertama kali dibuat per view
**Kondisi Saat Ini:** Konten muncul mendadak tanpa state sela; saat kunjungan pertama ke tab yang banyak markdown (Research Overview, Risk Criteria, dll.) atau tab yang banyak chart, bisa terlihat container kosong sebelum konten muncul.
**Perubahan yang Diperlukan:** Tambahkan skeleton CSS ringan (shimmer animasi memakai `background: linear-gradient` dengan token `--bg-surface`/`--border-subtle` yang sudah ada — tanpa warna baru) yang ditampilkan di setiap container `.md-content` / chart **sebelum** fetch/render-nya selesai, dihapus setelah `marked.js` menyisipkan HTML atau constructor/`setOption` chart selesai dijalankan.
```css
.skeleton {
  background: linear-gradient(90deg, var(--bg-surface) 25%, var(--bg-surface-hover) 50%, var(--bg-surface) 75%);
  background-size: 200% 100%;
  animation: skeleton-shimmer 1.4s ease-in-out infinite;
  border-radius: 16px;
  min-height: 200px;
}
@keyframes skeleton-shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```
**Kriteria Selesai:**
- [ ] Skeleton hanya terlihat selama window fetch/render sesungguhnya (uji dengan throttle "Slow 3G" di dev tools untuk memastikan tidak hanya berkedip sekilas).
- [ ] Skeleton menghormati `prefers-reduced-motion` (fallback ke placeholder statis tanpa pulse).
- [ ] Dihapus dengan bersih — tidak ada elemen skeleton tersisa di DOM setelah konten selesai load (hindari node duplikat/tumpang tindih).
- [ ] Tidak menunda render konten sesungguhnya — ini hanya overlay/placeholder visual, bukan gate yang blocking.

---

**TASK-12 · 🟡 Rendah**
**Bukti dari Skill:** F9 (§1)
**File:** `index.html`, semua tag `<img>` (`LOGO UNIVERSITAS TELKOM.png`, `5 Layer ZTA PNG*.png`, `Privacy-Icon.png`, `Sankey Diagram Before Revision.png`)
**Kondisi Saat Ini:** Belum ada atribut `loading="lazy"`; gambar disajikan pada ukuran/berat PNG asli (hingga 1.4MB untuk satu aset).
**Perubahan yang Diperlukan:**
1. Tambahkan `loading="lazy"` ke setiap `<img>` yang bukan elemen visible pertama saat halaman dimuat (logo universitas di Home view, karena berada di atas fold pada first paint, sebaiknya tetap `loading="eager"` atau tidak ditentukan; diagram ZTA dan gambar section evaluasi, yang berada di tab yang tidak dikunjungi secara default, sebaiknya `lazy`).
2. **Opsional, terpisah dari task ini dan memerlukan persetujuan eksplisit:** konversi 4 PNG besar ke WebP dengan fallback `<picture>`/PNG. Tandai ini sebagai follow-up PR terpisah karena menyentuh aset biner yang direferensikan lewat nama file eksak di seluruh file konten markdown (`grep -rn "\.png" *.md index.html` dulu untuk menemukan setiap referensi sebelum me-rename/menambah apa pun).
**Kriteria Selesai:**
- [ ] Setiap `<img>` below-the-fold punya `loading="lazy"`.
- [ ] Logo halaman Home (di atas fold) secara eksplisit dikecualikan dari lazy-loading.
- [ ] Jika konversi WebP dilanjutkan: PNG asli dipertahankan sebagai fallback (elemen `<picture>`), tidak dihapus — nama file yang direferensikan di tempat lain di repo (file markdown) tidak boleh rusak.

---

### Fase 6 — Audit Paritas Mode Terang

**TASK-13 · 🔴 Tinggi**
**File:** seluruh `index.html` — setiap token/rule yang disentuh Task 01–12
**Kondisi Saat Ini:** Tema terang (`[data-theme="light"]`) adalah blok override penuh yang mencerminkan sebagian besar token tema gelap saat ini.
**Perubahan yang Diperlukan:** Untuk setiap token/komponen baru atau yang dimodifikasi dari Fase 1–5, verifikasi ulang bahwa ia memiliki padanan mode terang yang benar dan sudah dicek kontrasnya. Ini adalah task checklist/audit, bukan kode baru dengan sendirinya — tugasnya adalah menangkap hal apa pun yang mungkin ditambahkan Fase 1–5 hanya untuk mode gelap.
**Kriteria Selesai:**
- [ ] `toggleTheme()` tetap berfungsi penuh tanpa regresi visual di kedua arah.
- [ ] Token severity risiko baru (Task 01/02), focus ring (Task 03), skip link (Task 04), skeleton shimmer (Task 11) semuanya dikonfirmasi benar khusus di mode terang (bukan hanya "tidak rusak" — benar-benar dicek kontras sesuai standar Task 05, karena perhitungan kontras mode terang berbeda dengan mode gelap).
- [ ] Tidak ada token yang didefinisikan di `:root` yang tertinggal tanpa override di `[data-theme="light"]` di tempat nilai spesifik-terang sebenarnya dibutuhkan (beberapa, seperti token spacing/radius, memang benar tidak butuh varian tema — hanya token terkait warna yang butuh).

---

## 4. Fase 7 — Eksplisit Opsional (Jangan Otomatis Diimplementasikan)

Berikut ditemukan oleh skill/audit tapi **di luar scope yang diminta** ("improve appearance") atau membawa biaya/risiko yang perlu persetujuan eksplisit dari stakeholder sebelum agent menyentuhnya:

- **Layout RTL untuk bahasa Arab (`ar`).** Language switcher menawarkan bahasa Arab, tapi belum ada mirroring `dir="rtl"` di mana pun di CSS. Ini gap internasionalisasi yang sah, tapi merupakan **task layout struktural**, bukan task appearance visual, dan menyentuh logika spacing/alignment setiap komponen. Direkomendasikan sebagai rencana terpisah dan khusus jika dilanjutkan.
- **Peningkatan pairing font (Task 10).** Sudah ditandai opsional di atas — hanya diimplementasikan dengan persetujuan eksplisit mengingat batasan network-request-baru di §5.
- **Konversi aset WebP (Task 12b).** Hanya dilanjutkan di PR follow-up khusus setelah dikonfirmasi tidak ada file lain di repo yang mereferensikan PNG lewat nama file/ekstensi eksak.
- **Memecah `index.html` menjadi file CSS/JS terpisah atau memperkenalkan bundler/build step.** Akan meningkatkan maintainability tapi langsung bertentangan dengan model deployment single-file tanpa build step yang saat ini dipakai proyek ini (GitHub Pages menyajikan `index.html` apa adanya). Jangan lakukan ini tanpa permintaan eksplisit dari user — lihat Batasan.

---

## 5. Urutan Eksekusi (Dependency Graph)

```
TASK-00 (setup)
   │
   ▼
TASK-01 (token) ──► TASK-02 (badge, bergantung pada token warna baru)
   │
   ▼
TASK-03 (focus ring, bergantung pada token --focus-ring dari TASK-01)
   │
   ├──► TASK-04 (skip link)
   └──► TASK-05 (audit kontras — sebaiknya dijalankan SETELAH 01–04 karena
                  task-task tersebut memperkenalkan token/elemen yang juga
                  perlu diaudit)
   │
   ▼
TASK-06 (perbaikan scroll nav) ──► TASK-07 (opsional, motion active-state, boleh dilewati)
   │
   ▼
TASK-08 (fallback tabel Sankey)
TASK-09 (count-up metrik)              ← ketiga task ini independen satu
TASK-10 (font opsional, boleh dilewati)  sama lain dan independen dari
                                          Fase 3; boleh dikerjakan urutan
                                          apa pun atau paralel oleh sesi
                                          agent terpisah
   │
   ▼
TASK-11 (loading skeleton)
TASK-12 (lazy-load gambar)             ← independen satu sama lain
   │
   ▼
TASK-13 (audit paritas mode terang) ← WAJIB dijalankan terakhir; ini
                                        mengecek ulang semua yang
                                        ditambahkan di Fase 1–5
```

Aturan praktis: **apa pun yang memperkenalkan CSS custom property baru harus selesai sebelum apa pun yang mengonsumsinya**, dan **audit mode terang (TASK-13) selalu menjadi gate terakhir sebelum merge**, apa pun urutan pengerjaan task di tengah.

---

## 6. Batasan (Berlaku untuk Setiap Task, Tanpa Kecuali)

1. **Tidak ada perubahan konten/data.** Deskripsi threat, skor risiko, pemetaan COBIT/ZTA/ISO 27002, teks dan skor evaluasi artifact, metadata skripsi (judul, nama penulis, NIM `1202223026`, universitas, program, tahun), dan seluruh konten naratif file `.md` harus tetap identik byte-per-byte kecuali suatu task secara eksplisit menyatakan sebaliknya (tidak ada di rencana ini yang seperti itu). Ini adalah artifact sidang skripsi — integritas konten tidak dapat dinegosiasikan.
2. **Arsitektur single-file tanpa build step dipertahankan.** `index.html` tetap file statis self-contained yang bisa di-deploy ke GitHub Pages via `git push` dengan nol build step. Jangan memperkenalkan bundler, migrasi framework, atau pemecahan file kecuali diminta secara eksplisit oleh pemilik repo dalam task di masa depan.
3. **Semua 10 bahasa harus tetap berfungsi setelah setiap task.** Copy UI baru apa pun (teks skip link, header tabel sankey, dll.) harus ditambahkan sebagai key `data-i18n` dengan terjemahan ditambahkan ke **semua 10** blok bahasa di objek `translations` — bukan hanya bahasa Inggris. Task yang menambahkan string hanya-bahasa-Inggris dianggap belum selesai.
4. **Nama fungsi JS, signature, dan behavior global yang sudah ada dipertahankan:** `switchView(viewId)`, `toggleTheme()`, `setLanguage(lang)`, variabel instance chart (`riskChartInstance`, `riskChartInstanceAfter`, `layerChartInstance`, `layerChartInstanceAfter`, `sankeyChartInstance`, `sankeyChartInstanceAfter`), dan nama key yang sudah ada di objek `translations`. Perluas, jangan pernah rename atau hapus.
5. **Pilihan library eksternal sudah tetap:** Chart.js + `chartjs-plugin-datalabels`, Apache ECharts, Marked.js, Phosphor Icons (semuanya dimuat via tag CDN `<script defer>` di `<head>`). Jangan ganti library mana pun dengan library lain, dan hindari menambah dependency berat baru — satu-satunya network request baru opsional yang disahkan dalam seluruh rencana ini adalah mono font satu-weight di Task 10, yang sendiri memerlukan persetujuan eksplisit sebelum diimplementasikan.
6. **Warna aksen brand tetap.** `--accent-primary` (`#0ea5b7` gelap / `#0891a1` terang, warna teal) adalah identitas visual proyek ini di kedua tema dan harus tetap menjadi aksen utama. Token baru (Task 01) memperluas palet; mereka tidak menggantikan aksen ini.
7. **Token severity risiko baru (Task 02) tidak boleh dipakai untuk mengklasifikasi ulang data yang sudah ada.** Token-token ini melengkapi cakupan sistem desain terhadap skala 5-tier yang sudah didefinisikan di `KRITERIA SKALA RISIKO.md`; mereka tidak boleh menyebabkan salah satu dari 11 threat saat ini secara visual berubah tier severity-nya.
8. **Budget motion sengaja dibuat kecil.** Sesuai §2.3, hanya animasi spesifik yang disebutkan di Task 07 (opsional), 09, dan 11 yang disahkan. Jangan menambah scroll-triggered reveal, parallax, stagger entrance kartu, atau animasi apa pun yang tidak eksplisit ditentukan di suatu task — ini artifact akademik/profesional, bukan situs marketing.
9. **Jangan menyentuh atau menghapus `scratch/` atau file yang sudah dicakup oleh rencana cleanup `Rencana-Implementasi-untuk-AI-Coding-Agent.md` yang sudah ada.** Dokumen tersebut sudah memiliki tanggung jawab atas hygiene direktori root (pengarsipan dev-script, meta tags, favicon, dll.); rencana ini hanya mencakup desain visual/UX/aksesibilitas, di atas kondisi repo apa pun yang ditinggalkan oleh rencana lain tersebut. Cek checkbox-nya dulu sebelum mulai untuk menghindari kerja duplikat.
10. **Setiap task harus diverifikasi di kedua tema, 3 breakpoint, dan ≥2 bahasa sebelum ditandai selesai** (sesuai matriks pengujian wajib di §0).

---

## 7. Yang Tidak Boleh Diubah (Daftar Keras)

Untuk kejelasan mutlak, AI coding agent yang mengeksekusi rencana ini **tidak boleh pernah**, di bawah task mana pun dalam dokumen ini:

- Mengubah skor risiko, jumlah threat, klasifikasi severity, pemetaan kontrol, atau angka evaluasi mana pun.
- Mengubah judul skripsi, nama penulis/NIM, nama universitas/fakultas/program, atau tahun publikasi di mana pun mereka muncul (view Home, meta tags, section footer/acknowledgment).
- Me-rename, menghapus, atau mengubah return value/side effect dari `switchView`, `toggleTheme`, atau `setLanguage`.
- Menghapus opsi bahasa dari `#langSwitcher` atau menghapus key dari objek `translations`.
- Mengganti Chart.js, ECharts, Marked.js, atau Phosphor Icons dengan library lain.
- Memperkenalkan package manager, bundler, atau build pipeline (script npm di `scratch/` adalah tooling dev yang sudah ada sebelumnya, bukan bagian dari situs yang di-deploy, dan di luar scope — jangan perluas perannya).
- Mengubah model deployment dari `index.html` statis tunggal di GitHub Pages.
- Mengubah warna aksen brand teal utama ke hue yang berbeda.
- Menghapus atau me-rename salah satu dari tujuh file konten `.md` yang di-fetch saat runtime (`IT RISK ASSESSMENT.md`, `KRITERIA SKALA RISIKO.md`, `Reseach Overview Menu.md`, `Risk Mitigation After Revision.md`, `ZTA Tenet.md`, `daftar_risiko_prioritas.md`, `artifact_evaluation.md`) atau aset gambar mana pun yang benar-benar direferensikan oleh `index.html` atau file `.md` tersebut.
- Mengubah `LICENSE`.

---

## 8. Checklist Sign-Off Akhir (Sebelum Membuka PR)

- [ ] Semua task Fase 0–6 (TASK-00 sampai TASK-13) selesai atau secara eksplisit ditandai "Ditunda" beserta alasannya, sesuai §4/§6.
- [ ] Setiap checkbox kriteria selesai di setiap task yang sudah selesai sudah dicentang.
- [ ] `git diff` diperiksa dari awal sampai akhir untuk memastikan tidak ada perubahan konten/data/teks di luar string i18n baru yang secara eksplisit disahkan.
- [ ] Situs diuji di kedua tema, 3 breakpoint, ≥2 bahasa, navigasi keyboard-only, dan satu pass jaringan yang di-throttle (untuk verifikasi skeleton/lazy-load).
- [ ] Deskripsi PR mereferensikan dokumen ini dengan nama dan mendaftar TASK-ID mana yang selesai, ditunda, atau dilewati, dengan alasan satu baris untuk penundaan mana pun.
- [ ] Screenshot (before/after, dari baseline TASK-00) dilampirkan ke PR untuk review visual.
