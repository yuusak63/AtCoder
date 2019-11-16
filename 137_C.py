from collections import Counter

N = int(input())
s_sorted = []

for _ in range(N):
    s_sorted.append(''.join(sorted(input())))
s_count = Counter(s_sorted)
ans = 0
for i in s_count:
    ans += (s_count[i] * (s_count[i] - 1)) // 2
print(ans) 
