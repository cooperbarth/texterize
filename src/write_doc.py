import numpy as np
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

FONT = "Courier"

def writeDoc(text_list):
    document = Document()
    for line in text_list:
        p = document.add_paragraph()
        for char in line:
            p.text += char
        
        run = p.add_run()
        font = run.font
        font.name = FONT
        font.size = Pt(12)

        p_format = p.paragraph_format
        p_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    document.save("texterize.docx")