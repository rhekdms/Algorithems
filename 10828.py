import sys
input = sys.stdin.readline
from collections import deque
N=int(input())
stack = deque()
for i in range(N):
    A = input().rstrip()
    if 'push' in A:
        stack.append(int(list(A.split())[1]))
    if A == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if A == 'size':
        print(len(stack))
    if A == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if A == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)