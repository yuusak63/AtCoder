A,B = list(map(int,input().split()))

if A%2 != B%2:
    print('IMPOSSIBLE')
else :
    x = (A+B)/2
    print(int(x))
