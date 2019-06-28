import sys

sys.path.append('../texterize')
from __init__ import create
from __init__ import createFromFile

TEST_PATH = "./test_files/"
TEST_IMG_PATH = "./test_img/"
FILE_TYPE = "HTML"

createFromFile(TEST_PATH + "test_1.txt", TEST_IMG_PATH + "test_1.jpg", output_file_type=FILE_TYPE)