import numpy as np, math

def buildBlock(text, dimensions):
    '''
    params:
    -text: a string to be split into a block
    -dimensions: a tuple containing the numpy shape of the input image

    return:
    A tuple containing a 2D numpy array and an integer scaling factor
    '''

    assert len(dimension) == 3, "Chroma dimensions possess an invalid shape, aborting."

    for char in [" ", "\n", "\r"]:
        text = text.replace(char, "")
    TEXT_LENGTH = len(text)

    IMG_WIDTH, IMG_HEIGHT = dimensions #don't know if these are in right order (could be height then width)
    IMG_AREA = IMG_WIDTH * IMG_HEIGHT
    IMG_RATIO = IMG_WIDTH / IMG_HEIGHT

    SCALING_FACTOR = 1.0 / math.gcd(IMG_WIDTH, IMG_HEIGHT)
    #all this function is doing is getting the correct size for the RGB multiplier and returning that array

    '''
    dimensions is (300, 300, 3)
    img_area of 90000
    img_ratio of 1.0

    block with 150 words
    MORE CONCEPTUAL WORK HERE
    '''



    TEXT_LENGTH_SQRT = int(math.sqrt(TEXT_LENGTH))
    text_list = np.array(list(text))[:TEXT_LENGTH_SQRT ** 2]
    text_block = np.array(np.split(text_list, TEXT_LENGTH_SQRT))

    #need to check to make sure text doesn't wrap
    return text_block, scaling_factor