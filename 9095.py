import sys
input = sys.stdin.readline
T = int(input())
s = {1:1,2:2,3:4}
def f(x):
    if x in s:
        pass
    else:
        s[x] = f(x-3)+f(x-2)+f(x-1)
    return s[x]

for i in range(T):
    n = int(input())
    if n == 1 or n == 2 or n == 3:
        print(s[n]-1)
    else:
        print(f(n))