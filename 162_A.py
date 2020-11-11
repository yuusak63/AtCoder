N = int(input())
N = str(N)
num = []
num = [int(x) for x in list(str(N))]
lenN = len(N)
flg = 0


for i in range(lenN):
    if num[i] == 7:
        flg = 1

if flg == 1:
  print('Yes')
else:
  print('No')
