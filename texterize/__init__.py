from docx import Document
import numpy as np
import sys

sys.path.append("./../src")
from filter_text import filterText
from build_chroma import buildChroma
from build_block import buildBlock
from write_doc import writeDoc

OUTPUT_DIRECTORY = "../test/output_files/texterize.docx" #this should be changed to "./texterize.docx" upon release

#main, input text as raw string
def create(text, img_path, write_path=OUTPUT_DIRECTORY, overwrite=True):
    '''
    params:
    -text: The text to be converted into an image, in string format
    -img_path: The path to the image that the texterized image should be based on
    -writePath: The filename/path to which the resulting document should be written
    -overwrite: Bool representing whether an existing doc with the given filepath should be overwritten
    '''
    assert isinstance(text, str), f"Expected input of type string, found {type(text)}."

    text = filterText(text)
    chroma, chroma_shape = buildChroma(img_path, len(text))
    text_arr = buildBlock(text, chroma_shape)
    writeDoc(text_arr, chroma, write_path, overwrite)
    
#Run create() using text in a .txt file, rather than as input
def createFromFile(file_path, img_path, write_path=OUTPUT_DIRECTORY, overwrite=True):
    '''
    params:
    -file_path: The path to the .txt file to pull the text from
    -img_path: The path to the image that the texterized image should be based on
    -write_path: The filename/path to which the resulting document should be written
    -overwrite: Bool representing whether an existing doc with the given filepath should be overwritten
    '''
    try:
        f = open(file_path, "r")
        text = f.read()
        f.close() #expand function this way so the file closes even if an error in rendering occurs
    except:
        raise Exception(f"Could not open file {file_path}, aborting.")
    create(text, img_path, write_path, overwrite)