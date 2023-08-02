import sys
input = sys.stdin.readline
N = int(input())
i = sorted([list(map(int,input().split())) for i in range(N)])
for j in i:
    print(*j)