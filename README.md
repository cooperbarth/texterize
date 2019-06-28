# texterize
Making pictures worth a thousand words (or so).

`texterize` is a package that uses pixel aggregation to create ASCII art out of blocks of text.

{Insert Images Here}

## Installation:
`python3 -m pip install texterize`
*Note: texterize is incompatible with Python 2.X.*

## Usage:
`Texterize` is used to create colorized ASCII art out of a given image and selection of text. Upon feeding in an image and a string of text (either through a text file (via `createFromFile()`) or through raw input via (`create()`), an image will be generated in the desired format (either HTML or MS Word).

```
import texterize

TEXT_FILE_PATH = "./path/to/text/FILE_NAME.txt"
IMG_FILE_PATH = "./path/to/img/FILE_NAME.txt"

texterized_img_path = texterize.createFromFile(TEXT_FILE_PATH, IMG_FILE_PATH, write_path="./my_texterized_image")
```