#! python3

import numpy as np

class PerceptonNetwork():

	def __init__(self, learning_ratio = 0.1, dim = 2,
		activation_function = lambda x: 1 if x >= 1 else 0):

		self.learning_ratio = learning_ratio
		self.weights = np.zeros(2)
		self.activation_function = activation_function

	def output(self, x):
		return self.activation_function(x.dot(self.weights))

	def train(self, X, Y):
		while any(Y - np.array(list(map(self.output, X)))):
			for x, y in zip(X, Y):
				self.weights += self.learning_ratio * x * (y - self.output(x))


	def print(self, X):
		for x in X:
			print(x, neural_output(x))

# Train set - Logic AND'
X = np.array(((0, 0), (0, 1), (1, 0), (1, 1)))

Y = np.array((0, 0, 0, 1))

net = PerceptonNetwork()

# Output from Neural Network
print(f'Output from Neural Network:')
print('X     Y')
for x in X:
	print(x, net.output(x))
print()

# Train Neural Network
net.train(X, Y)

print('Final Output')
for x in X:
	print(x, net.output(x))