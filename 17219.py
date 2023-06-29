import sys
input = sys.stdin.readline
N,M = map(int, input().split())
A = dict([(map(str,input().split())) for i in range(N)])
for i in range(M):
    sol = input().rstrip()
    print(A[sol])