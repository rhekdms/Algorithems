import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
num = deque()
queue = deque()
sol = []
for i in range(n):
    num.append(int(input()))
i = 1
while num:
    if i<=n and (not queue or queue[-1]!=num[0]):
        queue.append(i)
        i+=1
        sol.append('+')
    elif i<=n+1 and queue[-1]==num[0]:
        queue.pop()
        num.popleft()
        sol.append('-')
    else:
        break

if num:
    print('NO')
else:
    print(*sol,sep='\n')