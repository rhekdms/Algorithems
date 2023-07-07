import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for i in range(T):
    p = input().rstrip()
    n = int(input())
    x = input().strip()[1:-1]
    cnt = 0
    if 'D' in p and p.count('D')>n:
        print('error')
    elif not x:
        print('[]')
    else:
        x = deque(map(int,x.split(',')))
        for j in p:
            if j == 'R':
                cnt += 1
            elif cnt%2 == 0:
                x.popleft()
            else:
                x.pop()
        if cnt%2==0:
            print('[',end='')
            print(*list(x),sep=',',end='')
            print(']')
        else:
            print('[',end='')
            print(*(list(x)[::-1]),sep=',',end='')
            print(']')