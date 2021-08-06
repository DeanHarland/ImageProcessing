import sys
import os
import PIL.Image
from PIL import Image
import random

def openImage(file):
    img = Image.open(file)
    print(img.format, img.size, img.mode)
    img.show()
def RotateBoxinImg(file):
    img = Image.open(file)
    print(img.format, img.size, img.mode)
    box = (100, 100, 400, 400)
    region = img.crop(box)

    region = region.transpose(Image.ROTATE_180)
    img.paste(region,box)

    #region.show()
    img.show()




#def greyScaleImg():
 #   img.show()

#greyScaleImg()


