import sys
input = sys.stdin.readline
A = list(map(str,input().strip()))
B = list(map(str,input().strip()))
cnt = 0
for i in range(min(len(A),len(B))):
    if A[i]==B[i]:
        cnt+=1
print(max(len(A),len(B))-cnt) 
# 다시!