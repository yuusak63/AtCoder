import math

N = int(input())
n = str(N)

L = sum(list(map(int, str(N))))

ans = L % 9
if ans == 0:
    print('Yes')
else:
    print('No')