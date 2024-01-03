import time
import os
import pickle
from main import ImageToAscii
#asciify a video
obj = ImageToAscii("/home/klepsydra/Desktop/videoplayback.mp4", 5)
obj.video_ascii()

def read():
	pickle_off = open ("output.txt", "rb")
	emp = pickle.load(pickle_off)
	for el in emp:
		print(el)
		time.sleep(0.02)
		os.system('clear')
read()

os.system('clear')
#asciify an image
obj = ImageToAscii("/home/klepsydra/Pictures/me/wedding_proposal.jpg", 4)
obj.image_ascii()