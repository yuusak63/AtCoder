import re
S = str(input())
T = str(input())

if re.match(S,T) :
    print('Yes')
else:
    print('No')