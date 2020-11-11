A,B,C,D = map(int,input().split())

Takahashi = A
Aoki = C

#whileTakahashi > 0 or Aoki > 0 :
while True:
    Aoki = Aoki - B
    if Aoki <= 0:
        break

    Takahashi = Takahashi - D
    if Takahashi <= 0:
        break

if Takahashi <= 0:
    print('No')
else:
    print('Yes')
