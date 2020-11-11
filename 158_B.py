N,A,B = map(int,input().split())
cnt = 0
num = 0
flg = 'A'

for i in range(N):
    if flg == 'A' and num < A:
        cnt += 1
        num += 1
        if num == A:
            num = 0
            flg = 'B'
    elif flg == 'B' and num < B:
        num += 1
        if num == B:
            num = 0
            flg = 'A'
print(cnt)
