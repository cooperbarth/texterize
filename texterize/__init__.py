from docx import Document
import numpy as np

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
    text_list = np.fromstring(text)[:TEXT_LENGTH_SQRT ** 2]
    np.split(text_list, TEXT_LENGTH_SQRT) #We now have N rows of N characters
    #need to make this ratio approximately equal to the picture aspect ratio, not just a square.
    
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