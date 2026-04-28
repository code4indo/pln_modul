# AGENTS.md — Panduan untuk AI Coding Agent

Dokumen ini ditujukan bagi agen AI yang akan membantu pengembangan atau pemeliharaan proyek ini. Proyek ini **bukan proyek perangkat lunak dalam arti tradisional**, melainkan **proyek dokumen pelatihan berbasis LaTeX**.

---

## Ikhtisar Proyek

Proyek ini adalah sumber terbuka (source files) untuk **Modul 4.3: Optimalisasi Prosedur dan Alur Kerja Terintegrasi** — bagian dari kurikulum *Center of Excellence Records Management* milik **PT PLN (Persero)**. Level kompetensi yang ditargetkan adalah **Level 4 (Mastery)**, ditujukan untuk Manajemen Atas.

Semua dokumen ditulis dalam **Bahasa Indonesia**. Standar regulasi yang menjadi rujukan meliputi PP 71/2019, Perka ANRI, ISO 15489, PARBICA Guideline, serta standar BUMN terkait tata kelola dan kearsipan digital.

---

## Teknologi & Stack

| Komponen | Detail |
|----------|--------|
| **Typesetting Engine** | LaTeX (pdfLaTeX/XeLaTeX) |
| **Document Class — Modul** | `report` (12pt, a4paper) |
| **Document Class — Handout** | `article` (11pt, a4paper) |
| **Document Class — Slide** | `beamer` (aspectratio=169, 11pt) |
| **Diagram & Grafik** | TikZ + PGF (extensive custom BPMN/flow styles) |
| **Tabel** | `booktabs`, `tabularx` |
| **Kotak Kustom** | `tcolorbox` |
| **Bahasa** | `babel[bahasa]`, encoding UTF-8 |
| **Font Handout** | Helvetica (`\sfdefault`) via `helvet` |
| **Warna Korporat** | PLN Blue `RGB(0,75,135)`, PLN Orange `RGB(255,107,53)`, PLN Cyan `RGB(0,163,224)` |

---

## Struktur Direktori & Organisasi File

```
pln_modul/
├── assets/                           # Aset gambar statis (PNG)
│   ├── ADKAR_Model.png
│   ├── Balanced_Scorecard.png
│   ├── Blockchain_Hash_Chain.png
│   ├── Kotters_8_Step.png
│   ├── Power-Interest_Grid.png
│   └── rc1.png, rc2.png, rc3.png     # Records Continuum visualisasi
├── fakta/                            # Catatan riset & verifikasi faktual
│   ├── fakta1.md                     # Verifikasi keanggotaan ANRI di PARBICA
│   ├── fakta2.md                     # Analisis gap PARBICA Guideline 13
│   ├── fakta3.md                     # Definisi intervensi operasional
│   ├── fakta4.md                     # Standar metadata wajib (12 field)
│   ├── fakta5.md                     # Klarifikasi "SOP Digital 8 Komponen"
│   ├── fakta6.md                     # Alasan pengecualian metadata deskriptif
│   └── fakta7.md                     # Asal-usul 7 Domain Evaluasi
├── bab1-2.tex                        # Bab 1: Pendahuluan + Bab 2: Evaluasi Prosedur
├── bab3-4.tex                        # Bab 3–4: Penyusunan SOP Digital Terintegrasi
├── bab5-6.tex                        # Bab 5: Penghitungan Efisiensi & ROI + Bab 6: Penutup
├── slide_presentasi.tex              # Slide Beamer (~112 frame)
├── handout.tex                       # Handout eksekutif ringkasan
├── pretest.tex                       # Soal pre-test peserta
├── posttest.tex                      # Soal post-test peserta
├── lampiran.tex                      # Lembar kerja (worksheet) kosong
├── contoh_lampiran.tex               # Contoh pengisian lembar kerja
├── lampiran_checklist_parbica.tex    # Checklist Diagnostik PARBICA
├── glosarium.tex                     # Glosarium istilah Modul 4.3 & 4.4
└── narasi.md                         # Naskah verbatim narasumber (speaker script)
```

### File Bersih vs. File Build
- File `.tex` adalah **sumber utama** yang harus diedit.
- File `.pdf` adalah **output build**; perlu diregenerasi setelah edit `.tex`.
- File `.aux`, `.log`, `.out`, `.toc`, `.nav`, `.snm`, `.vrb` adalah **artefak build LaTeX** dan diabaikan oleh `.gitignore`.

---

## Proses Build

Tidak ada Makefile atau skrip otomatis. Build dilakukan secara manual dengan perintah berikut:

```bash
# Modul Bab 1–2
pdflatex bab1-2.tex

# Modul Bab 3–4
pdflatex bab3-4.tex

# Modul Bab 5–6
pdflatex bab5-6.tex

# Slide presentasi
pdflatex slide_presentasi.tex

# Handout
pdflatex handout.tex

# Pre-test / Post-test
pdflatex pretest.tex
pdflatex posttest.tex

# Lampiran & glosarium
pdflatex lampiran.tex
pdflatex contoh_lampiran.tex
pdflatex lampiran_checklist_parbica.tex
pdflatex glosarium.tex
```

> **Catatan:** Jika dokumen menggunakan referensi silang (cross-ref) atau Daftar Isi, kompilasi **2×** diperlukan agar nomor halaman dan hyperlink benar.

---

## Konvensi Pengembangan

### Warna Korporat PLN
Setiap file `.tex` **wajib** mendefinisikan warna korporat berikut **sebelum** `\usepackage{hyperref}`:

```latex
\definecolor{plnblue}{RGB}{0,75,135}
\definecolor{plnorange}{RGB}{255,107,53}
```

Beberapa file juga menggunakan:
```latex
\definecolor{plncyan}{RGB}{0,163,224}
\definecolor{plngreen}{RGB}{0,150,136}
```

### Header & Footer
- Modul: `\fancyhead[L]{Modul 4.3: ...}`, `\fancyhead[R]{Level 4 (Mastery) -- PLN}`
- Handout: `\fancyhead[L]{Handout Eksekutif: Modul 4.3}`, `\fancyhead[R]{PT PLN (Persero) -- Level 4 (Mastery)}`

### Kotak Kustom (tcolorbox)
Semua modul menggunakan kotak kustom `plnbox` dan `notebox` dengan skema warna seragam:
```latex
\newtcolorbox{plnbox}[1][]{%
  colback=plnblue!5!white, colframe=plnblue, fonttitle=\bfseries,
  title=#1, sharp corners, boxrule=0.8pt, breakable}
```

### TikZ Styles (Slide)
File `slide_presentasi.tex` mendefinisikan banyak *TikZ styles* khusus untuk diagram BPMN:
- `startstyle`, `endstyle`, `manual`, `waiting`, `autostep`, `humanstep`
- `gateway`, `arr`, `arr_tobe`, `apimsg`
- `meta`, `docstyle`

**Jangan mengubah nama style ini** tanpa memperbarui semua node yang merujuknya di seluruh frame.

### Penomoran Bab
| File | Bab |
|------|-----|
| `bab1-2.tex` | 1. Pendahuluan; 2. Evaluasi Prosedur Yang Ada & Identifikasi Area Optimasi |
| `bab3-4.tex` | 3. (disesuaikan); 4. Penyusunan SOP Digital Terintegrasi |
| `bab5-6.tex` | 5. Penghitungan Efisiensi & ROI; 6. Penutup & Refleksi |

---

## Strategi Verifikasi & Fakta

Direktori `fakta/` berisi catatan riset mandiri untuk memastikan akurasi klaim dalam modul. Ini bukan bagian dari output PDF, melainkan **dokumen internal** untuk:
- Memverifikasi keanggotaan organisasi (misal: ANRI bukan anggota PARBICA, melainkan SARBICA).
- Mengklarifikasi apakah standar internasional benar-benar menyebutkan klaim tertentu.
- Menyusun kerangka evaluasi (7 Domain) dengan dasar akademik/regulasi yang transparan.

**Konvensi:** Jika menambahkan klaim baru terkait standar internasional atau regulasi, **wajib** membuat file `faktaN.md` baru yang mendokumentasikan sumber dan klarifikasinya.

---

## Panduan Edit yang Aman

1. **Selalu edit file `.tex`, bukan `.pdf`.**
2. **Setelah edit, build ulang** dengan `pdflatex` dan verifikasi PDF hasilnya.
3. **Jangan commit file build** (`.aux`, `.log`, `.out`, `.toc`, `.nav`, `.snm`, `.vrb`, `.fls`, `.fdb_latexmk`, `.synctex.gz`). File ini sudah di-`.gitignore`.
4. **Gambar statis** (`assets/`, `*.png` di root) boleh di-commit karena merupakan dependensi dokumen.
5. **TikZ diagrams** yang kompleks berada *inline* di dalam file `.tex`. Edit dengan hati-hati agar koordinat node tidak tergeser.
6. **`narasi.md`** adalah naskah verbatim narasumber. Perubahan pada slide harus disinkronkan dengan narasi jika mempengaruhi urutan atau isi yang disebutkan narasumber.

---

## Keamanan & Lisensi

- Proyek ini berisi materi pelatihan internal untuk BUMN. Pastikan tidak ada informasi yang bersifat **rahasia perusahaan (proprietary/confidential)** yang tidak semestinya dipublikasikan.
- Remote GitHub: `https://github.com/code4indo/pln_modul.git`
- Tidak ada dependensi eksternal selain distribusi LaTeX standar (TeX Live / MiKTeX).

---

# gaya bahasa 

gunakan gaya bahasa formal, hindari menggunakan kalimat  / kata kiasan / metaforis

## Ringkasan Perintah untuk Agen

```bash
# Build semua dokumen utama
pdflatex bab1-2.tex && pdflatex bab3-4.tex && pdflatex bab5-6.tex
pdflatex slide_presentasi.tex
pdflatex handout.tex
pdflatex pretest.tex && pdflatex posttest.tex
pdflatex lampiran.tex && pdflatex contoh_lampiran.tex
pdflatex lampiran_checklist_parbica.tex
pdflatex glosarium.tex

# Cek status git
git status

# Commit perubahan
git add <file.tex> <assets/jika ada>
git commit -m "<deskripsi perubahan dalam Bahasa Indonesia>"
```
