import sys
input = sys.stdin.readline
N = int(input())
line = int(input())
net = [[] for i in range(N+1)]
for i in range(line):
    a,b = map(int,input().split())
    net[a].append(b)
    net[b].append(a)
visit = []
def f(v):
    visit.append(v)
    for i in net[v]:
        if i not in visit:
            f(i)
f(1)
print(len(visit)-1)