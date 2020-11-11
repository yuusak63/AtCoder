import math

N,X,T = map(int,input().split())
key = math.ceil(N/X)
ans = key * T
print(ans)