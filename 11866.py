import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
num = deque(range(1,N+1))
print('<',end="")
while len(num)!=1:
    num.rotate(-K+1)
    print(num.popleft(),end=", ")
print(num.popleft(),end=">")