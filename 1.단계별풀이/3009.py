import sys
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
c = list(map(int,sys.stdin.readline().split()))
if a[0] == b[0]:
    dx = c[0]
elif b[0] == c[0]:
    dx = a[0]
else:
    dx = b[0]

if a[1] == b[1]:
    dy = c[1]
elif b[1] == c[1]:
    dy = a[1]
else:
    dy = b[1]

print(dx, dy)