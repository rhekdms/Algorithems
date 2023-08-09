import sys
input = sys.stdin.readline
A = list(sorted(int(input()) for i in range(5)))
while True:
    if len(A)==1:
        print(A[0])
        break
    if A[0] == A[1]:
        del A[0:2]
    else:
        print(A[0])
        break