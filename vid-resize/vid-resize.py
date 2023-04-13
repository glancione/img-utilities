import moviepy.editor as mp
import os, sys

path = "./"
dirs = os.listdir( path )

def resize_vid():
	for item in dirs:
		if os.path.isfile(path+item):
			clip = mp.VideoFileClip(path+item)
			f, e = os.path.splitext(path+item)
			clip_resized = clip.resize(height=1080)
			clip_resized.write_videofile(f + " resized.mp4")

resize_vid()
