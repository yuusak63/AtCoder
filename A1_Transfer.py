A, B, C = map(int,input().split())
if B+C < A:
    print(0)
else:
    ans = C - (A - B)
    print (ans)
