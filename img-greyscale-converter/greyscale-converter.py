# this slice of code convert all the images in mypath into greyscale images

from PIL import Image, ImageOps

from os import listdir
mypath = './tiles/'
onlyfiles = [f for f in listdir(mypath)]

for j in onlyfiles:
	out_file = './tiles_bw/bw' + str(j)
	og_image = Image.open(mypath + j)
	#og_image.show()
	# applying grayscale method
	gray_image = ImageOps.grayscale(og_image)
	#gray_image.show()
	gray_image.save(out_file)