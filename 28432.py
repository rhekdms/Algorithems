import sys
input = sys.stdin.readline
S = [input().strip() for i in range(int(input()))]
M = int(input())
A = [input().strip() for i in range(M)]
Q = S.index('?')
for i in range(M):
    if (A[-1] in S) or (Q != 0 and S[Q-1][-1] != A[-1][0]) or ('?' != S[-1] and S[Q+1][0] != A[-1][-1]):
        A.pop()
        continue
    print(A[-1])
    break