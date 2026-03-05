import os
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# ====== CONFIG ======
VAULT_PATH = "/home/user/Public/gh/second-brain-web/Frontend"
OUTPUT_PATH = "frontend-second-brain.pdf"  # базовое имя файла
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# ====================

# функция для добавления текущей даты
def get_timestamped_filename(base_path):
    now = datetime.now()
    timestamp = now.strftime("_%Y-%m-%d_%H-%M-%S")
    name, ext = os.path.splitext(base_path)
    return f"{name}{timestamp}{ext}"

def get_all_markdown_files(base_path):
    md_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                md_files.append(full_path)
    return sorted(md_files)

def build_pdf(vault_path, output_path):
    pdfmetrics.registerFont(TTFont("DejaVuSans", FONT_PATH))
    output_path = get_timestamped_filename(output_path)  # добавляем дату

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading2'],
        fontName="DejaVuSans",
        textColor=colors.darkblue,
        fontSize=12,
        spaceAfter=6
    )
    text_style = ParagraphStyle(
        'TextStyle',
        parent=styles['Normal'],
        fontName="DejaVuSans",
        fontSize=10,
        leading=14
    )

    md_files = get_all_markdown_files(vault_path)

    for file_path in md_files:
        relative_path = os.path.relpath(file_path, vault_path)
        elements.append(Paragraph(f"FILE: {relative_path}", header_style))
        elements.append(Spacer(1, 0.2 * inch))

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            content = f"[ERROR READING FILE: {e}]"

        for line in content.split("\n"):
            elements.append(Paragraph(line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"), text_style))

        elements.append(Spacer(1, 0.5 * inch))

    doc.build(elements)
    print(f"PDF создан: {output_path}")


if __name__ == "__main__":
    build_pdf(VAULT_PATH, OUTPUT_PATH)