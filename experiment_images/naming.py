from PIL import Image, ImageOps
import PIL
import os
import glob
import shutil

# Get the directory of the current Python file
#current_dir = os.path.dirname(os.path.abspath('naming.py'))
# Set the working directory to the directory of the Python file
dir = os.getcwd()
os.chdir(dir+ '\\Cave art images')

# 1. Create a list of all the folders in the directory
directory = os.getcwd()
items = os.listdir(directory)
folders = [item for item in items if item != 'naming.py']
#set end directory
# Define the directory path where you want to save the object
end_dir = dir + '\\experiment_images'

# Check if the directory exists, if not, create it
if not os.path.exists(end_dir):
    os.makedirs(end_dir)

# 3. Extract all of the images:
#repeat for each folder
for folder in folders:
    #change the working directory
    os.chdir(directory + '\\' + folder)
    #get the images
    list_dir = os.listdir(os.getcwd())
    images = [file for file in list_dir if file.endswith(('jpg', 'png'))]
    #print(images)

    #for all images in the folder
    for img in images:
         #copy original
        shutil.copy(img, end_dir)

        #flip images
        #open image
        im = Image.open(img)
        #flip image
        im = ImageOps.mirror(im)
        #new name
        if img.endswith('l.jpg'):
            new_img = img.replace('l', 'r')
        else:
            new_img = img.replace('r', 'l')

        #save transposed image with same quality as original
        im.save(end_dir + '\\' + new_img, quality=100,dpi=(300,300))
        im.close()
    
    #change the working directory
    os.chdir(directory)
print(os.listdir(end_dir))