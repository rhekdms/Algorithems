import sys
import heapq
input = sys.stdin.readline
N, H, T = map(int,input().split())
G = []
for i in range(N):
    heapq.heappush(G, -(int(input())))
    
t = 0
check = 1

while check:
    if -G[0]<H or T==t:
        check=0
        break
    x = (-heapq.heappop(G))
    if x != 1 and H<=x:
        heapq.heappush(G,-(x//2))
        t+=1
    elif x == 1:
        heapq.heappush(G,-x)
        break
        
if -G[0]<H:
    print("YES")
    print(t)
else:
    print("NO")
    print(-G[0])