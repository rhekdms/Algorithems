import sys
input = sys.stdin.readline
input()
A = set(map(int, input().split()))
input()
B = map(int,input().split())
for i in B:
    if i in A:
        print(1)
    else:
        print(0)