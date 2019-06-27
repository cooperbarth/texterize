from PIL import Image
import math, numpy as np

def buildChroma(img_path, text_length):
    '''
    params:
    -img_path: the path to the image that the texterized image should be based on
    -text: A string containing the input text

    return:
    A tuple containing an N-by-N-by-3 numpy array containing the RGB values for each pixel of the given image and its shape
    '''
    try:
        img = Image.open(img_path)
        img_matrix = np.array(img.convert('RGB'))
    except:
        raise Exception(f"Could not open image {img_path}, aborting.")

    ORIG_WIDTH, ORIG_HEIGHT, _ = img_matrix.shape #don't know if these are in right order (could be height then width)
    if ORIG_WIDTH * ORIG_HEIGHT < text_length:
        return img_matrix

    SCALING_FACTOR = math.gcd(ORIG_WIDTH, ORIG_HEIGHT)
    img_width = int(ORIG_WIDTH / SCALING_FACTOR)
    img_height = int(ORIG_HEIGHT / SCALING_FACTOR)
    REDUCED_WIDTH = img_width
    REDUCED_HEIGHT = img_height
    while img_width * img_height < text_length:
        img_width += REDUCED_WIDTH
        img_height += REDUCED_HEIGHT

    img_compressed = img.thumbnail((img_width, img_height), Image.ANTIALIAS)   
    return np.array(img.convert('RGB'))

buildChroma("./../test/test_img/test_1.jpeg", 125)