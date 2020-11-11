N = int(input())
A = list(map(int,input().split()))

sum = 0
key = 0
para = A[0]
for i in range(N):
    if i == 0:
        continue
    else:
        if para > A[i]:
            key = para - A[i]
            sum = sum + key
        else:
            key = 0
            sum = sum + key
            para = A[i]

print(sum)