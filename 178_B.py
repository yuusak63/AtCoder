import math
A,B,C,D = map(int,input().split())

cal1 = A*C
cal2 = A*D
cal3 = B*C
cal4 = B*D

ans = max(cal1,cal2,cal3,cal4)
print(ans)
