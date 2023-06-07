import sys
input = sys.stdin.readline

N = list(map(int,input().strip()))
i = 0
for k in range(1, len(N)):
    a = 1
    b = 1
    for j in N[:k]:
        a *= j
    for l in N[k:]:
        b *= l
    if a == b:
        i = 1
        print('YES')
        break
if i == 0:
    print("NO")