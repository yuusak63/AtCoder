N = int(input())
A = list(map(int,input().split()))
sum = 0
ans = 0

for i in range(N):
    sum = sum + ((A[i])**-1)
    ans = sum**-1

print(ans)
