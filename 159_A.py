#coding:utf-8
#from scipy.special import comb
import itertools

#a = len(list(itertools.combinations(range(n), r)))
#a = factorial(n) / factorial(r) / factorial(n - r)

N, M = map(int, input().split())

ansN = len(list(itertools.combinations(range(N), 2)))
ansM = len(list(itertools.combinations(range(M), 2)))

ans = ansN + ansM
#ans = comb(N,2,exact = True) + comb(M,2,exact = True)

print(ans)
