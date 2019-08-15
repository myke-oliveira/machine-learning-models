#! python3

import numpy as np

learning_ratio = .1

print('Train set - Logic OR')
X = np.array(((0, 0), (0, 1), (1, 0), (1, 1)))

Y = np.array((0, 1, 1, 1))
print('X     Y')
for x, y in zip(X, Y):
	print(x, y)
print()

weights = np.array((0., 0.))
print(f'Weights = {weights}')

activation_fuction = lambda x: 1 if x >= 1 else 0
neural_output = lambda x: activation_fuction(x.dot(weights))

# Output from Neural Network
print(f'Output from Neural Network:')
print('X     Y')
for x in X:
	print(x, neural_output(x))
print()

# Train Neural Network
print('Training Neural Network...')
while (any(y - neural_output(x) for x, y in zip(X, Y))):
	for x, y in zip(X, Y):
		weights += learning_ratio * x * (y - neural_output(x))
		print(weights)

print('Final Output')
for x in X:
	print(x, neural_output(x))