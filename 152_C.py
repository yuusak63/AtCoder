N = int(input())
A = list(map(int,input().split()))
lng_a = N
cnt = 0
for i in range(0,N):
    if i == 0:
        cnt = 1
        lng_a = A[i]
    else:
        if lng_a > A[i]:
            cnt += 1
            lng_a = A[i]
print(cnt)
