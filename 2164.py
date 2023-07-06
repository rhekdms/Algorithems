import sys
from collections import deque
input=sys.stdin.readline
N = int(input())
N = deque(range(1,N+1))
while len(N)>1:
    N.popleft()
    N.rotate(-1)
print(N[0])