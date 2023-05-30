import sys
a = []
for i in range(5):
    a += [int(sys.stdin.readline())]
print(sum(a))