from random import random
from operator import mul
from math import atan
import numpy as np

class ANN():

	def __init__(self,input_n,output_n,hidden_n,num_nodes,alpha,eta):
		self.input = [] 

		self.hidden_n = hidden_n

		self.hidden = [[0 for a in range(num_nodes)] if i==hidden_n-1 else [0 for b in range(num_nodes+1)] for i in range(hidden_n)]


		num_layers = hidden_n+2

		self.sizes = [input_n+1 if i is 0 else output_n if i is num_layers-1 else num_nodes if i is num_layers-2 else num_nodes+1 for i in range(num_layers)]

		rand = lambda x: 0.01 if x is 0 else x
		
		self.weight = [ [ [rand(random()) for k in range(self.sizes[i+1])] for j in range(self.sizes[i])] for i in range(num_layers-1)]

		self.output = [0 for i in range(output_n)]


	def train(self, data):
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

