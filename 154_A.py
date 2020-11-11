S,T = list(map(str,input().split()))
A,B = list(map(int,input().split()))
U = input()

if U == S:
    A = A - 1
else:
    B = B - 1

print(A,B)
