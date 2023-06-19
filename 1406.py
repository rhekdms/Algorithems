import sys
input = sys.stdin.readline

N = list(input().strip())
N_R = []
for i in range(int(input())):
    M = input().rstrip()
    if M == 'L':
        if N:
            N_R.append(N.pop())
    elif M == 'D':
        if N_R:
            N.append(N_R.pop())
    elif M == 'B':
        if N:
            N.pop()
    else:
        N.append(M[-1])
print(*N,*N_R[::-1],sep='')