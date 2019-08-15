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
print()

# sigmoide
f = lambda x: 1 / (1 + np.exp(x))

print('Hidden Layer')
S = f(np.matmul(X, weights0))
print(S)
print()

weights1 = np.array([[-.017],
	[-.893],
	[.148]])

print('weights1 = ')
print(weights1)
print()

print('Output')
T = f(np.matmul(S, weights1))
print(T)
