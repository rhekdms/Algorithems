import sys
input = sys.stdin.readline
N, M = map(int,input().split())
a = []
for N in range(1,N+1):
    a.append(N)
for M in range(M):
    i, j = map(int,input().split())
    b = a[i-1:j]
    b = b[::-1]
    a[i-1:j] = b
for a in a:
    print(a, end=' ')
'''
b = a[i-1:j-2:-1]
a[i-1:j] = b
N M
5 4  (0 1 2 3 4)
i j
1 2   2 1 3 4 5
3 4   2 1 4 3 5
1 4   3 4 1 2 5
2 2   3 4 1 2 5
'''