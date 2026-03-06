import os
import platform
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# ====== AUTO CONFIG BY OS ======

SYSTEM = platform.system()

if SYSTEM == "Windows":
    VAULT_PATH = "./Frontend"
    FONT_PATH = r"C:\Windows\Fonts\arial.ttf"
    FONT_NAME = "ArialCyr"

elif SYSTEM == "Linux":
    VAULT_PATH = "/home/user/Public/gh/second-brain-web/Frontend"
    FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    FONT_NAME = "DejaVuSans"

else:
    raise Exception(f"Unsupported OS: {SYSTEM}")

OUTPUT_PATH = "frontend-second-brain.pdf"

# ===============================


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
                md_files.append(os.path.join(root, file))

    return sorted(md_files)


def build_pdf(vault_path, output_path):

    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))

    output_path = get_timestamped_filename(output_path)

    doc = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []

    styles = getSampleStyleSheet()

    header_style = ParagraphStyle(
        "HeaderStyle",
        parent=styles["Heading2"],
        fontName=FONT_NAME,
        textColor=colors.darkblue,
        fontSize=12,
        spaceAfter=6,
    )

    text_style = ParagraphStyle(
        "TextStyle",
        parent=styles["Normal"],
        fontName=FONT_NAME,
        fontSize=10,
        leading=14,
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

            safe_line = (
                line.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )

            if safe_line.strip() == "":
                safe_line = "&nbsp;"

            elements.append(Paragraph(safe_line, text_style))

        elements.append(Spacer(1, 0.5 * inch))

    doc.build(elements)

    print(f"OS detected: {SYSTEM}")
    print(f"Font used: {FONT_NAME}")
    print(f"PDF created: {output_path}")


if __name__ == "__main__":
    build_pdf(VAULT_PATH, OUTPUT_PATH)