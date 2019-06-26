from docx import Document
import numpy as np
import sys

sys.path.append("./../src")
from build_block import buildBlock
from write_doc import writeDoc
from build_chroma import buildChroma
from coalesce import coalesce

OUTPUT_DIRECTORY = "../test/output_files/texterize.docx"

#main, input text as raw string
def create(text, img, write_path=OUTPUT_DIRECTORY, overwrite=True):
    '''
    params:
    -text: The text to be converted into an image, in string format
    -img: The path to the image that the texterized image should be based on
    -writePath: The filename/path to which the resulting document should be written
    -overwrite: Bool representing whether an existing doc with the given filepath should be overwritten
    '''
    assert isinstance(text, str), f"Expected input of type string, found {type(text)}."

    text_arr = buildBlock(text)
    coalesce(text_arr, buildChroma(img))
    writeDoc(text_arr, write_path, overwrite)
    
#Run create() using text in a .txt file, rather than as input
def createFromFile(filePath, img, writePath=OUTPUT_DIRECTORY, overwrite=True):
    '''
    params:
    -text: The text to be converted into an image, in string format
    -img: The path to the image that the texterized image should be based on
    -writePath: The filename/path to which the resulting document should be written
    -overwrite: Bool representing whether an existing doc with the given filepath should be overwritten
    '''
    try:
        f = open(filePath, "r")
        text = f.read()
        f.close() #expand function this way so the file closes even if an error in rendering occurs
    except:
        raise Exception(f"Could not open file {filePath}, aborting.")
    create(text, img, writePath, overwrite)