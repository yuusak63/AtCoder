import numpy as np

N = int(input())
S = [input() for i in range(N)]

print(len(np.unique(S)))
