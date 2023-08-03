import sys
from collections import deque
input = sys.stdin.readline
K = int(input())
a = deque([0])
for i in range(K):
    b = int(input())
    if b:
        a.append(b)
    else:
        a.pop()
print(sum(a))