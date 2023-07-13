import sys
input = sys.stdin.readline
N,r,c = map(int,input().split())
sol = [0, ((2**N)**2)-1]
i = (2**N)**2//2
k = 2**(N-1)
while sol[0]!=sol[-1]:
    if r < k:
        sol[-1] -= i
    else:
        sol[0] += i
        r-=k
    i //= 2
    if c < k:
        sol[-1] -= i
    else:
        c-=k
        sol[0] += i
    i //= 2
    k //= 2
print(sol[0])