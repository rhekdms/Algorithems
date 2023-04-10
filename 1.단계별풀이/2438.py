import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    for j in range(N):
        if i>=j:
            print('*', sep='', end='')
    print()