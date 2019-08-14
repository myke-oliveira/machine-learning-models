#! python3

import numpy as np

learning_ratio = .1

print('Train set - Logic AND')
X = [np.array((0, 0)), np.array((0, 1)), np.array((1, 0)), np.array((1, 1))]

Y = [0, 0, 0, 1]
print('X     Y')
for x, y in zip(X, Y):
	print(x, y)
print()

weights = np.array((0, 0))
print(f'Weights = {weights}')

activation_fuction = lambda x: 1 if x >= 1 else 0
neural_output = lambda x: x.dot(weights)

# Output from Neural Network
print(f'Output from Neural Network:')
print('X     Y')
for x in X:
	print(x, neural_output(x))
print()

# Train Neural Network
print('Training Neural Network...')

while True:
	for x, y in zip(X, Y):
		print(x, y)
		# weights = weights + learning_ratio * x * (y-)
	break


