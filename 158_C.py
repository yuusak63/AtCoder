import math

A,B = map(int,input().split())

#calcA = (int,A / 0.08)
#calcB = (int,B / 0.10)
bai = int(A/0.08) * int(B/0.10) // math.gcd(int(A/0.08), int(B/0.10))
print(A)
print(B)
#print(calcA)
#print(calcB)
print(bai)


#if calcA == calcB:
#    print(calcA)
#else:
#    print('-1')
