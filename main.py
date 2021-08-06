import sys
import os
import PIL.Image
from PIL import Image

import fileLoader
import imageFileConverter

# First attempt at changing a file, opens explorer, which ever file is selected will save it as a new .png file
def ChangeFile():
    chosen_file = fileLoader.loadSingleFile()
    imageFileConverter.changeSingleFileToPng(chosen_file)



ChangeFile()