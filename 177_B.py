import math

S = str(input())
T = str(input())

ans = len(T)

for i in range(0,len(S) - len(T)+1):
    diff = 0
    for j in range(len(T)):
        if T[j] != S[i + j]:
            diff += 1
    ans = min(ans,diff)

print(ans)