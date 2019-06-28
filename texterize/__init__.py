from docx import Document
import numpy as np
import sys

sys.path.append("./../src")
from filter_text import filterText
from build_chroma import buildChroma
from build_block import buildBlock
from write_file import write

OUTPUT_DIRECTORY = "./texterized_image"
SUPPORTED_FILE_TYPES = ["HTML", "Word"]

#main, input text as raw string
def create(text, img_path, output_file_type="HTML", write_path=OUTPUT_DIRECTORY, overwrite=True):
    '''
    params:
    -text: The text to be converted into an image, in string format
    -img_path: The path to the image that the texterized image should be based on
    -writePath: The filename/path to which the resulting document should be written
    -overwrite: Bool representing whether an existing doc with the given filepath should be overwritten
    '''
    assert isinstance(text, str), f"Expected input of type string, found {type(text)}."
    assert output_file_type in SUPPORTED_FILE_TYPES, (f"Output file type {output_file_type} not supported.")

    text = filterText(text)
    chroma, chroma_shape = buildChroma(img_path, len(text))
    text_arr = buildBlock(text, chroma_shape)
    write(text_arr, chroma, output_file_type, write_path, overwrite)
    
#Run create() using text in a .txt file, rather than as input
def createFromFile(file_path, img_path, output_file_type="HTML", write_path=OUTPUT_DIRECTORY, overwrite=True):
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
        f.close()
    except:
        raise Exception(f"Could not open file {file_path}, aborting.")
    create(text, img_path, output_file_type, write_path, overwrite)