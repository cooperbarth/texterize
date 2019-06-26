from matplotlib.pyplot import imread

def buildChroma(img_path):
    '''
    params:
    -img_path: the path to the image that the texterized image should be based on

    return:
    An tuple containing an N-by-N-by-3 numpy array containing the RGB values for each pixel of the given image and its shape
    '''
    try:
        chroma = imread(img_path)
        return chroma, chroma.shape
    except:
        raise Exception(f"Could not open image {img_path}, aborting.")