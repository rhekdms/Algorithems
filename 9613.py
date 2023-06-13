import sys
from math import gcd
from itertools import combinations as com
input = sys.stdin.readline

T = int(input())
for i in range(T):
    sol = 0
    num = list(map(int,input().split()))
    combi = list(com(num[1:],2))
    for j in combi:
        sol+=gcd(*j)
    print(sol)