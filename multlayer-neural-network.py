import numpy as np

X = np.array([[0, 0],
	[0, 1],
	[1, 0],
	[1, 1]])

Y = np.array([[0], [1], [1], [0]])

print('X = ')
print(X)
print()
print('Y = ')
print(Y)
print()

weights0 = np.array([[-.424, -.740, -.961],
	[.358, -.577, -.469]])

print('weights0 = ')
print(weights0)

print(weights0 * X)
