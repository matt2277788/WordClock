
import numpy as np


filepath = '/home/treffer/playground/WordClock/Layout'
letterMatrix = np.loadtxt(fname=filepath, dtype=str)
#letterMatrix.tolist()
s=("".join(letterMatrix.tolist()))

print(s)

