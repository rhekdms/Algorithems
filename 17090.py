import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N,M = map(int,input().split())
map = [input().rstrip() for i in range(N)]
check = [[0]*M for i in range(N)]
def f(n,m):
    if n+1<N and not check[n+1][m] and map[n+1][m]=='U':
        check[n+1][m]=1
        f(n+1,m)
    if n!=0 and check[n-1][m]==0 and map[n-1][m]=='D':
        check[n-1][m]=1
        f(n-1,m)
    if m+1<M and not check[n][m+1] and map[n][m+1]=='L':
        check[n][m+1]=1
        f(n,m+1)
    if m!=0 and not check[n][m-1] and map[n][m-1]=='R':
        check[n][m-1]=1
        f(n,m-1)
    return
for i in range(M):
    if not check[0][i] and map[0][i]=='U':
        check[0][i]=1
        f(0,i)
    if not check[-1][i] and map[-1][i]=='D':
        check[-1][i]=1
        f(N-1,i)
for i in range(N):
    if not check[i][0] and map[i][0]=='L':
        check[i][0]=1
        f(i,0)
    if not check[i][-1] and map[i][-1]=='R':
        check[i][-1]=1
        f(i,M-1)
cnt=0
for i in check:
    cnt+=i.count(1)
print(cnt)