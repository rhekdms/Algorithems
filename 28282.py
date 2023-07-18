import sys
input = sys.stdin.readline
X,K = map(int,input().split())
A = list(map(int,input().split()))
print(sum(A[:X].count(i)*(X-A[X:].count(i)) for i in range(1,K+1)))