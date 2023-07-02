import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N,W = map(int,input().split())
    M = [list(map(int,input().split())) for i in range(2)]
    check = [[1]*N for i in range(2)]
    for l in range(2):
        for j in range(N):
            if check[l][j]!=0 and check[l][j-1]!=0 and M[l][j] + M[l][j-1] <= W:
                check[l][j]=check[l][j-1]=0
            if l==0 and check[-1][j]!=0 and check[0][j]!=0 and M[-1][j] + M[0][j] <= W:
                check[-1][j]=check[0][j]=0
        print(check)
    print((2*N+sum(check[0])+sum(check[1]))//2)
# 다시!