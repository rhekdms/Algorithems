import sys
input = sys.stdin.readline
T = int(input())
for T in range(T):
    R, S = input().split()
    a = ''
    for i in S:
        a += int(R) * i
    print(a)