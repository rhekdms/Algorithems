import sys
from collections import deque
input=sys.stdin.readline
N,K = map(int,input().split())
V = tuple(sorted(map(int,input().split())))
m = tuple(V[i+1]-V[i] for i in range(N-1))
if N-K-2 >0:
    temp = deque([min(m[:(N-K-2)])])
else:
    temp = deque([])
sol = 20000001
for i in range(K+1):
    if i-1>=0 and temp[0] == m[i-1]:
        temp.popleft()
    while len(temp) >= 1 and m[i+(N-K-2)] < temp[-1]:
        temp.pop()
    temp.append(m[i+(N-K-2)])
    sol = min(temp[0]+V[i+(N-K-1)]-V[i], sol)
print(sol)