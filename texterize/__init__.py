import numpy as np, math, sys

sys.path.append("../src")
from write_doc import writeDoc

#DESCRIPTION HERE
def create(text, img, writePath=""):
    '''
    params:
    -text: The text to be converted into an image, in string format
    -img: The path to the image that the texterized image should be based on
    -writePath: The filename/path to which the resulting document should be written
    '''
    assert isinstance(text, str), f"Expected input of type string, found {type(text)}."

    TEXT_LENGTH = len(text)
    TEXT_LENGTH_SQRT = int(math.sqrt(TEXT_LENGTH))
    text_list = np.asarray(list(text))[:TEXT_LENGTH_SQRT ** 2]
    text_block = np.split(text_list, TEXT_LENGTH_SQRT)
    #need to make this ratio approximately equal to the picture aspect ratio, not just a square.

    writeDoc(text_block)
    
#DESCRIPTION HERE
def createFromFile(filePath, img, writePath=""):
    '''
    params:
    -text: TODO
    -img: TODO
    -writePath: TODO
    '''
    f = open(filePath, "r")
    text = f.read()
    f.close() #expand function this way so the file closes even if an error in rendering occurs
    create(text, img, writePath)

create("Hello, this is Cooper, and fskdjgnskjgksdfl", "")
