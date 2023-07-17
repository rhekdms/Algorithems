import sys
input = sys.stdin.readline
N = int(input())
num = [list(map(int,input().split())) for i in range(N)]
sol = {-1:0, 0:0, 1:0}
def f(n):
    a = []
    for i in n:
        a += [*i]
    if -1 in a and 0 not in a and 1 not in a:
        sol[-1]+=1
        return
    elif 0 in a and -1 not in a and 1 not in a:
        sol[0]+=1
        return
    elif 1 in a and 0 not in a and -1 not in a:
        sol[1]+=1
        return
    else:
        l = len(n)//3
        for i in range(1,4):
            for j in range(1,4):
                f([k[(j-1)*l:j*l] for k in n[(i-1)*l:i*l]])
        return
f(num)
print(sol[-1],sol[0],sol[1],sep='\n')