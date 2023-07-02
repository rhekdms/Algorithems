import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
que = deque()
for i in range(N):
    a = input().rstrip()
    if 'push' in a:
        que.append(list(a.split())[1])
    elif a == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif a == 'size':
        print(len(que))
    elif a == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif a == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif a == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)