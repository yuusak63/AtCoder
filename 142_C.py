N = int(input())
A = list(map(int,input().split()))

B =[0]*N
i = 1
for num in A:
    B[num-1] = i
    i += 1

print(*B)
