from __future__ import division
from fer import FER
from PIL import Image
import csv
import numpy

expressions = ['angry','disgust','fear','happy','sad','surprise','neutral'] #seven facial expressions

def load_training_set(path):
	pass #returns a list or format of the training set from the csv file

def load_image(path):
	img = Image.open(path)
	img = img.convert("L")
	pixels = img.load()
	print "Image size:",img.size

	pixel_list = []
	for i in range(48):
		for j in range(48):
			pixel_list.append(pixels[i,j])
	
	"""
	#trying to check if the acquired pixel_list is the same as the original
	new = Image.new(mode = "L", size = (48,48))
	x = new.load()
	k = 0
	for i in range(48):
		for j in range(48):
			x[i,j] = pixel_list[k]
			k+=1
	new.save("new.png")
	"""

	return pixel_list #returns a list of pixels with size 2304(or 48*48)

def main():
	recognizer = FER()
	a = 0

	print "Welcome to Facial Expression Recognizer!"

	while True:
		print "[1] Train"
		print "[2] Test"
		a = int(raw_input("You want to:"))

		if a is 1:#to train
			training_path = raw_input("Enter the path of the csv file:")
			training_set = load_training_set(training_path)
			if recognizer.train(training_set):
				print "Training successful!"
			else:
				print "Training failed. Program will terminate."
			break
		elif a is 2: #to test
			for i in range(len(expressions)):
				print "["+str(i)+"]",expressions[i]
			img_path = raw_input("Please enter the path of the image:")
			image_pixel = load_image(img_path)
			recognizer.predict(image_pixel)
			break
		else:
			print "Please enter a correct input."

if __name__ == "__main__":
	main()