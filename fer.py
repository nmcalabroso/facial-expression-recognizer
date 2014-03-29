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
		print "FER Train"
		start = time.clock()
		weights = self.neural.train(dataset,epoch=3)
		result = True
		timex = 0
		
		weight_f = open("weights.txt","w")
		#print "len(weights)",len(weights)
		#print "len(weights[0])",len(weights[0])
		#print "weights[0][1]",weights[0][1]
		
		for layer in range(len(weights)):
			weight_f.write("Layer "+str(layer)+"\n")
  			for e in range(len(weights[layer])):
  				weight_f.write("Node "+str(e)+"\n")
  				for f in range(len(weights[layer][e])):
  					weight_f.write(str(weights[layer][e][f]) + " ")
  				weight_f.write("\n")
  		
  		weight_f.close()

  		end = time.clock()
  		timex = end - start
  		#train; writes the weight on the file; returns true if sucesss, false otherwise; returns time consumed
		return result,timex

	def test(self,dataset,weights):
		start = time.clock()
		correct = 0
		accuracy = 0.0
		result = True
		timex = 0
		count = 1
		for row in dataset:#temporary set to 10
			start = time.clock()
			print 'test_data',count
			prediction = self.predict(row[1],weights,flag=count)
			if prediction == row[0]:
				correct+=1
			
			count += 1
			end = time.clock()
  			timex = end - start
  			print 'test time',timex

		accuracy = correct/len(dataset)

		end = time.clock()
  		timex = end - start
		#returns the accuracy of the algorithm in floating point format; returns true if sucess, false otherwise; returns time consumed
		return accuracy,result,timex

	def predict(self,image,weights,flag=-1):
		#classify a single image, returns the index of result (see main for the legend index:[0,7])
		if flag == 1:
			self.neural.set_weight(weights)
		elif flag == -1:
			self.neural.set_weight(weights)
		output = list(self.neural.classify(image))
		predicted_output = output.index(max(output))
		print "output:",output
		return predicted_output