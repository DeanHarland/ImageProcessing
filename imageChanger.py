import sys
import os
import PIL.Image
from PIL import Image


img = Image.open("blur.png")
print(img.format, img.size, img.mode)



def greyScaleImg():
    img.show()

greyScaleImg()


