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

def main():
	print "inputx:",inputx
	print "sizes:",sizes
	print "weight:"
	print('\n'.join('{}: {}'.format(*k) for k in enumerate(weight)))
	
	for i in range(hidden_n+1):
		print "output:",feed_forward(i+1)
		print "inputx:",inputx
		print "hidden:",hidden
		raw_input("Continue...")

if __name__ == '__main__':
	main()
