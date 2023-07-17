import sys
N = int(sys.stdin.readline())
def f(x):
    if x == 3:
        return [['*','*','*'],['*',' ','*'],['*','*','*']]
    else:
        return [sum(i,[]) for i in zip(f(x//3),f(x//3),f(x//3))]+[sum(k,[]) for k in zip(f(x//3),[[' ' for i in range(x//3)] for j in range(x//3)],f(x//3))]+[sum(i,[]) for i in zip(f(x//3),f(x//3),f(x//3))]
for i in f(N):
    print(*i,sep='')