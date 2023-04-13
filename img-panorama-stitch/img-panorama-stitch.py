#this script join multiple images to create a panorama image
import cv2
image_paths=['1.jpg','2.jpg','3.jpg'] #change this with filenames of the pictures you want to stitch together
# initialized a list of images
imgs = []

for i in range(len(image_paths)):
	imgs.append(cv2.imread(image_paths[i]))
	#imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
	# this is optional if your input images isn't too large
# showing the original pictures
#cv2.imshow('1',imgs[0])
#cv2.imshow('2',imgs[1])
#cv2.imshow('3',imgs[2])

stitchy=cv2.Stitcher.create()
(dummy,output)=stitchy.stitch(imgs)

if dummy != cv2.STITCHER_OK:
# checking if the stitching procedure is successful
# .stitch() function returns a true value if stitching is
# done successfully
	print("stitching ain't successful")
else:
	print('Your Panorama is ready!!!')

# final output
cv2.imwrite("output.jpg",output)
