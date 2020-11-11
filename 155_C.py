import collections

N = int(input())
s = [input() for i in range(N)]
k = 0
i = 0
ans =[]

c = collections.Counter(s)
c_mc=c.most_common()
for i in range(len(c)):
    if c_mc[i][1] ==c_mc[0][1]:
        ans.append(c_mc[i][0])

ans_A =sorted(ans)
for i in range(len(ans_A)):
    print(ans_A[i])
