import sys
input = sys.stdin.readline
sol = {1:1,2:1}
def f(x):
    if x in sol:
        return sol[x]
    else:
        sol[x] = f(x-1) + f(x-2)
        return(sol[x])
N = int(input())
print(f(N))