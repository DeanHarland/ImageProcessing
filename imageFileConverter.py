import os, sys
from pathlib import Path
from PIL import Image

# Get current working directory
main_path = os.getcwd()

# Manually set file paths
image_path = f"{main_path}/Pokedex/"
new_path = f"{main_path}/Output/"
Path(new_path).mkdir(parents=True, exist_ok=True)


# Iterate through each file and save it as .png
def changeAllFilesToPng():
    for filename in os.listdir(image_path):
        clean_name = os.path.splitext(filename)[0]
        print(clean_name)
        img = Image.open(f'{image_path}{filename}')
        img.save(f'{new_path}/{clean_name}.png', 'png')
        print('all done!')


# Changes a single file to a png and saves it in the output folder.
def changeSingleFileToPng(file):
    img = Image.open(file)
    file_name = os.path.basename(file)
    clean_name = os.path.splitext(file_name)[0]
    img.save(f'{new_path}/{clean_name}.png', 'png')
    print('Finished changing file to png')


# Changes multiple files to a png and saves it in the output folder.
def changeMultipleFilesToPng(files):
    for item in files:
        img = Image.open(item)
        file_name = os.path.basename(item)
        clean_name = os.path.splitext(file_name)[0]
        img.save(f'{new_path}/{clean_name}.png', 'png')
    print('Finished changing files to png')


# Changes a single file to a Jpeg and saves it in the output folder.
def changeSingleFileToJpg(file):
    img = Image.open(file)
    file_name = os.path.basename(file)
    clean_name = os.path.splitext(file_name)[0]
    img.save(f'{new_path}/{clean_name}.jpg', 'JPEG')
    print('Finished changing file to jpg')


# Changes multiple files to a Jpeg and saves it in the output folder.
def changeMultipleFilesToJpg(files):
    for item in files:
        img = Image.open(item)
        file_name = os.path.basename(item)
        clean_name = os.path.splitext(file_name)[0]
        img.save(f'{new_path}/{clean_name}.jpg', 'JPEG')
    print('Finished changing files to jpg')


'''
# Changes a single file to a png and saves it in the same folder
def changeSingleFileToPng(file):
    img = Image.open(file)
    clean_name = os.path.splitext(file)[0]
    img.save(f'{clean_name}.png', 'png')
    print('Finished changing file to png')
'''

'''
def changeSingleFileToPng(file):
    img = Image.open(file)
    img.save()
    #img.save(f'{new_path}/{file}', 'png')
    print('Finished changing file to png')

'''
