import sys
N = list(map(int,sys.stdin.readline().split()))
for i in N:
    N[N.index(i)] = i**2
print(sum(N) % 10)