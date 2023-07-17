import sys
N = int(sys.stdin.readline())
def f(x):
    if x == 3:
        return ['***','* *','***']
    else:
        return [zip(f(x//3),f(x//3),f(x//3)), zip(f(x//3),[' '*(x//3) for i in range(x//3)],f(x//3)), zip(f(x//3),f(x//3),f(x//3))]