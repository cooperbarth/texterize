import sys

sys.path.append('../texterize')
from __init__ import create
from __init__ import createFromFile

TEST_PATH = "./test_files/test_1.txt"
TEST_IMG_PATH = "./test_img/test_1.jpg"
FILE_TYPE = "Word"

createFromFile(TEST_PATH, TEST_IMG_PATH, output_file_type=FILE_TYPE)