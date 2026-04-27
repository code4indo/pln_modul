#!/usr/bin/env python3
"""Generate handout PDF with cover page + content pages.

Cara penggunaan:
  1. Ekstrak template-cover.zip
  2. cd template-cover
  3. pip install fpdf2 Pillow
  4. python3 generate_cover.py

File PDF akan dihasilkan: handout.pdf
"""

from fpdf import FPDF
from PIL import Image
import os

# --- Base directory (sama dengan lokasi script ini) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- File paths (relative ke BASE_DIR) ---
COVER_BG    = os.path.join(BASE_DIR, "cover_handout.png")
CONTENT_BG  = os.path.join(BASE_DIR, "content_handout.png")
FONT_REG    = os.path.join(BASE_DIR, "fonts", "OpenSans-Regular.ttf")
FONT_BOLD   = os.path.join(BASE_DIR, "fonts", "OpenSans-Bold.ttf")
OUTPUT      = os.path.join(BASE_DIR, "handout.pdf")

# --- Teks Cover ---
LEVEL_TEXT   = "LEVEL MANEJERIAL"
TITLE_LINE1  = "PERANCANGAN SISTEM KEAMANAN"
TITLE_LINE2  = "& KETERLACAKAN TERINTEGRASI"
BOTTOM_LINE1 = "PUSAT PENDIDIKAN DAN PELATIHAN"
BOTTOM_LINE2 = "PT PLN (PERSERO)"

# --- Teks Content (placeholder) ---
CONTENT_TITLE = "PENDAHULUAN"
CONTENT_BODY  = (
    "Ini adalah contoh teks konten untuk halaman kedua dan seterusnya. "
    "Ganti teks ini sesuai kebutuhan materi Anda."
)

# --- Style ---
FONT_SIZE_LEVEL   = 14
FONT_SIZE_TITLE   = 16
FONT_SIZE_BOTTOM  = 14
FONT_SIZE_CONTENT_TITLE = 16
FONT_SIZE_CONTENT_BODY  = 12
LINE_GAP_MM       = 2.0

# Warna
TEXT_COLOR_NAVY = (0, 51, 102)
TEXT_COLOR_BODY = (0, 0, 0)

# --- Layout Cover ---
LEFT_MARGIN = 20
Y_POSITION  = 0.33

# --- Layout Content ---
CONTENT_LEFT_MARGIN   = 25
CONTENT_TOP_MARGIN    = 40
CONTENT_RIGHT_MARGIN  = 25
CONTENT_BOTTOM_MARGIN = 30

# --- Helper ---
page_w = 210
page_h = 297

def draw_left_text(pdf, text, x_mm, y_mm, font_size, color, bold=True):
    style = "B" if bold else ""
    pdf.set_font("OpenSans", style, font_size)
    pdf.set_text_color(*color)
    pdf.text(x_mm, y_mm, text)

def draw_centered_text(pdf, text, y_mm, font_size, color, bold=True):
    style = "B" if bold else ""
    pdf.set_font("OpenSans", style, font_size)
    pdf.set_text_color(*color)
    text_w = pdf.get_string_width(text)
    x = (page_w - text_w) / 2
    pdf.text(x, y_mm, text)

def get_bg_dimensions(img_path):
    img = Image.open(img_path)
    w_mm = 210.0
    scale = w_mm / img.width
    h_mm = img.height * scale
    return w_mm, h_mm

# ============================================================
#  BUILD PDF
# ============================================================
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)
pdf.set_margin(0)

# Register fonts
pdf.add_font("OpenSans", "", FONT_REG)
pdf.add_font("OpenSans", "B", FONT_BOLD)

# Background dimensions
cover_w, cover_h = get_bg_dimensions(COVER_BG)
content_w, content_h = get_bg_dimensions(CONTENT_BG)

# ============================================================
#  HALAMAN 1: COVER
# ============================================================
pdf.add_page()
pdf.image(COVER_BG, x=0, y=0, w=cover_w, h=cover_h)

y_start = page_h * Y_POSITION

draw_left_text(pdf, LEVEL_TEXT, LEFT_MARGIN,
               y_start - FONT_SIZE_LEVEL * 0.4 - LINE_GAP_MM,
               FONT_SIZE_LEVEL, TEXT_COLOR_NAVY)

draw_left_text(pdf, TITLE_LINE1, LEFT_MARGIN,
               y_start + FONT_SIZE_TITLE * 0.35,
               FONT_SIZE_TITLE, TEXT_COLOR_NAVY)

draw_left_text(pdf, TITLE_LINE2, LEFT_MARGIN,
               y_start + FONT_SIZE_TITLE * 0.35 + FONT_SIZE_TITLE * 0.45 + LINE_GAP_MM,
               FONT_SIZE_TITLE, TEXT_COLOR_NAVY)

y_bottom = page_h * 0.77
draw_left_text(pdf, BOTTOM_LINE1, LEFT_MARGIN, y_bottom, FONT_SIZE_BOTTOM, TEXT_COLOR_NAVY)
draw_left_text(pdf, BOTTOM_LINE2, LEFT_MARGIN,
               y_bottom + FONT_SIZE_BOTTOM * 0.5 + LINE_GAP_MM,
               FONT_SIZE_BOTTOM, TEXT_COLOR_NAVY)

# ============================================================
#  HALAMAN 2+: CONTENT (background content_handout.png)
# ============================================================
pdf.add_page()
pdf.image(CONTENT_BG, x=0, y=0, w=content_w, h=content_h)

y_pos = CONTENT_TOP_MARGIN
draw_left_text(pdf, CONTENT_TITLE, CONTENT_LEFT_MARGIN, y_pos,
               FONT_SIZE_CONTENT_TITLE, TEXT_COLOR_NAVY)

y_pos += 6
pdf.set_draw_color(*TEXT_COLOR_NAVY)
pdf.set_line_width(0.5)
pdf.line(CONTENT_LEFT_MARGIN, y_pos, page_w - CONTENT_RIGHT_MARGIN, y_pos)

y_pos += 10
pdf.set_font("OpenSans", "", FONT_SIZE_CONTENT_BODY)
pdf.set_text_color(*TEXT_COLOR_BODY)

content_w_mm = page_w - CONTENT_LEFT_MARGIN - CONTENT_RIGHT_MARGIN
pdf.set_xy(CONTENT_LEFT_MARGIN, y_pos)
pdf.multi_cell(content_w_mm, 7, CONTENT_BODY, align="L")

# --- Save ---
pdf.output(OUTPUT)
print(f"PDF saved: {OUTPUT}")
