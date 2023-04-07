import sys
input = sys.stdin.readline
v = input()
a = str(input().rstrip())
b = 0
for i in a:
    b += int(i)
print(b)