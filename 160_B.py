X = int(input())

ans1 = X // 500

calc1 = X -(500*ans1)
ans2 = calc1 // 5

ans = ans1 *1000 + ans2 *5

print(ans)
