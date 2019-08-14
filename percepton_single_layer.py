#! python3

import numpy as np

inputs = np.array([1, 7, 5])
weights = np.array([0.8, 0.1, 0])

sumxw = inputs.dot(weights)

print(sumxw)

activation_fuction = lambda x: 1 if x > 0 else 0

print(activation_fuction(sumxw))
