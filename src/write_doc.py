import os, numpy as np
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

FONT = "Courier" #any monospaced font
FONT_SIZE = 5.0
LINE_SPACING = 1.0

#writes a text block to a .docx file
def writeDoc(text_arr, chroma, write_path, overwrite):
    '''
    params:
    -text_arr: TODO
    -chroma: TODO
    -write_path: TODO
    -overwrite: TODO
    '''

    document = Document()
    font = document.styles['Normal'].font
    font.name = FONT
    font.size = Pt(FONT_SIZE)

    p = document.add_paragraph()
    p_format = p.paragraph_format
    p_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_format.line_spacing = LINE_SPACING

    for line in text_arr:
        for char in line:
            p.text += char
        p.text += "\n"
 
    if overwrite and os.path.exists(write_path):
            os.remove(write_path)
    document.save(write_path)