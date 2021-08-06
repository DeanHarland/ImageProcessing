import sys
import os
import PIL.Image
from PIL import Image
import fileLoader
import imageFileConverter
import imageChanger

# Opens explorer and when a file is chosen will save it as a new .something file
def ChangeFileToPng():
    chosen_file = fileLoader.loadSingleFile()
    imageFileConverter.changeSingleFileToPng(chosen_file)
def ChangeFileToJpg():
    chosen_file = fileLoader.loadSingleFile()
    imageFileConverter.changeSingleFileToJpg(chosen_file)

# Opens explorer and when multiple files are chosen it will save each as a new .something file
def ChangeMultipleFiletoPng():
    chosen_file = fileLoader.loadMultipleFiles()
    imageFileConverter.changeMultipleFilesToPng(chosen_file)

def ChangeMultipleFiletoJpg():
    chosen_file = fileLoader.loadMultipleFiles()
    imageFileConverter.changeMultipleFilesToJpg(chosen_file)


def imageTest():
    chosen_file = fileLoader.loadSingleFile()
    imageChanger.openImage(chosen_file)


imageTest()







#ChangeFileToPng()
#ChangeFileToJpg()
#ChangeMultipleFiletoPng()
#ChangeMultipleFiletoJpg()
