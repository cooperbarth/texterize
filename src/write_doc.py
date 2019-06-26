import numpy as np
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

FONT = "Courier"
FONT_SIZE = 5.0
LINE_SPACING = 1.0

def writeDoc(text_list, write_path):
    document = Document()
    font = document.styles['Normal'].font
    font.name = FONT
    font.size = Pt(FONT_SIZE)

    for line in text_list:
        p = document.add_paragraph()
        for char in line:
            p.text += char

        p_format = p.paragraph_format
        p_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_format.line_spacing = LINE_SPACING
    document.save(write_path)