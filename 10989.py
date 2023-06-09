import sys
input = sys.stdin.readline
N = int(input())
sol = [0]*10001
for i in range(N):
    sol[int(input())]+=1
for i in range(1,10001):
    for j in range(sol[i]):
        print(i)