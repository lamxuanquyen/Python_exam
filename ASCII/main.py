#https://github.com/AJITH-klepsydra/other_repositories/blob/main/Image_To_Ascii_Art/main.py
import cv2
import numpy as np
import pickle

class ImageToAscii:
	def __init__(self,path,re_val):
		self.path=path
		self.frames_list=[]
		self.ASCII = ['@','#','S','%','?','*','+',';',':',',']
		self.resize_fact = re_val
	def load_image(self):
		image=cv2.imread(self.path)
		image = cv2.resize(image,(image.shape[1]//self.resize_fact,image.shape[0]//self.resize_fact))
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		return image
	def image_ascii(self,*args,**kwargs):
		try:
			if args:
				img = args[0]
			else:
				img = self.load_image()
			rows,cols = img.shape
			frame="\n"
			for i in range(rows):
				for j in range(cols):
					im_val =img.item(i,j)
					frame += self.ASCII[im_val//30]
				frame +="\n"
	
			print(frame)
			return frame	
		except Exception as e:
			print(e)
	def video_ascii(self):
		self.video=cv2.VideoCapture(self.path)
		while(True):
			try:
				_,image = self.video.read()
				image = cv2.resize(image,(image.shape[1]//self.resize_fact,image.shape[0]//self.resize_fact))
				image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
				self.frames_list.append(self.image_ascii(image))
			except Exception as e:
				print(e)
				break
		with open("output.txt","wb") as f:
			pickle.dump(self.frames_list, f)