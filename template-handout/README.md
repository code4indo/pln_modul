# Template Cover Handout — PLN

Template untuk membuat dokumen handout dengan cover dan halaman konten
menggunakan background PLN.

## Struktur Folder

```
template-cover/
├── cover_handout.tex          ← File LaTeX (kompilasi dengan XeLaTeX/LuaLaTeX)
├── generate_cover.py          ← Script Python (alternatif, langsung ke PDF)
├── cover_handout.png          ← Background halaman cover
├── content_handout.png        ← Background halaman konten (hal. 2+)
├── fonts/
│   ├── OpenSans-Regular.ttf
│   └── OpenSans-Bold.ttf
└── README.md                  ← File ini
```

## Opsi 1: Python (Direktori ke PDF)

### Prasyarat
```bash
pip install fpdf2 Pillow
```

### Jalankan
```bash
cd template-cover
python3 generate_cover.py
```

### Output
- `handout.pdf` — file PDF siap pakai

### Kustomisasi
Edit `generate_cover.py`:
- **Teks cover**: ubah `LEVEL_TEXT`, `TITLE_LINE1`, `TITLE_LINE2`, `BOTTOM_LINE1`, `BOTTOM_LINE2`
- **Teks konten**: ubah `CONTENT_TITLE`, `CONTENT_BODY`
- **Warna**: ubah `TEXT_COLOR_NAVY`, `TEXT_COLOR_BODY`
- **Posisi**: ubah `LEFT_MARGIN`, `Y_POSITION`, `y_bottom`
- **Font size**: ubah `FONT_SIZE_*`

## Opsi 2: LaTeX

### Prasyarat
- XeLaTeX atau LuaLaTeX (fontspec memerlukan engine ini)
- Font Open Sans sudah disertakan di folder `fonts/`

### Jalankan
```bash
cd template-cover
xelatex cover_handout.tex
```

### Output
- `cover_handout.pdf` — file PDF siap pakai

### Kustomisasi
Edit `cover_handout.tex`:
- Teks cover dan konten langsung di source
- Warna: ubah `\definecolor{titlenavy}`
- Posisi: ubah koordinat `xshift`, `yshift` pada node TikZ

## Font

Font yang digunakan: **Open Sans** (Google Fonts, lisensi SIL Open Font License)
- Regular: `fonts/OpenSans-Regular.ttf`
- Bold: `fonts/OpenSans-Bold.ttf`

## Background

| File | Digunakan di |
|------|-------------|
| `cover_handout.png` | Halaman 1 (cover) |
| `content_handout.png` | Halaman 2+ (konten) |
