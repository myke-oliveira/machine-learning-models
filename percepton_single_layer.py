#! python3

import itertools

inputs = [1, 7, 5]
weights = [0.8, 0.1, 0]

sumxw = sum(x*w for x, w in zip(inputs, weights))

print(sumxw)

activation_fuction = lambda x: 1 if x > 0 else 0

print(activation_fuction(sumxw))
