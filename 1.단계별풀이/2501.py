import sys

input = sys.stdin.readline
N, K = map(int,input().split())
n = []
for i in range(1, N+1):
    if N % i == 0:
        n.append(i)
if len(n) >= K:
    print(n[K-1])
else:
    print(0)