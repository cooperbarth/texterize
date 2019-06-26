import numpy as np
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.text.parfmt import ParagraphFormat

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

        #p_format = ParagraphFormat()
        #p_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        #p.paragraph_format = p_format
    document.save("texterize.docx")