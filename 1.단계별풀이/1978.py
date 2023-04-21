import sys

N = int(sys.stdin.readline())
a = list(map(int,input().split()))
n = 0
for i in a:
    m = []
    for j in range(2,i+1):
        if i % j == 0:
            m.append(j)
        if m == [i]:
            n += 1
print(n)