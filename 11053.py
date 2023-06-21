import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
check = [0]*N
for i in range(N):
    for j in range(i):
        if A[j]<A[i] and check[i]<check[j]:
            check[i]=check[j]
    check[i]+=1

print(max(check))