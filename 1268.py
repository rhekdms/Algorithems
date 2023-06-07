import sys
input = sys.stdin.readline

N = int(input().strip())
scl = [list(map(int,input().split())) for i in range(N)]
s_class = [0]*N

for i in range(N):
    p = [0]*N
    for j in range(5):
        for k in range(N):
            if p[k]==0 and scl[i][j] == scl[k][j]:
                p[k]+=1
    s_class[i]+=sum(p)
print(s_class.index(max(s_class))+1)