import sys
import os
import PIL.Image
from PIL import Image


img = Image.open("blur.png")
print(img.format, img.size, img.mode)



def greyScaleImg():
    img.show()

greyScaleImg()





'''
with Image.open("astro.jpg") as img:

    img.effect_noise((200,200),1)
    img.rotate(45).show()
'''