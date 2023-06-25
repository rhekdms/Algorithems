import sys
input=sys.stdin.readline
visit = []

def dfs(n,m):
    visit.append(G[n][m])
    for i in [[n-1,m],[n+1,m],[n,m-1],[n,m+1]]:
        if -1<i[0]<R and -1<i[1]<C:
            if G[i[0]][i[1]] not in visit:
                dfs(i[0],i[1])

R,C = map(int,input().split())
G = [list(map(str,input().strip())) for i in range(R)]
dfs(0,0)
print(visit)
#1987보류