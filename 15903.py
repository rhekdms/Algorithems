import sys
import heapq
input = sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int,input().split()))
heapq.heapify(a)
for i in range(m):
    b = heapq.heappop(a)+heapq.heappop(a)
    heapq.heappush(a,b)
    heapq.heappush(a,b)
print(sum(a))