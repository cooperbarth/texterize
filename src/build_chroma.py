from matplotlib.pyplot import imread

def buildChroma(img):
    '''
    params:
    -img: the path to the image that the texterized image should be based on

    return:
    An N-by-N-by-3 numpy array containing the RGB values for each pixel of the given image
    '''
    try:
        return imread(img)
    except:
        raise Exception("Invalid Image Path")