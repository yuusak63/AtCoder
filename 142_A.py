N = int(input())
cnt = 0
ans = 0

for i in range(1,N+1):
     if i % 2 == 1 :
        cnt += 1
ans = cnt / N
print('{:.10f}'.format(ans))
