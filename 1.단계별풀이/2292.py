import sys
input = sys.stdin.readline
N = int(input())
i = 1
j = 0
if N == 1:
    print(1)
else:
    while N>i:
        i += 6 * j
        j += 1
    print(j)
'''
0 1 1
1 7 2
2 19 3
3 37 4
4 61 5
5 91 6

1      1
2~7    6
8~19   12
20~37  18
38~61  24
62~    30
'''