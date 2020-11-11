import math

X = int(input())
year = 0
ans = 100

while ans < X:
    ans = math.floor(ans* 1.01)
    year = year + 1

print(year)


#ans = math.ceil(math.log(X/100,1.01))

#print(ans)

#while 1:
#    ans = ans * 1.01
#    if ans >= X:
#        break
#    year = year + 1

#print(year)