import sys
input = sys.stdin.readline

N = int(input())
sol = 0
i = 0
while 9*(10**i)<N:
    N -= 9*(10**i)
    sol += 9*(10**i)*(i+1)
    i += 1
sol += N*(i+1)
print(sol)