K, X = map(int,input().split())
for i in range(X - K + 1,K + X):
    if i < X + K - 1:
        print(i,end = ' ')
    else:
        print(i)
