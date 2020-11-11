x = list(map(int,input().split()))

for j in range(5):
    if x[j] == 0:
        print(j+1)
        break