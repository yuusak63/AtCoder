import math

A,B,H,M = map(int,input().split())

degH = 30 * H + 0.5 * M
degM = 6 * M

digA = abs(degH - degM) * math.pi / 180
#度 × 円周率 ÷ 180
if digA <= math.pi /2 :
    ans = float(math.sqrt((A**2) + (B**2) - (2*A*B*math.cos(digA))))
else:
    ans = float(math.sqrt((A**2) + (B**2) - (2*A*B*math.cos(-digA))))

print('{:.21f}'.format(ans))
