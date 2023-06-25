sol = [0,1]
def f(x):
    if x<len(sol):
        return sol[x]
    else:
        sol.append(f(x-1)+f(x-2))
        return sol[x]
    
K = int(input())
f(K)
print(*sol[-2:])