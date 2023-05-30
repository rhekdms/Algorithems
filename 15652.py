import sys
from itertools import product as pro
input = sys.stdin.readline
N, M = map(int,input().split())
N = list(list(range(1,N+1)) for i in range(M))
N = pro(*N)
n = []
for i in N:
    n.append(sorted(i))
N = list(dict.fromkeys(n))
for i in N:
    for j in i:
        if j == '[' or j == ']' or j == ',':
            pass
        else:
            print(j,end='')
    print()
# 시간초과