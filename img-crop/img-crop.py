from PIL import Image
import os, sys

path = "./imgdir/"
dirs = os.listdir( path )

def cropimg():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            box = (199,0, 711, 512) # specify the crop box coordinates  
            cropped = im.crop(box)
            cropped.save(f + ' cropped.png', 'PNG', quality=100)

cropimg()
