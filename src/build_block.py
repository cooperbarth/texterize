import numpy as np, math

def buildBlock(text, dimensions):
    '''
    params:
    -text: a string to be split into a block
    -dimensions: a tuple containing the numpy shape of the input image

    return:
    A tuple containing a 2D numpy array and an integer scaling factor
    '''

    assert len(dimensions) == 3, "Chroma dimensions possess an invalid shape, aborting."



#ksdjbnfgklsd

    TEXT_LENGTH_SQRT = int(math.sqrt(TEXT_LENGTH))
    text_list = np.array(list(text))[:TEXT_LENGTH_SQRT ** 2]
    text_block = np.array(np.split(text_list, TEXT_LENGTH_SQRT))

    #need to check to make sure text doesn't wrap
    return text_block, scaling_factor