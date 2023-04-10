import sys
input = sys.stdin.readline
N, M = map(int,input().split())
a = []
for N in range(N):
    a.append(0)
for M in range(M):
    i, j, k = map(int,input().split())
    for x in range(i-1,j):
        a[x] = k
for a in a:
    print(a, end=' ')
'''
N M
5 4

i j k
1~2 3   3 3 0 0 0
3~4 4   3 3 4 4 0
1~4 1   1 1 1 1 0
2~2 2   1 2 1 1 0
'''