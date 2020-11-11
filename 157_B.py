n = 3  # nは入力回数
A = []
for i in range(n):
    array = list(map(int, input().strip().split()))
    A.append(array)

N = int(input())
b = [input() for i in range(N)]

for j in range(0,3):
    for k in range(0,3):
        for m in range(N):
            if A[j][k] == b[m]:
                A[j][k] = 0
                break

if A[0][0] == 0 and A[0][1] == 0 and A[0][2] == 0:
    print('Yes')
elif A[1][0] == 0 and A[1][1] == 0 and A[1][2] == 0:
    print('Yes')
elif A[2][0] == 0 and A[2][1] == 0 and A[2][2] == 0:
    print('Yes')
elif A[0][0] == 0 and A[1][0] == 0 and A[2][0] == 0:
    print('Yes')
elif A[0][1] == 0 and A[1][1] == 0 and A[2][1] == 0:
    print('Yes')
elif A[0][2] == 0 and A[1][2] == 0 and A[2][2] == 0:
    print('Yes')
elif A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
    print('Yes')
elif A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0:
    print('Yes')
else:
    print('No')
