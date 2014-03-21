from __future__ import division
from ann import ANN
import time

#Facial Expression Recognizer
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
		start = time.clock()
		weights = self.neural.train(dataset)
		result = True
		timex = 0
		
		weight_f = open("weights.txt","w")
		for layer in weights:
  			for e in layer:
  				weight_f.write(str(e))
  			weight_f.write("\n")
  		weight_f.close()

  		end = time.clock()
  		timex = end - start
  		#train; writes the weight on the file; returns true if sucesss, false otherwise; returns time consumed
		return result,timex

	def test(self,dataset):
		start = time.clock()
		correct = 0
		accuracy = 0.0
		result = True
		timex = 0

		for row in dataset:
			prediction = self.predict(row[1])
			if prediction == row[0]:
				correct+=1

		accuracy = correct/len(dataset)

		end = time.clock()
  		timex = end - start
		#returns the accuracy of the algorithm in floating point format; returns true if sucess, false otherwise; returns time consumed
		return accuracy,result,timex

	def predict(self,image):
		#classify a single image, returns the index of result (see main for the legend index:[0,7])
		return self.neural.classify(image)
