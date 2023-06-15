import sys
input = sys.stdin.readline
N = int(input())
A = list(list(map(int,input().split())))
sol = []
for i in range(N-1):
    for j in range(i+1,N):
        if A[i]+A[j] in A and A[i]+A[j] not in sol:
            sol.append(A[i]+A[j])
print(len(sol))