N,K = map(int,input().split())
diff = N
cnt = 0

while True :
    #if diff > K:
    #    diff = diff - K
    #else:
    #    diff = K - diff
    if K == 1:
        diff = 0
        cnt = 2
    else:
        diff = abs(diff - K)
        cnt += 1

    if diff < K and cnt >= 2:
        break

print(diff)
