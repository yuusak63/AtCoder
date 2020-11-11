N = int(input())
num = []
for i in range(1,N+1):
    num.append(i)

for j in range(N):

    if num[j] % 3 == 0 and num[j]  % 5 == 0 :
        num[j] = 'FizzBuzz'
    elif num[j] % 3 == 0:
        num[j] = 'Fizz'
    elif num[j] % 5 == 0:
        num[j] = 'Buzz'

sum = 0

for k in range(N):
    if num [k] == 'FizzBuzz' or num[k] == 'Fizz' or num[k] =='Buzz':
        sum = sum
    else:
        sum = sum + num[k]

print(sum)
