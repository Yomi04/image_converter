import sys
import os
from PIL import Image 

# using sys module to grab the command line arguments
command_input = sys.argv[1:]

# this signifies that there will be two arguments 
image_folder,new_folder = command_input

# check if there is a new folder,if not create one.
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through the first argument(images folder), then convert the images inside of it to a png images.
for files in os.listdir(image_folder):

    img = Image.open(f'{image_folder}{files}')

    split_text = os.path.splitext(files)[0]

    # save them to the new folder 
    img.save(f'{new_folder}{split_text}.png','png')

print('you have successfully converted the files!')


