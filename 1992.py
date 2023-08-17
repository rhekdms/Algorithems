import sys
input = sys.stdin.readline
N = int(input())
A = ''
for i in range(N):
    A += input().strip()
A = list(map(int,A))
def f(x,*args):
    if 1 not in args:
        return 0
    if 0 not in args:
        return 1
    a = [[],[],[],[]]
    for i in range(x**2):
        if i//x < x//2:
            if i%x < x//2:
                a[0].append(args[i])
            else:
                a[1].append(args[i])
        elif i%x < x//2:
                a[2].append(args[i])
        else:
            a[3].append(args[i])
    return f'({f(x//2,*a[0])}{f(x//2,*a[1])}{f(x//2,*a[2])}{f(x//2,*a[3])})'
                
print(f(N,*A))