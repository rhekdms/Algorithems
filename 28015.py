import sys
input = sys.stdin.readline
N,M = map(int,input().split())
draw = [list(map(int,input().split())) for i in range(N)]
cnt = 0
for i in draw:
    t = 0
    k = {}
    for j in range(len(i)):
        if i[j]==0:
            k[t]=(i[t:j])
            t=j+1
    k[t]=i[t:]
    t=0
    for j in k.values():
        num = [0,0]
        if j:
            for r in range(len(j)-1):
                if j[r]!=j[r+1]:
                    num[t%2]+=1
                    t+=1
            num[t%2]+=1
            cnt=cnt+1+(min(num))
print(cnt)