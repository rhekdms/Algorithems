import sys
input = sys.stdin.readline

N,K = map(int,input().split())

A = [1]+[0]*N

for i in range(K):
    for j in range(1,N+1):
        A[j]= A[j]+A[j-1]

print(A[N]%1000000000)