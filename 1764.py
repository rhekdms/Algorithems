import sys
input = sys.stdin.readline
N,M = map(int, input().split())
D = set(input() for i in range(N))
B = set(input() for i in range(M))
for i in B:
    if i not in D:
        B.remove(i)

print(len(B))
for i in sorted(B):
    print(i,end='')