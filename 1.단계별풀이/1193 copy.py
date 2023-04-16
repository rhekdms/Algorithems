import sys
input = sys.stdin.readline
X = int(input())
for x in range(X):
    i += 1
    j -= 1
    if j == 0:
        i = 1
        k += 1
        j = k
if k % 2 == 0:
    print(f'{i}/{j}')
else:
    print(f'{j}/{i}')

'''
k=1

'''