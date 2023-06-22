import sys
input = sys.stdin.readline
N = int(input())
sol = [[] for i in range(201)]
for i in range(N):
    a,b = input().split()
    sol[int(a)]+=[b]
for i in range(201):
    for j in sol[i]:
        print(i,j)