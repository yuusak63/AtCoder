K = int(input())
A,B = map(int,input().split())

flg = 0
ans = A

#for i in range(A,B):
#    if i % K == 0:
#        flg = 1
#        break

while ans <= B:
    if ans % K ==0:
        flg = 1
        break
    ans = ans +1


if flg == 1:
    print('OK')
else:
    print('NG')