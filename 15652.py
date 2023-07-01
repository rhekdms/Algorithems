import sys
input = sys.stdin.readline
N, M = map(int,input().split())
sol=[0 for i in range(M)]

def f(set,x):
    for i in range(x,N+1):
        sol[set]=i
        if set==M-1:
            print(*sol)
        else:
            f(set+1,i)
        if sol == [[N] for i in range(M)]:
            return

f(0,1)