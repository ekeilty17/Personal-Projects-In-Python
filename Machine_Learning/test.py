import numpy as np

data = np.array([ [1, 1, 1], [2, 2, 2], [3, 3, 3] ])
labels = np.array([ 1, 2, 3 ])

print(data)
print(np.multiply(data, labels[:, np.newaxis]))