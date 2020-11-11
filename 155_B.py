N = int(input())
A = list(map(int,input().split()))
flg = 0

for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 3 != 0 and A[i] % 5 != 0 :
            flg = 1
            break
        elif A[i] % 3 == 0:
            flg = 0
        elif A[i] % 5 == 0:
            flg = 0
        else:
            flg = 1

if flg == 0:
    print('APPROVED')
else:
    print('DENIED')
