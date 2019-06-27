import os, numpy as np
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor

FONT = "Courier" #any monospaced font
FONT_SIZE = 5.0
LINE_SPACING = 1.0

#writes a text block to a .docx file
def writeDoc(text_arr, chroma, write_path, overwrite):
    '''
    params:
    -text_arr: A 2-D numpy array of the text to write to the document
    -chroma: A 3-D numpy array containing the RGB values to assign to each character of text
    -write_path: The path to write the output file to
    -overwrite: A Boolean representing whether or not to overwrite an existing .doxcx file if found.
    '''

    document = Document()
    font = document.styles['Normal'].font
    font.name = FONT
    font.size = Pt(FONT_SIZE)

    p = document.add_paragraph()
    p_format = p.paragraph_format
    p_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_format.line_spacing = LINE_SPACING

    for i in range(text_arr.shape[0]):
        for j in range(text_arr.shape[1]):
            c = p.add_run(text_arr[i][j])
            R, G, B = chroma[i][j]
            c.font.color.rgb = RGBColor(int(R), int(G), int(B))
        _ = p.add_run("\n")
 
    if overwrite and os.path.exists(write_path):
        os.remove(write_path)
    document.save(write_path)