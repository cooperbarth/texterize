import os, numpy as np
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

FONT = "Courier"
FONT_SIZE = 5.0
LINE_SPACING = 1.0

def writeDoc(text_list, write_path, overwrite):
    if overwrite and os.path.exists(write_path):
        os.remove(write_path)

    document = Document()
    font = document.styles['Normal'].font
    font.name = FONT
    font.size = Pt(FONT_SIZE)

    p = document.add_paragraph()
    p_format = p.paragraph_format
    p_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_format.line_spacing = LINE_SPACING

    for line in text_list:
        for char in line:
            p.text += char
        p.text += "\n"
 
    document.save(write_path)