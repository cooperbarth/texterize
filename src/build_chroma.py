from matplotlib.pyplot import imread
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
        img_matrix = imread(img_path)
    except:
        raise Exception(f"Could not open image {img_path}, aborting.")

    ORIG_WIDTH, ORIG_HEIGHT, _ = img_matrix.shape #don't know if these are in right order (could be height then width)
    SCALING_FACTOR = math.gcd(ORIG_WIDTH, ORIG_HEIGHT)

    img_width = int(ORIG_WIDTH / SCALING_FACTOR)
    img_height = int(ORIG_HEIGHT / SCALING_FACTOR)
    REDUCED_WIDTH = img_width
    REDUCED_HEIGHT = img_height

    while img_width * img_height < text_length:
        img_width += REDUCED_WIDTH
        img_height += REDUCED_HEIGHT

    chroma = np.zeros((img_width, img_height, 3))
    CHUNK_WIDTH = ORIG_WIDTH - img_width + 1
    CHUNK_HEIGHT = ORIG_HEIGHT - img_height + 1

    print(CHUNK_HEIGHT * CHUNK_WIDTH * (img_height - 1) * (img_width - 1))

    for i in range(img_matrix.shape[0] - CHUNK_WIDTH):
        for j in range(img_matrix.shape[1] - CHUNK_WIDTH):
            chunk = img_matrix[i:i+CHUNK_HEIGHT][j:j+CHUNK_WIDTH]
            sum_RGB = [0, 0, 0]
            #need to make this more efficient
            #runtime is O(CHUNK_WIDTH * CHUNK_HEIGHT * (img_width - 1) * (img_height - 1))
            #that's 305_532_864 million calls for this example

buildChroma("./../test/test_img/test_1.jpg", 125)