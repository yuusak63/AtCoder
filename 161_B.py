N,M = map(int,input().split())
A = list(map(int,input().split()))
sumA = 0

for i in range(N):
  sumA = sumA + A[i]

cnt = 0

for j in range(N):
  if sumA * (1/4/M) <= A[j]:
    cnt = cnt + 1

if cnt >= M:
  print('Yes')
else :
  print('No')
