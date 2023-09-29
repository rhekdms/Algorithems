import sys
import heapq
input = sys.stdin.readline

# 입력
N,K = map(int,input().split())
A = []
for i in range(N):
    a = list(map(int,input().split()))
    heapq.heappush(A,(-a[1],a[0]))
B = [int(input()) for i in range(K)]
heapq.heapify(B)

# 계산
sol = 0
while A:
    a = heapq.heappop(A)
    for j in range(len(B)):
        if a[1] <= B[j]:
            sol -= a[0]
            del B[j]
            break

print(sol)