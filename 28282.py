import sys
input = sys.stdin.readline
X,K = map(int,input().split())
A = [{i:0 for i in range(1,K+1)},{i:X for i in range(1,K+1)}]
j = 1
for i in list(map(int,input().split())):
    if j > X:
        A[1][i]-=1
    else:
        A[0][i]+=1
    j+=1
sol = 0
for key,value in A[0].items():
    sol+=A[1][key]*value
print(sol)