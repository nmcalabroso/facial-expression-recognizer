from __future__ import division
from fer import FER
from PIL import Image
import csv
import os

expressions = ['angry','disgust','fear','happy','sad','surprise','neutral'] #seven facial expressions

def load_data_set(filename):
	sub_dir = "resources/"
	my_file = open(os.path.join(sub_dir, filename), "rb")
	reader = csv.reader(my_file)

	header = None
	rownum = 0
	training_set = []
	test_set = []

	i = 0

	for row in reader:
		if rownum is 0:
			header = row
			print "header:",header
		else:
			if i<10000:
				data = row #(emotion, pixel_list, usage)
				point = (int(data[0]),map(int,data[1].split()))
				if data[2] == "Training":
					print "Loading training data:",i
					training_set.append(point)
				else:
					test_set.append(point)
			i+=1
		rownum += 1

	my_file.close()
	return training_set,test_set #returns a list or format of the training set from the csv file

def load_image(path):
	img = Image.open(path)
	img = img.convert("L")
	pixels = img.load()
	print "Image size:",img.size

	pixel_list = []
	for i in range(48):
		for j in range(48):
			pixel_list.append(pixels[i,j])
	
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
			filename = "fer2013.csv"#raw_input("Enter the name (relative to resources folder) of the csv file:")
			training_set,test_set = load_data_set(filename)
			#format of each element in each list is (emotion,pixel_list)
			train = recognizer.train(training_set) 
			if train[0]:
				print "Training successful!"
				print "Time:",train[1]
			else:
				print "Training failed. Program will terminate."
				break

			#uncomment to test
			"""test = recognizer.test(test_set)
			if test[1]:
				print "Testing complete!"
				print "Accuracy:",test[0]
				print "Time:",test[2]
			else:
				print "Testing failed!"
				break"""
			break
		elif a is 2: #to test
			for i in range(len(expressions)):
				print "["+str(i)+"]",expressions[i]
			img_path = raw_input("Please enter the name of the image:")
			image_pixel = load_image(img_path)
			result = recognizer.predict(image_pixel)

			print "Your image:",img_path,"is:"
			print "["+str(result)+"]",expressions[result]

			break
		else:
			print "Please enter a correct input."

if __name__ == "__main__":
	main()