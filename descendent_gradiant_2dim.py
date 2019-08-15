from itertools import product
import numpy as np

learning_ratio = .1

o = 1e-10
EPSILON = 1e-10

f = lambda x, y: (x-3)**2 + (y+1)**2

gradient = lambda f, x, y: np.array(((f(x+o, y)-f(x, y))/o, (f(x, y+o)-f(x, y))/o))

for x, y in product(range(-10, 11, 1), range(-10, 11, 1)):
	print(f'f({x}, {y}) = {f(x, y)}')
	print(f'∇f({x}, {y}) = {gradient(f, x, y)}')

x, y = 4, 7

while True:
	g = gradient(f, x, y)
	x_before, x = x, x - g[0] * learning_ratio
	y_before, y = y, y - g[1] * learning_ratio
	print(f'(x, y) = ({x}, {y})')
	if all(g < EPSILON):
		break

print(f'f({x}, {y}) = {f(x, y)}')
print(f'∇f({x}, {y}) = {gradient(f, x, y)}')
