H,A = list(map(int,input().split()))
para = H
i = 0

while H > 0:
  H = H - A
  i += 1

print(i)
