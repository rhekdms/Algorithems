import sys
from itertools import permutations as per
input = sys.stdin.readline
N,M = map(int,input().split())
a = list(map(int,input().split()))
for i in list(sorted(per(a,M))):
    print(*i)