N,M = map(int,input().split())
A = list(map(int,input().split()))

ans = N
for i in range(M):
  ans = ans - A[i]

if ans < 0:
  print('-1')
else:
  print(ans)
