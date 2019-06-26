import numpy as np
import sys, os

sys.path.append("./../src")
from write_doc import writeDoc
from build_block import buildBlock

OUTPUT_DIRECTORY = "../test/output_files/texterize.docx"
TEST_PATH = "../test/test_files/"

#DESCRIPTION HERE
def create(text, img, writePath=OUTPUT_DIRECTORY, overwrite=True):
    '''
    params:
    -text: The text to be converted into an image, in string format
    -img: The path to the image that the texterized image should be based on
    -writePath: The filename/path to which the resulting document should be written
    '''
    assert isinstance(text, str), f"Expected input of type string, found {type(text)}."

    if overwrite and os.path.exists(writePath):
        os.remove(writePath)

    text_block = buildBlock(text)
    writeDoc(text_block, writePath)
    
#DESCRIPTION HERE
def createFromFile(filePath, img, writePath="", overwrite=True):
    '''
    params:
    -text: TODO
    -img: TODO
    -writePath: TODO
    '''
    f = open(filePath, "r")
    text = f.read()
    f.close() #expand function this way so the file closes even if an error in rendering occurs
    create(text, img, writePath, overwrite)

#TODO: Remove this; just for testing
createFromFile(TEST_PATH + "test_1.txt", "", OUTPUT_DIRECTORY)
