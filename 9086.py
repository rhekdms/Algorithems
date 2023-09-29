N = int(input())
A = []
for i in range(N):
    A.append(input())
for i in range(N):
    print(A[i][0],A[i][-1],sep='')