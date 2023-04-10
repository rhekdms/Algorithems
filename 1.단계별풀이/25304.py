import sys
input = sys.stdin.readline
X = int(input())
N = int(input())
price = 0
for i in range (N):
    A, B = map(int,input().split())
    price = price + A * B
if X == price:
    print('Yes')
else:
    print('No')