from random import random
from math import atan

input_n = 4
output_n = 2
hidden_n = 2
num_nodes = 2

inputx = [i for i in range(input_n+1)]
num_layers = hidden_n+2
sizes = [input_n+1 if i is 0 else output_n if i is num_layers-1 else num_nodes if i is num_layers-2 else num_nodes+1 for i in range(num_layers)]
rand = lambda x: 0.01 if x is 0 else x		
weight = [[[rand(random()) for k in range(sizes[i+1])] for j in range(sizes[i])] for i in range(num_layers-1)]
hidden = [[0 for a in range(num_nodes)] if i==hidden_n-1 else [0 for b in range(num_nodes+1)] for i in range(hidden_n)]

err_hidden = [[0 for a in range(num_nodes)] for i in range(hidden_n)]
err_output = []

def feed_forward(layer):
	g = lambda x: atan(x)
	output = [0 for i in range(output_n)]

	if layer == 1: #input layer and 1st hidden layer
		nodes_value = inputx
	else:
		nodes_value = hidden[layer-2]

	if layer != hidden_n+1:
		hidden[layer-1] = [g(sum(map((lambda e: e[0]*e[1]),zip([i[j] for i in weight[layer-1]],nodes_value)))) for j in range(sizes[layer])]
	else:
		output = [g(sum(map((lambda e: e[0]*e[1]),zip([i[j] for i in weight[layer-1]],nodes_value)))) for j in range(sizes[layer])]

	return output

def back_propagation(layer,y):
	dg = lambda x: 1/(x**2+1)
		#5 4 3 2
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

def main():
	print "inputx:",inputx
	print "sizes:",sizes
	print "weight:"
	print('\n'.join('{}: {}'.format(*k) for k in enumerate(weight)))
	
	print "Feed Forward:"
	for i in range(hidden_n+1):
		print "output:",feed_forward(i+1)
		print "inputx:",inputx
		print "hidden:",hidden
		raw_input("Continue...")

	print "Back Propagation:"
	for i in range(hidden_n,0,-1): 
		print "output:",back_propagation(i)
		raw_input("Continue...")
		
	print "Updating Weights:"


if __name__ == '__main__':
	main()
