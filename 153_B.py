H,N = list(map(int,input().split()))
A = list(map(int,input().split()))
para = H

list.sort(A, reverse=True)

for i in range(N):
    para = para - A[i]
    if para <= 0 :
        print('Yes')
        break
    elif i ==N - 1  and para > 0:
         print('No')
