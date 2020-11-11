import math
N,D = map(int,input().split())
cnt = 0
for i in range(N):
    X, Y = map(int, input().split())
    sqrt = math.sqrt(X**2 + Y**2)
    if sqrt <= D:
        cnt = cnt + 1

print(cnt)