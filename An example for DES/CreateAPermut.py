
import numpy as np

arr = np.arange(64).reshape((8,8))
arr = arr.ravel()
np.random.shuffle(arr)
arr = arr.reshape(8,8)

print(arr)

