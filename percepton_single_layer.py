#! python3

import itertools

inputs = [1, 7, 5]
weights = [0.8, 0.1, 0]

print(sum(x*w for x, w in itertools.product(inputs, weights)))
