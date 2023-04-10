import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    for j in range(N):
        if i + j >= N - 1:
            print('*', sep='', end='')
        else:
            print(' ', sep='', end='')
    print()

'''
 01234 j
0    *
1   **
2  ***
3 ****
4*****

'''