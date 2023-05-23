from PIL import Image, ImageDraw, ImageFont
import os
 
def text_on_img(filename='01.png', text="Hello", size=12, color=(255,255,0), bg='red'):
	"Draw a text on an Image, saves it, show it"
	fnt = ImageFont.truetype('arial.ttf', size)
	# create image
	image = Image.new(mode = "RGB", size = (int(size/4)*len(3*text),size+50), color = bg)
	draw = ImageDraw.Draw(image)
	# draw text
	draw.text((int(size/10)*len(text),10), text, font=fnt, fill=(200,200,200))
	# save file
	image.save(filename)
	# show file
	#os.system(filename)
 
x = "0000"

for i in range(1000):
   y = "glanc" + x
   text_on_img(filename='./' + x + '.png',text=y, size=300, bg='black', color = (255, 0, 0))
   x = str(int(x) + 1).zfill(len(x))