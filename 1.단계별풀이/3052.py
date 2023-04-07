import sys
input = sys.stdin.readline
a = []
for i in range(10):
    num = int(input().rstrip())
    num = num % 42
    a.append(num)
a = set(a)
print(len(a))