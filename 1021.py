import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
num = deque(map(int,input().split()))
N = deque(range(1,N+1))
cnt = 0
while num:
    if N[0] == num[0]:
        num.popleft()
        N.popleft()
    elif N.index(num[0])<=len(N)//2:
        N.rotate(-1)
        cnt+=1
    else:
        N.rotate(1)
        cnt+=1
print(cnt)