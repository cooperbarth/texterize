import numpy as np, math

def buildBlock(text):
    TEXT_LENGTH = len(text)
    TEXT_LENGTH_SQRT = int(math.sqrt(TEXT_LENGTH))
    text_list = np.asarray(list(text))[:TEXT_LENGTH_SQRT ** 2]
    text_block = np.split(text_list, TEXT_LENGTH_SQRT) #need to make this ratio approximately equal to the picture aspect ratio, not just a square.

    return text_block