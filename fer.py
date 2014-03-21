from ann import ANN

class FER():
	def __init__(self):
		#change 3rd param
		"""
		Usually you should start with a high learning rate and a low momentum. Then you decrease the learning rate over time
		and increase the momentum. The idea is to allow more exploration at the beginning of the learning and force convergence
		at the end of the learning. Usually you should look at the training error to set up your learning schedule: 
		if it got stuck, i.e. the error does not change, it is time to decrease your learning rate.
		"""
		self.neural = ANN(48*48,7,2,1200,10,0.5)

	def train(self,dataset):
		pass #train; writes the weight on the file; returns true if sucesss, false otherwise; returns time consumed

	def test(self,dataset):
		pass #returns the accuracy of the algorithm in floating point format; returns true if sucess, false otherwise; returns time consumed

	def predict(self,image):
		pass #classify a single image, returns the index of result (see main for the legend index:[0,7])