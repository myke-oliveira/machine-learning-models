from time import sleep
learning_ratio = .1

dx = 1e-10

f = lambda x: x**2 - 3*x + 2

d = lambda f, x: (f(x+dx)-f(x))/dx

x = 4

print(f'x = {x}')
print(f'f(x) = {f(x)}')
print(f'df/dx = {d(f, x)}')

while True:
	x_n_1, x = x, x - d(f, x) * learning_ratio
	if abs(x_n_1 - x) < dx:
		break

print(f'x = {x}')
print(f'f(x) = {f(x)}')
print(f'df/dx = {d(f, x)}')