import sys
input = sys.stdin.readline
N = int(input())
kids = list(int(input()) for i in range(N))

dp=[0]*N
for i in range(N):
    for j in range(i):
        if kids[j]<kids[i] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

print(N-max(dp))