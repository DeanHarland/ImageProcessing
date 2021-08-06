import sys
import os
from PIL import Image

# Get current working directory

os.chdir('C:/Users/Dean/Documents/PortfolioProjects/ImageProcessing/Pokedex')
main_path = os.getcwd()
print(main_path)
# Grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]
print(main_path, path, directory)


image_path = os.path.join(main_path, path, '')
new_path = os.path.join(main_path, directory, '')

# Check if new exists, if not create it
if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{image_path}{filename}')
    # added the / in case user doesn't enter it. You may want to check for this and add or remover it.
    img.save(f'{new_path}/{clean_name}.png', 'png')
    print('all done!')
