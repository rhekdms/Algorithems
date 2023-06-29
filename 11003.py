import sys
from collections import deque
input = sys.stdin.readline
N,L = map(int,input().split())
A = list(map(int,input().split()))
sol = deque()
for i in range(N):
    sol.append(A[i])
    if len(sol) == L+1:
        sol.popleft()
    print(min(sol),end=' ')

#다시!