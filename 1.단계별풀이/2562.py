import sys
input = sys.stdin.readline
a = []
for i in range(1,10):
    a.append(int(input()))
print(max(a), a.index(max(a)) + 1, sep='\n')