from __future__ import division
from random import random

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
		self.input = []
		self.hidden_n = hidden_n
		self.sizes = [input_n+1 if i is 0 else output_n if i is num_layers-1 else num_nodes if i is num_layers-2 else num_nodes+1 for i in range(num_layers)]
		self.hidden = [[0 for a in range(num_nodes)] if i==hidden_n-1 else [0 for b in range(num_nodes+1)] for i in range(hidden_n)]
		self.weight = [[[rand(random()) for k in range(self.sizes[i+1])] for j in range(self.sizes[i])] for i in range(num_layers-1)]
		self.output = [0 for i in range(output_n)]
		
		self.err_hidden = [[0 for a in range(num_nodes)] for i in range(hidden_n)]
		self.err_output = []

	def train(self,data):
		#data = [(emotion, [pixels]), ...]
		for row in range(len(data)):
			self.input = data[row][1]
			self.input.insert(0,1) #insert bias at index 0

			#put values in hidden and output layer
			for i in range(self.hidden_n+1):
				self.feed_forward(i+1)

	def feed_forward(self,layer):
		g = lambda x: atan(x)

		if layer == 1: #input layer and 1st hidden layer
			nodes_value = self.input
		else:
			nodes_value = self.hidden[layer-2]

		if layer != self.hidden_n+1:
			self.hidden[layer-1] = [g(sum(map((lambda e: e[0]*e[1]),zip([i[j] for i in self.weight[layer-1]],nodes_value)))) for j in range(self.sizes[layer])]
		else:
			self.output = [g(sum(map((lambda e: e[0]*e[1]),zip([i[j] for i in self.weight[layer-1]],nodes_value)))) for j in range(self.sizes[layer])]

	def back_propagation(self,layer,y):
		dg = lambda x: 1/(x**2+1)
		#5 4 3 2
		if layer == self.hidden_n:
			output = self.output
			#change output[i] to summation of w
			self.err_output = [dg(sum(map((lambda e: e[0]*e[1]),zip([k[i] for k in self.weight[layer]],self.hidden[layer]))))*(y[i]-output[i]) for i in range(len(output))]
		else:
			hidden = self.hidden[layer+1]

			if layer == 0:
				x = self.input
			else:
				x = self.hidden[layer-1]

			if layer == self.hidden_n-1:
				b4 = self.err_output
			else:
				b4 = self.err_hidden[layer+1]

			self.err_hidden[layer] = [dg(sum(map((lambda e: e[0]*e[1]),zip([k[j] for k in self.weight[layer]],x))))*sum([self.weight[layer][i][j]*b4[j] for j in range(len(self.weight[layer][i]))]) for i in range(len(hidden))]

	def update_weights(self):
		for i in range(len(self.weights)):
			for j in range(len(self.weights[i])):
				for k in range(len(self.weights[i][j])):
					self.weights
					if i == 0:
						pass
					elif i == 2:
						pass