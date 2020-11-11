S = int(input())
cnt = 0
LenS = len(str(S))
strS = str(S)

for i in range(1,LenS):
    for j in range(1,LenS):
        strS = strS[i:j]
        #strS = int(strS)
        if strS % 2019 == 0:
            cnt = cnt + 1

print(cnt)
