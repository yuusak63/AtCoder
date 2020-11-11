import math
D,T,S = map(int,input().split())

calc = math.ceil(D/S)

if calc <= T:
    print('Yes')
else:
    print('No')
