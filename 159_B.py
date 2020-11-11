S = list(str(input()))
N = len(S)
revS = S[::-1]

num1 = int((N-1)/2)
num2 = int((N+3)/2)

strN = S[1:num1]
endN = S[num2:N]

if S == revS and strN == endN:
    print('Yes')
else:
    print('No')
