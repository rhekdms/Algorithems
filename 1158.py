import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
N = deque(range(1,N+1))
sol = []
while N:
    N.rotate(-K+1)
    sol.append(N.popleft())
print('<',end='')
print(*sol,sep=', ',end='')
print('>')