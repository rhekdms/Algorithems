N,M = map(int,input().split())
S = []
A = []
cnt = 0
for i in range(N):
    S.append(input())
for i in range(M):
    A.append(input())
for i in S:
    cnt+=A.count(i)
print(cnt)