import sys
input = sys.stdin.readline
n = int(input())
sol = {1:1,2:2}
def f(x):
    if x in sol:
        return sol[x]
    else:
        sol[x] = f(x-1)+f(x-2)
        return sol[x]

print(f(n)%10007)