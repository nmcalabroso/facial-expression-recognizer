from ann import ANN

class FER():
	def __init__(self):
		self.neural = ANN()

	def train(self,dataset):
		pass #train; writes the weight on the file; returns true if sucesss, false otherwise

	def test(self,dataset):
		pass #returns the accuracy of the algorithm in floating point format

	def predict(self,image):
		pass #classify a single image, returns the index of result (see main for the legend index:[0,7])