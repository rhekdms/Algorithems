import sys
input = sys.stdin.readline
input()
A = list(map(int,input().split()))
Q = int(input())
L = list(map(int,input().split()))
sol = [0]*Q
for i in range(Q):
    for j in A:
        if L[i]%j==0:
            L[i]//j