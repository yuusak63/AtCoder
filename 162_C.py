import math
import itertools

K= int(input())
sum = 0

for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            sum = sum + math.gcd(math.gcd(i,j),k)

print(sum)
