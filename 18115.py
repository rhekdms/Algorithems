import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = deque(map(int,input().split()))
sol = deque()
for i in range(1,N+1):
    if A[-1] == 1:
        sol.appendleft(i)
    elif A[-1] == 2:
        sol.insert(1,i)
    else:
        sol.append(i)
    A.pop()
print(*sol)