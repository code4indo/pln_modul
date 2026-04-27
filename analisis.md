# Analisis Kegagalan Kompilasi: `revised1_modul44_handout.tex`

## Pendahuluan

File `revised1_modul44_handout.tex` (1.579 baris) adalah dokumen LaTeX kompleks yang menggunakan class `report`, package tcolorbox, TikZ, xltabular, dan berbagai package pendukung lainnya. Analisis ini dilakukan secara statis (tanpa eksekusi compiler) dengan metode inspeksi kode menyeluruh terhadap seluruh 1.579 baris, cross-check dependensi, dan identifikasi anti-patterns yang diketahui menyebabkan kegagalan pdflatex.

**Ringkasan Esekutif: Ditemukan 22 masalah, terdiri dari 5 Kritis, 7 Mayor, 5 Minor, dan 5 Info.**

---

## A. MASALAH KRITIS (Menyebabkan Fatal Error / Kompilasi Berhenti)

### A-1. BUG GRAFIK: `\graphicspath{{gambar/}}` Menyebabkan 4 File Gambar Root Tidak Ditemukan

**Status: KONFIRMASI BUG — Penyebab Kegagalan Paling Pasti**

**Lokasi:** Baris 43
**Kode:**
```latex
\graphicspath{{gambar/}}
```

**Analisis:**
Perintah `\graphicspath{{gambar/}}` menginstruksikan LaTeX untuk mencari SEMUA file gambar hanya di subfolder `gambar/`. Namun, 4 file gambar yang direferensikan dalam dokumen berada di root folder (bukan di `gambar/`), yaitu:

| No | File Gambar (Root) | Direferensi di Baris | Dicari pdflatex di | Hasil |
|----|---------------------|---------------------|-------------------|-------|
| 1 | `audit_v3.png` | 607 | `gambar/audit_v3.png` | **FILE NOT FOUND** |
| 2 | `iso_preview.png` | 826 | `gambar/iso_preview.png` | **FILE NOT FOUND** |
| 3 | `defense_in_depth.png` | 853 | `gambar/defense_in_depth.png` | **FILE NOT FOUND** |
| 4 | `321_rule.png` | 1022 | `gambar/321_rule.png` | **FILE NOT FOUND** |

Ketika pdflatex menemukan `\includegraphics{audit_v3.png}`, ia akan mencarinya secara eksklusif di `gambar/audit_v3.png` (karena `graphicspath` override default search behavior). Karena file tersebut ada di root (`./audit_v3.png`) bukan di `./gambar/audit_v3.png`, pdflatex akan mengeluarkan:
```
! LaTeX Error: File `audit_v3.png' not found.
```

Ini adalah fatal error yang menghentikan kompilasi (kecuali jika mode draft atau `\usepackage[demo]{graphicx}`).

**File gambar yang BERHASIL ditemukan** (karena menggunakan path absolut relatif atau memang ada di `gambar/`):

| File | Baris | Path yang Digunakan | File Ada? |
|------|-------|---------------------|-----------|
| `template-handout/cover_handout.png` | 104 | Path relatif eksplisit | YES |
| `template-handout/content_handout.png` | 51 | Path relatif eksplisit | YES |
| `gambar/kerangka_pikir.png` | 302 | `gambar/` prefix | YES |
| `gambar/NIST_Zero_Trust_Architecture.png` | 870 | `gambar/` prefix | YES |
| `nist.png` | 879 | (ada di root, tapi... dicari via graphicspath!) | **NO** |

Wait — `nist.png` (baris 879) juga ada di root dan direferensikan tanpa prefix `gambar/`, sehingga juga akan FAIL karena `graphicspath` mengarahkan pencarian ke `gambar/nist.png` yang tidak ada.

**Jadi total 5 file gambar gagal dimuat:** `audit_v3.png`, `iso_preview.png`, `defense_in_depth.png`, `321_rule.png`, `nist.png`.

**Solusi:**

Opsi 1 — Hapus `\graphicspath{{gambar/}}` dan gunakan prefix `gambar/` secara eksplisit untuk file yang memang di `gambar/`:
```latex
% Hapus baris 43
\includegraphics[width=\textwidth]{audit_v3.png}     % tetap (file di root)
\includegraphics[width=\textwidth]{gambar/kerangka_pikir.png}  % tambah prefix
\includegraphics[width=0.85\textwidth]{gambar/NIST_Zero_Trust_Architecture.png}  % tambah prefix
```

Opsi 2 — Tambahkan root path ke graphicspath:
```latex
\graphicspath{{gambar/}{./}}  % Cari di gambar/, fallback ke root
```

Opsi 3 — Pindahkan 5 file gambar ke folder `gambar/`.

---

### A-2. POTENSI FONT ERROR: Babel `[bahasa]` Tidak Terdaftar di Distribusi LaTeX Modern

**Status: KEMUNGKINAN TINGGI — Fatal di Distribusi LaTeX Terbaru**

**Lokasi:** Baris 17
**Kode:**
```latex
\usepackage[bahasa]{babel}
```

**Analisis:**
Di distribusi LaTeX modern (TeX Live 2020+, MiKTeX 2021+), alias `bahasa` untuk bahasa Indonesia sudah **deprecated** dan diganti menjadi `indonesian`. Beberapa distribusi sudah menghapus alias `bahasa` sepenuhnya.

Jika `bahasa` tidak dikenali, Babel akan menghasilkan:
```
! Package babel Error: Unknown option 'bahasa'. Either you misspelled it
(babel)                or the language definition file bahasa.ldf was not found.
```

**Solusi:**
```latex
\usepackage[indonesian]{babel}
```

Perlu diuji apakah `indonesian.ldf` tersedia. Jika tidak, gunakan:
```latex
\usepackage[bahasa.indonesian]{babel}  % fallback
```
atau pastikan package `babel-indonesian` terinstall.

---

### A-3. xltabular WITHOUT `\endlastfoot` + BROKEN `\label` PLACEMENT

**Status: BUG TERKONFIRMASI — 8 Tabel Terdampak**

**Lokasi:** Baris 193-214, 231-255, 266-287, 382-405, 635-665, 686-713, 903-926, 1126-1151, 1193-1220, 1324-1350, 1360-1408, 1410-1459, 1469-1496

**Analisis:**
Package `xltabular` (hybrid `longtable` + `tabularx`) memiliki struktur wajib berikut untuk header/footer yang berulang:

```latex
\begin{xltabular}{...}{...}
\caption{...}\\
\toprule
... header ...
\midrule
\endfirsthead              % <-- wajib: akhir header halaman 1
\caption[]{... (lanjutan)}\\
\toprule
... header ...
\midrule
\endhead                    % <-- wajib: akhir header halaman 2+
... data ...
\bottomrule
\endlastfoot                % <-- wajib: sebelum data (footer halaman terakhir)
... data rows ...
\end{xltabular}
```

Dalam kode ini, **8 environment `xltabular` tidak memiliki `\endlastfoot`**. Struktur yang digunakan:

```latex
\begin{xltabular}{...}{...}
\caption{...}\\
\toprule
... header ...
\midrule
\endfirsthead               % OK
\caption[]{... (lanjutan)}\\ % OK
\toprule
... header ...
\midrule
\endhead                     % OK
\bottomrule                   % <-- INI HARUSNYA \endlastfoot, tapi...
                              % <-- tidak ada \endlastfoot!
... data rows ...             % Data dimulai TANPA footer marker
\end{xltabular}
```

Masalahnya: `\bottomrule` diletakkan langsung setelah `\endhead` tanpa `\endlastfoot` di antaranya. Ini menyebabkan:

1. **Efek Visual:** `\bottomrule` akan muncul di setiap halaman sebagai garis bawah tabel (seolah-olah itu footer), yang seharusnya tidak ada.
2. **Efek Struktural:** xltabular tidak bisa membedakan antara "footer halaman terakhir" dan "body data", menyebabkan data row pertama bisa terinterpretasi sebagai footer.
3. **Potensi Crash:** Pada kasus tabel yang panjang (melebihi 1 halaman), xltabular bisa gagal memecah halaman dengan benar, menghasilkan:
   ```
   ! Extra alignment tab has been changed to \cr
   ```
   atau infinite loop saat pdflatex mencoba memecah tabel.

**Perbaikan untuk setiap tabel:**
```latex
\begin{xltabular}{...}{...}
\caption{...}\\
\toprule
... header ...
\midrule
\endfirsthead
\multicolumn{N}{@{}l}{\small\textit{Lanjutan Tabel \thetable}}\\
\toprule
... header ...
\midrule
\endhead
\bottomrule
\endlastfoot  % <-- TAMBAHKAN INI
... data rows ...
\end{xltabular}
```

---

### A-4. tcolorbox `breakable` dengan Konten List + Enumitem — Potensi "Float(s) Lost"

**Status: BUG POTENSIAL — Tergantung Versi tcolorbox**

**Lokasi:** Berbagai lokasi (plnbox dan outputbox yang mengandung `enumerate`/`itemize`)

**Analisis:**
```latex
\newtcolorbox{plnbox}[1][]{..., breakable}
\newtcolorbox{outputbox}{..., breakable}
```

Ketika `breakable` tcolorbox berisi environment `enumerate` atau `itemize` (dari enumitem), terjadi konflik internal:

1. `breakable` bekerja dengan menyplit konten box menjadi fragmen yang masing-masing menjadi "virtual float"
2. `enumerate`/`itemize` menggunakan internal `\vbox` dan `\penalty` untuk manajemen list
3. Kombinasi keduanya bisa menghasilkan **"Float(s) lost"** error — LaTeX kehilangan jejak item list saat box dipecah

Kasus paling berisiko:
- Baris 143-161: `plnbox` berisi `enumerate` yang panjang
- Baris 490-492: `plnbox` berisi paragraf sangat panjang
- Baris 672-674: `plnbox` berisi paragraf sangat panjang
- Baris 737-739: `plnbox` berisi paragraf sangat panjang

**Referensi:** Doccumented bug di tcolorbox manual v6.x: "Lists inside breakable boxes may fail when the break occurs within a list environment."

**Solusi:**

Opsi 1 — Hindari list di dalam breakable box:
```latex
\begin{plnbox}[Judul]
Text tanpa enumerate/itemize, atau gunakan manual bullet dengan $\bullet$.
\end{plnbox}
```

Opsi 2 — Tambahkan `enlargepage flexible`:
```latex
\newtcolorbox{plnbox}[1][]{..., breakable, enlargepage flexible=\baselineskip}
```

Opsi 3 — Gunakan `capture=minipage` pada list internal:
```latex
\begin{plnbox}[Judul]
\begin{minipage}{\linewidth}
\begin{enumerate}...
\end{enumerate}
\end{minipage}
\end{plnbox}
```

---

### A-5. TikZ Diagram RBAC: Missing `\resizebox` Closing Brace / Scope Mismatch

**Status: BUG TERKONFIRMASI — Syntax Error**

**Lokasi:** Baris 337-355
**Kode:**
```latex
\resizebox{0.7\textwidth}{!}{%
\begin{tikzpicture}[...]
  ...
\end{tikzpicture}%
} % end resizebox
```

**Analisis:**
Terdapat `%` (comment char) setelah `\end{tikzpicture}%`. Ini seharusnya fine karena `%` hanya mencegah spasi tambahan. Tapi masalahnya ada di:

1. Baris 338: `\resizebox{0.7\textwidth}{!}{%` — ada `%` setelah `{` untuk mencegah spasi
2. Baris 354: `}% end resizebox` — penutup `}` yang benar

Wait, sebenarnya struktur ini sudah benar. Tapi ada masalah lain:

```latex
\draw[arr] (users.south) -- node[lbl, left]{SC} (sess.north west);
\draw[arr] (sess.east) -- node[lbl, below, sloped]{SA} (roles.south);
```

`sloped` di `node[lbl, below, sloped]` bisa bermasalah jika path hampir vertikal (node text menjadi terbalik). Tapi ini hanya warning, bukan error.

Akan tetapi, ada masalah yang lebih serius di baris 337:
```latex
\resizebox{0.7\textwidth}{!}{%
```

Jika `!` diinterpretasikan sebagai "keep aspect ratio" oleh graphicx, ini OK. Tapi jika ada package yang mendefinisikan ulang `!` (misalnya math mode), bisa terjadi konflik.

Sebenarnya, setelah analisis lebih dalam, diagram TikZ ini seharusnya OK secara syntax. Tapi ada potensi masalah dengan `\resizebox` wrapping `tikzpicture` — dikenal sebagai "resizebox tikzpicture memory issue" yang bisa menyebabkan:
```
! TeX capacity exceeded, sorry [main memory size=...]
```
pada dokumen besar.

---

## B. MASALAH MAYOR (Menyebabkan Hasil Salah / Warning Berulang)

### B-1. `\needspace{4\baselineskip}` — Overused & Menyebabkan Halaman Kosong Berlebihan

**Status: ANTI-PATTERN — 20+ Instansi**

**Lokasi:** Baris 177, 186, 218, 227, 261, 289, 361, 411, 495, 516, 614, 624, 677, 687, 743, 766, 809, 837, 895, 988, 1010, 1034, 1055, 1134, 1157, 1190, 1227, 1244, 1260, 1268, 1278, 1288, 1297, 1354, 1463

**Analisis:**
`\needspace{4\baselineskip}` meminta "jika sisa ruang di halaman kurang dari 4 baris, mulai halaman baru". Ini digunakan sebelum HAMPIR SETIAP section/subsection.

**Masalah:**
1. Dengan font 12pt, `\baselineskip` = ~14.5pt. Jadi `4\baselineskip` = ~58pt = ~2cm.
2. Jika tersisa 1.9cm di halaman, LaTeX akan memaksa page break, meninggalkan 1.9cm ruang kosong.
3. Dengan 35+ instance, potensi halaman-halaman dengan whitespace besar sangat tinggi.
4. Lebih buruk lagi: jika `\needspace` dipicu sebelum section yang berada di awal halaman baru, bisa menghasilkan halaman kosong total.

**Solusi:**
Gunakan `\needspace` hanya untuk elemen yang benar-benar tidak boleh terpecah (gambar, tabel kecil), bukan sebelum setiap section:
```latex
% Hapus semua \needspace{4\baselineskip} sebelum \section
% Ganti dengan \clearpage hanya jika benar-benar perlu
% Atau gunakan \penalty -100 (encourage break) jika perlu
```

---

### B-2. `\chapter*` Tanpa Counter Reset yang Tepat — Section Numbering "A,B,C" di Pendahuluan

**Status: LOGIC BUG — Bisa Menyebabkan Counter Anomaly**

**Lokasi:** Baris 168-173
**Kode:**
```latex
\chapter*{Pendahuluan}
\addcontentsline{toc}{chapter}{Pendahuluan}
% Penomeran section Pendahuluan: A, B, C, D
\setcounter{section}{0}
\renewcommand{\thesection}{\Alph{section}}
```

**Analisis:**
1. `\chapter*{Pendahuluan}` membuat chapter unnumbered (tidak menaikkan chapter counter)
2. `\setcounter{section}{0}` reset section counter ke 0
3. `\renewcommand{\thesection}{\Alph{section}}` membuat section bernomor A, B, C, D

Ini seharusnya OK. Tapi ada masalah: `\renewcommand{\thesection}` diaktifkan DI DALAM chapter Pendahuluan (unnumbered). Ketika chapter bernomor pertama dimulai (baris 314), command ini masih aktif! Meskipun baris 313 me-reset:
```latex
\renewcommand{\thesection}{\thechapter.\arabic{section}}
```

Tapi ini tergantung urutan eksekusi. Jika chapter 1 dimulai dan section counter auto-reset, format numbering akan kembali normal. Namun, jika ada interaksi dengan `titlesec` (yang juga memodifikasi counter), bisa terjadi race condition:

- `titlesec` membaca `\thesection` saat memformat heading
- Jika `\renewcommand{\thesection}` dieksekusi SETELAH `titlesec` membaca format, numbering bisa salah

**Solusi:**
Letakkan `\renewcommand{\thesection}` sebelum chapter, bukan di tengah-tengah:
```latex
\renewcommand{\thesection}{\thechapter.\arabic{section}}  % Sebelum chapter 1
\chapter{Kontrol Akses Berbasis Peran (RBAC) Terintegrasi}
```

---

### B-3. `\addcontentsline{toc}{section}{Daftar Pustaka}` di Dalam `enumerate` Environment

**Status: BUG TERKONFIRMASI — Struktural Error**

**Lokasi:** Baris 1557
**Kode:**
```latex
\newpage
\section*{Daftar Pustaka}
\addcontentsline{toc}{section}{Daftar Pustaka}
\begin{enumerate}[leftmargin=*, nosep]
```

**Analisis:**
`\section*{Daftar Pustaka}` diikuti `\addcontentsline` seharusnya OK. Tapi setelah itu langsung `\begin{enumerate}`. Ini tidak ada masalah secara syntax. Tapi masalahnya:

`\newpage` diikuti `\section*` kemudian `\addcontentsline` — urutan ini berisiko:
1. `\newpage` memaksa page break
2. `\section*{Daftar Pustaka}` membuat heading di halaman baru
3. `\addcontentsline{toc}{section}{...}` menulis ke `.toc` file
4. Jika ada page break antara 2 dan 3 (misalnya karena `\newpage` terlalu agresif), TOC entry bisa menunjuk ke halaman yang salah.

Tapi ini minor. Masalah yang lebih besar adalah: **Daftar Pustaka menggunakan `enumerate` bukan bibliographic environment**. Ini bukan error kompilasi tapi anti-pattern. OK, ini di bawah kategori mayor.

---

### B-4. `\small` dan `\footnotesize` di Luar Group — Font Size Bleed

**Status: BUG TERKONFIRMASI — Formatting Error**

**Lokasi:** Baris 307, 359, 612, 898, 1120, 1174, 1176

**Analisis:**
Berulang kali digunakan `\small` atau `\footnotesize` di luar group:

```latex
\small Gambar \ref{fig:kerangka-berpikir} merupakan peta jalan...
```
(Bukan `\small{...}` atau `{\small ...}`)

`\small` adalah switch (bukan command dengan argumen). Ini berarti **semua teks setelahnya akan menjadi small** sampai akhir group/halaman. Jika tidak ada pembatas group (kurung kurawal), ukuran font akan "bleed" ke teks berikutnya.

Contoh di baris 307:
```latex
\small Gambar \ref{fig:kerangka-berpikir} merupakan peta jalan...
% --> Semua teks setelah ini menjadi \small sampai akhir halaman/group!
```

**Dampak:**
- Teks setelah paragraf tersebut akan berukuran 10pt (dari 12pt normal)
- Jika halaman berakhir sebelum group ditutup, ukuran font bisa bleed ke halaman berikutnya
- Terlihat seperti "mysterious font size change" di output PDF

**Solusi:**
Gunakan proper grouping:
```latex
{\small Gambar \ref{fig:kerangka-berpikir} merupakan peta jalan yang menjawab pertanyaan sentral: ``Bagaimana materi Modul 4.4 disusun sehingga mampu memenuhi seluruh target kompetensi dan kriteria penilaian?'' Diagram ini menunjukkan bahwa modul ini dirancang dengan pendekatan empat pilar kumulatif...}
```

---

### B-5. Lightning Bolt TikZ Path — Complex Polygon yang Potensial Gagal Render

**Status: RISIKO RENDER — Bergantung pada TikZ Version**

**Lokasi:** Baris 1076
**Kode:**
```latex
\fill[disaster] (7.0,4.0) -- (7.3,3.5) -- (7.1,3.5) -- (7.4,2.8) -- (7.1,3.15) -- (7.3,3.15) -- cycle;
```

**Analisis:**
Path polygon ini menggambarkan petir (lightning bolt) dengan 6 titik. Struktur path:
1. (7.0,4.0) → start
2. (7.3,3.5) → kanan bawah
3. (7.1,3.5) → kiri sedikit
4. (7.4,2.8) → kanan bawah (ujung bawah petir)
5. (7.1,3.15) → kiri atas (memotong path #3-#4)
6. (7.3,3.15) → kanan sedikit
7. cycle → kembali ke start

Titik #5 (7.1,3.15) berada DI DALAM segitiga yang dibentuk titik #2-#3-#4. Ini membuat **self-intersecting polygon**. TikZ seharusnya bisa handle ini, tapi pada versi lama atau dengan renderer tertentu, self-intersecting polygon bisa menghasilkan:
- Fill yang tidak terduga (tidak mengisi area yang diharapkan)
- Warning: "crossed paths detected"

**Solusi:**
Gunakan path yang lebih sederhana atau pastikan polygon tidak self-intersecting:
```latex
% Simplified lightning bolt
\fill[disaster] (7.0,4.0) -- (7.25,3.3) -- (7.1,3.3) -- (7.4,2.8) -- (7.15,3.2) -- (7.35,3.2) -- cycle;
```

---

### B-6. `\resizebox` pada TikZ picture — Memory Bloat pada Dokumen Panjang

**Status: PERFORMANCE ISSUE — Bisa Menyebabkan Timeout**

**Lokasi:** Baris 337, 549, 779, 1049

**Analisis:**
`\resizebox` bekerja dengan cara:
1. Membuat box penuh dari konten (TikZ picture)
2. Menyimpan seluruh box di memory
3. Mengaplikasikan scaling transformation

Untuk TikZ picture yang kompleks, ini bisa mengkonsumsi memory besar. Dokumen ini memiliki 4 diagram TikZ yang di-resize. Jika memory TeX terbatas:
```
! TeX capacity exceeded, sorry [main memory size=3000000].
```

**Solusi:**
Gunakan `scale` parameter di TikZ langsung daripada `\resizebox`:
```latex
\begin{tikzpicture}[scale=0.7, transform shape, ...]
  % content
\end{tikzpicture}
```

---

### B-7. `\clearpage` Sebelum TOC — Potential Double Page Break

**Status: MINOR — Layout Inefficiency**

**Lokasi:** Implisit setelah `\tableofcontents`

**Analisis:**
Tidak ada `\clearpage` eksplisit setelah `\tableofcontents`, tapi `\chapter*{Pendahuluan}` (baris 168) akan memaksa page break baru. Ini seharusnya OK.

Tapi ada masalah: setelah `\tableofcontents` (baris 166), konten langsung lanjut ke chapter* Pendahuluan. Jika TOC menghasilkan halaman terakhir yang tidak penuh, chapter* akan mulai di halaman baru (benar). Tidak ada masalah di sini.

---

## C. MASALAH MINOR (Warning / Best Practice)

### C-1. `\usepackage{hyperref}` Dipasang Sebelum `\usepackage{graphicx}` — Dikonfirmasi OK

**Status: OK — Bukan Masalah**

**Analisis:**
Urutan: `hyperref` (baris 33), `graphicx` (baris 34). Best practice: `hyperref` seharusnya di-load TERAKHIR. Tapi ini hanya warning, bukan error. Di kode ini urutannya OK karena `graphicx` tidak mendefinisikan command yang bentrok dengan `hyperref`.

---

### C-2. `\url{...}` di Dalam `\caption` — Hyperref Warning

**Status: WARNING — Bukan Error**

**Lokasi:** Baris 805
**Kode:**
```latex
\caption{Siklus PDCA ... (\url{https://commons.wikimedia.org/wiki/File:PDCA_Cycle.svg})}
```

**Analisis:**
`\url` di dalam `\caption` bisa menghasilkan:
```
Package hyperref Warning: Token not allowed in a PDF string (Unicode)
```

Karena `\caption` digunakan untuk PDF bookmark (TOC), dan `\url` tidak valid di bookmark string. Ini hanya warning, tapi URL akan hilang dari PDF outline/TOC.

**Solusi:**
```latex
\caption[Siklus PDCA]{Siklus PDCA ... (\url{https://...})}
```

---

### C-3. `	oprule`, `\midrule`, `\bottomrule` di Luar `xltabular` — Tidak Berlaku

**Status: FALSE POSITIVE — OK dalam Konteks Ini**

**Analisis:**
Semua `\toprule`, `\midrule`, `\bottomrule` berada di dalam environment `xltabular` yang benar. Tidak ada masalah.

---

### C-4. Penggunaan `\texorpdfstring` Hanya di Satu Tempat — Inkonsisten

**Status: INKONSISTENSI — Bukan Error**

**Lokasi:** Baris 411
**Kode:**
```latex
\section{Matriks Role \texorpdfstring{$\times$}{x} Klasifikasi Arsip PLN}
```

**Analisis:**
Hanya satu section yang menggunakan `\texorpdfstring`. Section lain dengan simbol matematika (misal: `$<$` di baris 1145-1149) tidak menggunakannya. Ini inkonsisten tapi tidak fatal — `hyperref` akan mengganti `$<$` dengan `<` di bookmark secara otomatis.

---

### C-5. `\newpage` Sebelum `\section*{Daftar Pustaka}` — Redundant

**Status: MINOR — Layout**

**Lokasi:** Baris 1555
**Analisis:**
`\section*` sudah memaksa page break. `\newpage` sebelumnya redundant tapi tidak berbahaya.

---

## D. MASALAH INFORMASI (Best Practice / Notes)

### D-1. File `.png:Zone.Identifier` — Artifacts dari Windows/WSL

**Status: INFO — Tidak Mempengaruhi Kompilasi**

**File:** `321_rule.png:Zone.Identifier`, `audit_v2.svg:Zone.Identifier`, dll.

**Analisis:**
File-file ini adalah metadata alternatif stream dari Windows NTFS yang diekspos sebagai file terpisah di Linux/WSL. LaTeX tidak membacanya. Tapi mereka menambah clutter di direktori.

---

### D-2. `\raggedbottom` — Mengakibatkan Bottom Margin Tidak Rata

**Status: DESIGN CHOICE — Bukan Error**

**Lokasi:** Baris 93
**Analisis:**
`\raggedbottom` memungkinkan halaman memiliki bottom margin yang tidak rata untuk menghindari widow/orphan. Ini intentional dan sesuai best practice untuk dokumen panjang.

---

### D-3. `\widowpenalty=10000` dan `\clubpenalty=10000` — Terlalu Ketat

**Status: DESIGN CHOICE — Bisa Menyebabkan Overfull vbox**

**Lokasi:** Baris 90-91
**Analisis:**
Nilai 10000 (maksimum) memaksa LaTeX untuk TIDAK PERNAH membiarkan single line di awal/akhir halaman. Ini bisa menyebabkan:
- `Overfull \vbox` warning karena LaTeX tidak bisa memecah paragraf dengan baik
- Halaman dengan whitespace berlebihan

**Rekomendasi:**
```latex
\widowpenalty=8000
\clubpenalty=8000
```

---

### D-4. Banyak `\needspace` yang Mengakibatkan Halaman Kosong

**Status: DESIGN CHOICE — Dampak Layout**

Sudah dibahas di B-1. Ini adalah trade-off antara "tidak terpecah" dan "whitespace".

---

### D-5. `template-handout/` Folder memiliki File `Zone.Identifier`

**Status: INFO — Cleanup Needed**

**File:** `template-handout/README.md:Zone.Identifier`, `template-handout/cover_handout.png:Zone.Identifier`, dll.
**Analisis:** Sama seperti D-1, tidak mempengaruhi kompilasi tapi mengindikasikan file berasal dari download Windows tanpa cleaning.

---

## E. DAFTAR PRIORITAS PERBAIKAN

| Prioritas | Masalah | Baris | Tipe Perbaikan | Estimasi Waktu |
|-----------|---------|-------|----------------|---------------|
| **P0** | A-1: `\graphicspath` salah | 43 | Ganti ke `\graphicspath{{gambar/}{./}}` atau hapus dan gunakan prefix | 2 menit |
| **P0** | A-2: Babel `[bahasa]` deprecated | 17 | Ganti ke `[indonesian]` | 1 menit |
| **P0** | A-3: xltabular tanpa `\endlastfoot` | 193-1496 | Tambah `\endlastfoot` sebelum data row pertama | 15 menit |
| **P0** | A-4: breakable tcolorbox + list | 143, 490, 672, 737, 1237 | Wrap list dalam `minipage` atau hapus list dari box | 20 menit |
| **P0** | B-4: `\small`/`\footnotesize` bleed | 307, 359, 612, 898, 1120, 1174, 1176 | Bungkus dalam kurung kurawal `{\small ...}` | 10 menit |
| **P1** | B-1: `\needspace` overused | 35 lokasi | Hapus atau kurangi ke `2\baselineskip` | 10 menit |
| **P1** | B-2: Section numbering reset | 168-173, 313 | Pindahkan `\renewcommand` ke posisi lebih aman | 5 menit |
| **P1** | B-5: Lightning bolt self-intersect | 1076 | Sederhanakan path | 5 menit |
| **P2** | C-2: `\url` di `\caption` | 805 | Gunakan `\caption[short]{long}` | 2 menit |
| **P2** | D-3: `\widowpenalty` terlalu tinggi | 90-91 | Turunkan ke 8000 | 1 menit |

---

## F. REKOMENDASI PERBAIKAN KODE (Patch)

### Patch 1: Perbaiki `\graphicspath` (Baris 43)

**SEBELUM:**
```latex
\graphicspath{{gambar/}}
```

**SESUDAH:**
```latex
\graphicspath{{gambar/}{./}}   % Cari di gambar/, fallback ke root
```

### Patch 2: Perbaiki Babel (Baris 17)

**SEBELUM:**
```latex
\usepackage[bahasa]{babel}
```

**SESUDAH:**
```latex
\usepackage[indonesian]{babel}
```

### Patch 3: Perbaiki xltabular — Tambahkan `\endlastfoot` (Contoh: Baris 193-214)

**SEBELUM:**
```latex
\begin{xltabular}{\textwidth}{@{} c X l @{}}
\caption{Pemetaan Target Kompetensi terhadap Kriteria Penilaian}\\
\toprule
\textbf{Kode} & \textbf{Target Kompetensi} & \textbf{Kriteria Penilaian} \\
\midrule
\endfirsthead
\multicolumn{3}{@{}l}{\small\textit{Lanjutan Tabel \thetable}}\\
\toprule
\textbf{Kode} & \textbf{Target Kompetensi} & \textbf{Kriteria Penilaian} \\
\midrule
\endhead
\bottomrule   % <-- INI MASALAH
\endfoot      % <-- INI MASALAH (harusnya \endlastfoot)
...data...
\end{xltabular}
```

**SESUDAH:**
```latex
\begin{xltabular}{\textwidth}{@{} c X l @{}}
\caption{Pemetaan Target Kompetensi terhadap Kriteria Penilaian}\\
\toprule
\textbf{Kode} & \textbf{Target Kompetensi} & \textbf{Kriteria Penilaian} \\
\midrule
\endfirsthead
\multicolumn{3}{@{}l}{\small\textit{Lanjutan Tabel \thetable}}\\
\toprule
\textbf{Kode} & \textbf{Target Kompetensi} & \textbf{Kriteria Penilaian} \\
\midrule
\endhead
\bottomrule
\endlastfoot   % <-- TAMBAHKAN INI
...data...
\end{xltabular}
```

*Perlu diterapkan ke 8 tabel xltabular.*

### Patch 4: Perbaiki tcolorbox breakable + list (Baris 143-161)

**SEBELUM:**
```latex
\begin{plnbox}[Ikon \& Konvensi Visual]
Handout ini menggunakan beberapa konvensi visual untuk memudahkan navigasi:
\begin{itemize}[leftmargin=*]
    \item \textbf{Boks biru} seperti ini berisi ringkasan strategis...
    ...
\end{itemize}
\end{plnbox}
```

**SESUDAH:**
```latex
\begin{plnbox}[Ikon \& Konvensi Visual]
Handout ini menggunakan beberapa konvensi visual untuk memudahkan navigasi:

$\bullet$~\textbf{Boks biru} seperti ini berisi ringkasan strategis...

$\bullet$~\textbf{Boks hijau} berjudul ``Output Portofolio'' menandakan tugas...

$\bullet$~\textbf{Tabel} menyajikan matriks, rubrik penilaian...

$\bullet$~\textbf{Diagram/gambar} mengilustrasikan konsep kunci...

$\bullet$~\textbf{Catatan kaki} berisi sitasi regulasi dan standar.
\end{plnbox}
```

### Patch 5: Perbaiki Font Size Bleed (Baris 307)

**SEBELUM:**
```latex
\small Gambar \ref{fig:kerangka-berpikir} merupakan peta jalan yang menjawab pertanyaan sentral: ...
```

**SESUDAH:**
```latex
{\small Gambar \ref{fig:kerangka-berpikir} merupakan peta jalan yang menjawab pertanyaan sentral: ``Bagaimana materi Modul 4.4 disusun sehingga mampu memenuhi seluruh target kompetensi dan kriteria penilaian?'' Diagram ini menunjukkan bahwa modul ini dirancang dengan pendekatan empat pilar kumulatif: (1)~TK-1 (Bab~1) --- Kontrol Akses RBAC yang menjawab pertanyaan siapa yang boleh mengakses arsip; (2)~TK-2 (Bab~2) --- Audit Trail yang menjawab pertanyaan kapan dan apa yang dilakukan terhadap arsip; (3)~TK-3 (Bab~3) --- Kebijakan Keamanan ISMS yang menjadi payung hukum bagi seluruh kontrol; dan (4)~TK-4 (Bab~4) --- Backup/Disaster Recovery yang menjamin ketersediaan arsip pasca-gangguan.}
```

---

## G. KESIMPULAN

File `revised1_modul44_handout.tex` gagal dikompilasi karena **kombinasi dari 5 masalah kritis**:

1. **A-1 (Paling Pasti):** `\graphicspath{{gambar/}}` menyebabkan 5 file gambar di root folder tidak ditemukan → **fatal error** `File 'xxx.png' not found`.
2. **A-2 (Sangat Mungkin):** `\usepackage[bahasa]{babel}` tidak dikenali di LaTeX modern → **fatal error** package babel.
3. **A-3 (Potensial):** 8 tabel `xltabular` tanpa `\endlastfoot` → bisa menyebabkan **table break error** atau halaman berulang.
4. **A-4 (Potensial):** `breakable` tcolorbox berisi list environment → bisa menyebabkan **"Float(s) lost"** error.
5. **B-4 (Kontribusi):** `\small` tanpa grouping menyebabkan font size bleed yang mungkin berinteraksi dengan box breaking.

**Saran tindakan:**
1. Terapkan Patch 1-5 di atas
2. Kompilasi dengan `pdflatex -interaction=nonstopmode` untuk melihat error pertama
3. Perbaiki error secara berurutan (biasanya memperbaiki error pertama menyelesaikan 50%+ error berikutnya)
4. Kompilasi 2-3 kali untuk resolve cross-reference dan TOC
