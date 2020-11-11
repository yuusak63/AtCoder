import math
N = int(input())

a = math.ceil(N / 1000)
ans = (1000*a) -N

print(ans)