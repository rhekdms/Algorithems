import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
S = deque()
for i in range(N):
    A = input().rstrip()
    if 'push' in A:
        S.append(int(list(A.split())[-1]))
    elif A == 'size':
        print(len(S))
    elif A == 'empty':
        if S:
            print(0)
        else:
            print(1)
    elif not S:
        print(-1)
    elif A == 'pop':
        print(S.popleft())
    elif A == 'front':
        print(S[0])
    elif A == 'back':
        print(S[-1])