import sys
input = sys.stdin.readline
A,B = input().split()
k=0
sol = len(A)
for i in range(len(B)-len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if A[j]!=B[j+k]:
            cnt+=1
    sol=min(cnt,sol)
    k+=1
print(sol)