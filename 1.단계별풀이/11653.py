import sys

N = int(sys.stdin.readline())
a = []
while N != 1:
    n = 2
    while N % n != 0:
        n += 1
    N /= n
    a.append(n)

for i in a:
    print(i)