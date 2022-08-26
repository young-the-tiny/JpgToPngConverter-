import sys
import os
from PIL import Image
#grab second and first arguments
#check if new folder exists? if not create one

#loop through image folder 
#convert to png
#save in new folder
print(str(sys.argv))
image_folder = sys.argv[1]
output_folder = sys.argv[2]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(image_folder):
    img = Image.open(f'./{image_folder}/{filename}')
    clean_name = os.path.splitext(filename)[0] #access the filename, not the file tail
    img.save(f'./{output_folder}/{clean_name}.png','png')
    print('All good!!')
#readme
# Before running the script enter this in terminal: ""python JpgToPngConverter.py imageFolder new"" then hit Enter!
