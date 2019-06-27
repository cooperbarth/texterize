import sys

sys.path.append('../texterize')
from __init__ import create
from __init__ import createFromFile

TEST_PATH = "./test_files/"
TEST_IMG_PATH = "./test_img/"

createFromFile(TEST_PATH + "test_1.txt", TEST_IMG_PATH + "cat.jpeg")