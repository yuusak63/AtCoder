import sys

N,K = list(map(int,input().split()))
H = list(map(int,input().split()))
para = H

list.sort(H, reverse=True)

if N < K:
    print(0)
    sys.exit()

cnt = 0

for i in range(N):
    para = H[i]
    while para > 0:
        para = para - 1
        cnt += 1

for i in range(N):
    para = para - A[i]
    if para <= 0 :
        print('Yes')
        break
    elif i ==N - 1  and para > 0:
         print('No')



while H > 0:
  H = H - A
  i += 1

print(i)
