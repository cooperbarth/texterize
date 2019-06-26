import numpy as np
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

FONT = "Courier"

def writeDoc(text_list, write_directory):
    document = Document()
    for line in text_list:
        p = document.add_paragraph()
        for char in line:
            p.text += char
        
        run = p.add_run()
        font = run.font
        font.name = FONT
        font.size = Pt(2)

        p_format = p.paragraph_format
        p_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_format.line_spacing = 1.0
    document.save(f"{write_directory}/texterize.docx")