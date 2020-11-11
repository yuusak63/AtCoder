A,B,C = list(map(int,input().split()))

if A == B == C:
    print('No')
elif A == B and B != C:
    print('Yes')
elif A != B and A == C:
    print('Yes')
elif A != B and B ==C:
    print('Yes')
elif A != B and A != C:
    print('No')
else:
    print('No')
