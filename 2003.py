import sys
input = sys.stdin.readline
N,M = map(int, input().split())
A = list(map(int,input().split()))
i = 0
j = 1
cnt = 0
while i<j:
    if sum(A[i:])<M:
        break
    elif sum(A[i:j])>M:
        if i+1 == j:
            j+=1
        i += 1
    elif sum(A[i:j])==M:
        cnt += 1
        i += 1
        j += 1
    else:
        j += 1
print(cnt)