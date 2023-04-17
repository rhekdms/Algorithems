import sys
input = sys.stdin.readline
a = [list(map(int,input().split())) for i in range(9)]
b = 0
row, col = 1, 1
for j in range(9):
    if max(a[j]) > b:
        b = max(a[j])
        row = j + 1
        col = a[j].index(b) + 1
        
print(b)
print(row, col)