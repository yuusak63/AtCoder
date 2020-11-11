N,K,M = list(map(int,input().split()))
A = list(map(int,input().split()))
sum = 0
ave = 0

for i in range(N-1):
    sum = sum + A[i]

if M*N-sum <=0:
    print(0)
elif M*N-sum >K:
    print(-1)
else:
    print(M*N-sum)
