import sys
input = sys.stdin.readline
N, M = map(int,input().split())

a = [list(map(int,input().split())) for i in range(N)]

b = []
for j in range(N):
    b.append(list(map(int,input().split())))
    
for k in range(N):
    for l in range(M):
        a[k][l] +=  b[k][l]


for i in range(N):
    print(*a[i])