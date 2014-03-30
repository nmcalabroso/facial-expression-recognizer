import csv
import os

def load_train_set(filename):
	sub_dir = "resources/"
	my_file = open(os.path.join(sub_dir, filename), "rb")
	reader = csv.reader(my_file)

	header = None
	rownum = 0
	training_set = []
	test_set = []
	num_training = 0
	num_test = 0
	for row in reader:
		print 'data',rownum
		if rownum is 0:
			header = row
			print "header:",header
		else:
			#if rownum < 2:
			data = row #(emotion, pixel_list, usage)
			point = (int(data[0]),map(int,data[1].split()))
			if data[2] == "Training":
				#print "Loading training data:",i
				training_set.append(point)
				num_training += 1
			else:
				test_set.append(point)
				num_test += 1
		rownum += 1

	my_file.close()


	c = open("fann_train.data","w")
	c.write(str(num_training)+' '+str(48*48)+' '+str(7)) #28k 2304 7
	c.write('\n')
	for i in training_set:
		for j in i[1]:
			c.write(str(j)+' ')
		c.write('\n')
		if i[0] == 0:
			c.write('1 0 0 0 0 0 0')
		elif i[0] == 1:
			c.write('0 1 0 0 0 0 0')
		elif i[0] == 2:
			c.write('0 0 1 0 0 0 0')
		elif i[0] == 3:
			c.write('0 0 0 1 0 0 0')
		elif i[0] == 4:
			c.write('0 0 0 0 1 0 0')
		elif i[0] == 5:
			c.write('0 0 0 0 0 1 0')
		elif i[0] == 6:
			c.write('0 0 0 0 0 0 1')
		c.write('\n')
	c.close()

	c = open("fann_test.data","w")
	for i in test_set:
		for j in i[1]:
			c.write(str(j)+' ')
		c.write('\n')
		if i[0] == 0:
			c.write('1 0 0 0 0 0 0')
		elif i[0] == 1:
			c.write('0 1 0 0 0 0 0')
		elif i[0] == 2:
			c.write('0 0 1 0 0 0 0')
		elif i[0] == 3:
			c.write('0 0 0 1 0 0 0')
		elif i[0] == 4:
			c.write('0 0 0 0 1 0 0')
		elif i[0] == 5:
			c.write('0 0 0 0 0 1 0')
		elif i[0] == 6:
			c.write('0 0 0 0 0 0 1')
		c.write('\n')
	c.close()

filename = "fer2013.csv"#raw_input("Enter the name (relative to resources folder) of the csv file:")
training_set = load_train_set(filename)