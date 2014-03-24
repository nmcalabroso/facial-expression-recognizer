from __future__ import division
from random import random
from copy import deepcopy
from math import atan
from math import fabs
from math import pi
import time
import numpy as np

class ANN():

	"""
	Formats:
	self.sizes = [...]

	self.input = [...]
	self.hidden = [[...]...]
	self.output = [...]

	self.weight = [[[...]...]...] => [[layer:[nodes:[values]]]]

	self.err_hidden = [[...]...]
	self.err_output = [...]
	"""

	def __init__(self,input_n,output_n,hidden_n,num_nodes,alpha,eta):
		num_layers = hidden_n+2
		rand = lambda x: 0.01 if x is 0 else x
		self.alpha = alpha #learning rate
		self.eta = eta #momentum
		self.hidden_n = hidden_n
		self.output_n = output_n

		self.input = []
		self.desired = []
		self.sizes = [input_n+1 if i is 0 else output_n if i is num_layers-1 else num_nodes+1 for i in range(num_layers)]
		self.hidden = [np.array([1 for b in range(num_nodes+1)]) for i in range(hidden_n)]
		self.weight = [[[rand(random()) for k in range(self.sizes[i+1])] for j in range(self.sizes[i])] for i in range(num_layers-1)]
		self.weight = [np.array(i) for i in self.weight] #make array
		self.transposed_weight = []
		self.prev_weight = deepcopy(self.weight)
		self.prev_transposed_weight = []
		self.output = np.array([0 for i in range(output_n)])
		self.err_hidden = [np.array([0 for a in range(num_nodes)]) for i in range(hidden_n)]
		self.err_output = []

	def transpose_weight(self):
		self.transposed_weight = [np.transpose(i) for i in self.weight]

		self.prev_transposed_weight = [np.transpose(i) for i in self.prev_weight]

	def train(self,data,epoch = 1):
		#data = [(emotion, [pixels]), ...]
		self.transpose_weight()	#initialize transpose weight

		total_err = 0.0
		new_err = 0.0
		dif = 10
		new_dif = 1

		self.alpha = fabs(dif)/len(data)
		self.eta = fabs(new_dif)/len(data)

		for a in range(epoch):
			total_err = 0.0
			print "alpha:",self.alpha
			print "eta:",self.eta
			print "Epoch:",a+1
			for row in range(len(data)):#temporary set to 2
				self.desired = np.array([pi/2 if i is data[row][0] else -(pi/2) for i in range(self.output_n)])
				self.input = data[row][1]
				self.input.insert(0,1) #insert bias at index 0
				self.input = np.array(self.input)	#make array
				timex = 0.0
				
				"""print "List Lengths:"
				print "len(input):",len(self.input)

				print "len(hidden):",len(self.hidden)
				for i in range(len(self.hidden)):
					print "len(hidden["+str(i)+"]):",len(self.hidden[i])

				print "len(weights):",len(self.weight)
				print "len(weight["+str(0)+"]):",len(self.weight[0])
				print "len(weight["+str(0)+"]["+str(0)+"]):",len(self.weight[0][0])
				"""
				print "\ndata",row, "epoch",a+1
				print "desired:",self.desired
				#print "weight[0][0]",self.weight[0][0]
				#print "hidden[0]:",self.hidden[0]
				print "output:",self.output
				print "error in output:",self.err_output

				start = time.clock()
				print "Feeding forward..."
				for i in range(self.hidden_n+1):
					self.feed_forward(i+1)
				
				print "Propagating backward..."
				for i in range(self.hidden_n,-1,-1):
					self.back_propagation(i)

				
				print "Updating weights..."
				for i in range(self.hidden_n+1):
					self.update_weights(i)

				end = time.clock()
				timex += end-start

				err = (np.sum((self.desired - self.output)**2))/np.size(self.output)#sum(0.5*(self.desired[i]-self.output[i])**2 for i in range(self.output_n))
				total_err += err
				print "Current error for this epoch:",err
				print "One training data took",timex,"sec..."
				# mean squared error
			#raw_input("Continue to new training data...")
			print "\nTotal error:",total_err
			new_dif = dif
			dif = new_err - total_err
			new_err = total_err
			self.alpha = fabs(dif)/len(data)
			self.eta = fabs(new_dif)/len(data)

		return [i.tolist() for i in self.weight]
			
	def feed_forward(self,layer):
		#g = lambda z: 1/(1 + exp(-z))
		g = lambda x: np.arctan(x)
		#print "Current layer:",layer

		if layer == 1: #input layer and 1st hidden layer
			nodes_value = self.input
		else:
			nodes_value = self.hidden[layer-2]

		#test
		transposed_weight = self.transposed_weight[layer-1] #np.array([[i[j] for i in self.weight[layer-1]] for j in range(self.sizes[layer])])
		if layer != self.hidden_n+1:
			self.hidden[layer-1] = g(np.dot(transposed_weight,nodes_value))
		else:
			self.output = g(np.dot(transposed_weight,nodes_value))






		# if layer != self.hidden_n+1:
		#	self.hidden[layer-1] = [g(sum(map((lambda e: e[0]*e[1]),zip([i[j] for i in self.weight[layer-1]],nodes_value))))for j in range(self.sizes[layer])]
		# else:
		# 	self.output = [g(sum(map((lambda e: e[0]*e[1]),zip([i[j] for i in self.weight[layer-1]],nodes_value)))) for j in range(self.sizes[layer])]

	def back_propagation(self,layer):
		#g = lambda z: 1/(1 + exp(-z))
		#dg = lambda x: g(x)*(1-g(x))

		dg = lambda x: 1/((x**2)+1)
		y = self.desired
		#5 4 3 2

		#print "Current layer:",layer

		if layer == self.hidden_n:
			output = self.output
			#change output[i] to summation of w

			#test
			mult = y-output
			transposed_weight = self.transposed_weight[layer]#np.array([[k[i] for k in self.weight[layer]]for i in range(len(output))])
			phi = np.dot(transposed_weight,self.hidden[layer-1])
			self.err_output = dg(phi) * (mult)
		



			#self.err_output = [dg(sum(map((lambda e: e[0]*e[1]),zip([k[i] for k in self.weight[layer]],self.hidden[layer-1]))))*(y[i]-output[i]) for i in range(len(output))]
		else:
			hidden = self.hidden[layer]

			if layer == 0:
				x = self.input
			else:
				x = self.hidden[layer-1]

			if layer == self.hidden_n-1:
				b4 = self.err_output
			else:
				b4 = self.err_hidden[layer+1]

			#test
			transposed_weight = self.transposed_weight[layer] #np.array([[k[i] for k in self.weight[layer]]for i in range(len(hidden))])
			self.err_hidden[layer] = dg(np.dot(transposed_weight,x))*np.dot(self.weight[layer+1],b4)


			#self.err_hidden[layer] = [dg(sum(map((lambda e: e[0]*e[1]),zip([k[i] for k in self.weight[layer]],x))))*sum(map((lambda e: e[0]*e[1]),zip(self.weight[layer+1][i],b4))) for i in range(len(hidden))]

	def update_weights(self,layer):
		#update for layer 0-1 (input layer to 1st-2nd hidden layer)
		#print "Current layer:",layer
		if layer == self.hidden_n:
			err_layer = self.err_output
		else:
			err_layer = self.err_hidden[layer]

		if layer == 0:
			from_layer = self.input
		else:
			from_layer = self.hidden[layer-1]

		#test
		col_vector = np.array(np.matrix(err_layer).T)
		a1 = col_vector*from_layer
		b1 = self.transposed_weight[layer]
		current_weight = b1 + self.alpha*self.prev_transposed_weight[layer] + self.eta*a1

		self.prev_weight[layer] = self.weight[layer]
		self.weight[layer] = np.transpose(current_weight)

		self.transpose_weight()



		#self.weight[layer] = [[self.weight[layer][i][j] + self.alpha*self.prev_weight[layer][i][j] + self.eta*err_layer[j]*from_layer[i] for j in range(len(self.weight[layer][i]))] for i in range(len(self.weight[layer]))]

	def classify(self,image):
		pass

