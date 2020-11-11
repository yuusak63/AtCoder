K,N = map(int,input().split())
A = list(map(int,input().split()))
sum = 0

if A[0] != 0:
  for i in range(1,N):
    sum = sum + (A[i] - A[i-1])
else:
  for i in range(2,N):
      sum = sum + (A[i] - A[i-1])

print(sum)
