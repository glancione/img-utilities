from PIL import Image
import numpy as np
#open desired image
im = Image.open('./test3.png')
#find its width & height
w,h = im.size
#find NEW dimensions from user-defined number (50% for example)
new_w = w * 0.150
new_h = h * 0.150
#round to nearest whole number and convert from float to int
new_w = np.round(new_w)
new_w = int(new_w)
new_h = np.round(new_h)
new_h = int(new_h)
#downsample image to these new dimensions
down_sampled = im.resize((new_w, new_h))
#upsample back to original size (using "4" to signify bicubic)
up_sampled = down_sampled.resize((w, h), resample = 4)
#save the image
up_sampled.save('./test3_out.png')