from pyfann import libfann

class classifier():

	def __init__(self):
		self.fann = libfann.neural_net()

	def analyze(self, input_img):	
		self.fann.create_from_file("fann_result_train92.net")

		output = self.fann.run(input_img)
		print output
		if output.index(max(output)) == 0:
			return True
		return False