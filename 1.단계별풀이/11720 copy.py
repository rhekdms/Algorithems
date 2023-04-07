import sys
input = sys.stdin.readline
a = str(input().rstrip())
b = []
for i in a:
    b.append(int(i))
print(sum(b))