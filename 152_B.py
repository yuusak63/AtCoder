A,B = list(map(int,input().split()))
para_a = str(B)
para_b = str(A)

for i in range(A-1):
    para_a = para_a + str(B)

for i in range(B-1):
    para_b = para_b + str(A)

if para_a < para_b:
    print(para_a)
else:
    print(para_b)
