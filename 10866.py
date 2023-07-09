import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
queue = deque()
for i in range(N):
    a = input().rstrip()
    if 'push_front' in a:
        queue.appendleft(int(list(a.split())[1]))
    elif 'push_back' in a:
        queue.append(int(list(a.split())[1]))
    elif a == 'size':
        print(len(queue))
    elif a == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif queue:
        if a == 'pop_front':
            print(queue.popleft())
        elif a == 'pop_back':
            print(queue.pop())
        elif a == 'front':
            print(queue[0])
        else:
            print(queue[-1])
    else:
        print(-1)