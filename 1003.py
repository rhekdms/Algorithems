import sys
input = sys.stdin.readline
T = int(input())

a = {0:[1,0],1:[0,1]}

def f(x):
    if x in a:
        return a[x]
    else:
        a[x] = [k+j for k,j in zip(f(x-1),f(x-2))]
        return a[x]

for i in range(T):
    sol = f(int(input()))
    print(*sol)