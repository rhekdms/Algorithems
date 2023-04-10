import sys
input = sys.stdin.readline
N, M = map(int,input().split())
a = []
for N in range(1,N+1):
    a.append(N)
for M in range(M):
    b = a
    i, j = map(int,input().split())
    a[i-1], a[j-1] = b[j-1], b[i-1]
for a in a:
    print(a, end=' ')
'''
N개 바구니 M번 공바꾸기
5         4
i j 교환
1 2     2 1 3 4 5
3 4     2 1 4 3 5
1 4     3 1 4 2 5
2 2     3 1 4 2 5
'''