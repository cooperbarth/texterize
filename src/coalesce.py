import numpy as np

#forms a 3-D numpy array representing the RGB values to apply to each character in the output file
def coalesce(block, chroma):
    '''
    params:
    -block: A 2-D numpy array representing the rows of text to be printed
    -chroma: A 3-D numpy array containing the RGB values for each pixel of the input image

    return:
    An MxNx3 numpy array, where MxN is the shape of the block parameter, containing the aggregate RGB values for each character
    '''

    

    return