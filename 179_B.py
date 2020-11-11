N = int(input())
D = [list(input()) for _ in range(N)]

cnt = 0

for j in range(N):
    if D[j][0] == D[j][2]:
        cnt +=1 
    elif cnt < 3 and D[j][0] != D[j][2]:
        cnt = 0

if cnt >= 3:
    print('Yes')
else:
    print('No')