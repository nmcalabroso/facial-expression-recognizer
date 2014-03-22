from __future__ import division
from random import random
from copy import deepcopy
from math import atan
from math import fabs
from math import pi
#from mpmath import mp
#@from mpmath import exp

import time

#add bias for the last hidden layer

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
		self.alpha = alpha
		self.eta = eta
		self.hidden_n = hidden_n
		self.output_n = output_n

		self.input = []
		self.desired = []
		self.sizes = [input_n+1 if i is 0 else output_n if i is num_layers-1 else num_nodes+1 for i in range(num_layers)]
		self.hidden = [[0 for b in range(num_nodes+1)] for i in range(hidden_n)]
		self.weight = [[[rand(random()) for k in range(self.sizes[i+1])] for j in range(self.sizes[i])] for i in range(num_layers-1)]
		self.prev_weight = deepcopy(self.weight)
		self.output = [0 for i in range(output_n)]
		self.err_hidden = [[0 for a in range(num_nodes)] for i in range(hidden_n)]
		self.err_output = []

	def train(self,data,epoch = 5):
		#data = [(emotion, [pixels]), ...]
		total_err = 0.0
		new_err = 0.0
		dif = 10
		new_dif = 1

		self.eta = fabs(dif)/len(data)
		self.alpha = fabs(new_dif)/len(data)

		for a in range(epoch):
			total_err = 0.0
			print "alpha:",self.alpha
			print "eta:".self.eta
			print "Epoch:",a+1
			for row in range(len(data)):
				self.desired = [pi/2 if i is data[row][0] else -(pi/2) for i in range(self.output_n)]
				self.input = data[row][1]

				self.input.insert(0,1) #insert bias at index 0
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

				total_err += sum(0.5*(self.desired[i]-self.output[i])**2 for i in range(self.output_n))
				print "One training data took",timex,"sec..."
				# mean squared error
			#raw_input("Continue to new training data...")
			print "Total error:",total_err
			new_dif = dif
			dif = new_err - total_err
			new_err = total_err
			self.alpha = fabs(new_dif)/len(data)
			self.eta = fabs(dif)/len(data)

	def feed_forward(self,layer):
		#g = lambda z: 1/(1 + exp(-z))
		g = lambda x: atan(x)
		#print "Current layer:",layer

		if layer == 1: #input layer and 1st hidden layer
			nodes_value = self.input
		else:
			nodes_value = self.hidden[layer-2]

		if layer != self.hidden_n+1:
			self.hidden[layer-1] = [g(sum(map((lambda e: e[0]*e[1]),zip([i[j] for i in self.weight[layer-1]],nodes_value))))for j in range(self.sizes[layer])]
		else:
			self.output = [g(sum(map((lambda e: e[0]*e[1]),zip([i[j] for i in self.weight[layer-1]],nodes_value)))) for j in range(self.sizes[layer])]

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
			self.err_output = [dg(sum(map((lambda e: e[0]*e[1]),zip([k[i] for k in self.weight[layer]],self.hidden[layer-1]))))*(y[i]-output[i]) for i in range(len(output))]
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

			self.err_hidden[layer] = [dg(sum(map((lambda e: e[0]*e[1]),zip([k[i] for k in self.weight[layer]],x))))*sum(map((lambda e: e[0]*e[1]),zip(self.weight[layer+1][i],b4))) for i in range(len(hidden))]

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

		self.weight[layer] = [[self.weight[layer][i][j] + self.alpha*self.prev_weight[layer][i][j] + self.eta*err_layer[j]*from_layer[i] for j in range(len(self.weight[layer][i]))] for i in range(len(self.weight[layer]))]
