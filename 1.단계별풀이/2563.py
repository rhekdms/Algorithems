import sys
input = sys.stdin.readline
a = [ [0] * 100 for i in range(100)]

N = int(input())

for k in range(N):
    c, b = map(int,input().split())
    for i in range(b,b+10):
        for j in range(c,c+10):
            a[i][j] = 1
            
count = 0
for n in range(100):
    count += sum(a[n])
print(count)