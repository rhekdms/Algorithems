import sys
input = sys.stdin.readline
A, B = input().split()
A, B = int(A[::-1]), int(B[::-1])
a = [A, B]
print(max(a))