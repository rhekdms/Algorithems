import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
n = []
for i in range(M, N+1):
    m = []
    for j in range(2, i+1):
        if i % j == 0:
            m.append(j)
    if m == [i]:
        n.append(i)
if len(n) != 0:
    print(sum(n))
    print(n[0])
else:
    print(-1)