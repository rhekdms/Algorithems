import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G = [list(map(int,input().split())) for i in range(N)]
sum_G = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        sum_G[i][j] = G[i-1][j-1] + sum_G[i-1][j] + sum_G[i][j-1] - sum_G[i-1][j-1]
for i in range(M):
    x_1,y_1,x_2,y_2 = map(int,input().split())
    if x_2<=N and y_2<=N:
        print(sum_G[x_2][y_2]-sum_G[x_2][y_1-1]-sum_G[x_1-1][y_2]+sum_G[x_1-1][y_1-1])