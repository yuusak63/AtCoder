N,K = map(int,input().split())

d = []
A = []
ans = []

for m in range(K):
    mm = m+1
    ans.append(mm) 

for i in range(K):
    dd = int(input())
    d.append(dd)
    aa = list(map(int,input().split()))
    A.append(aa)

#for  j in range(K):
#    ans.remove(A)

ans2 = [i2 for i2 in ans if ans == A]
print(ans2)