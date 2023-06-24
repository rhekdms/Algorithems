import sys
input = sys.stdin.readline
n = int(input())
step = [int(input()) for i in range(n)]
check = [1]*n
sol = [0]*n
sol[-1] = step[-1]
for i in range(n-1,0,-1):
    if check[i]:
        if sol[i-1]<step[i-1]+sol[i] and not(i==2 and sol[i-1]+step[0]>step[i-1]+sol[i]):
            sol[i-1] = step[i-1]+sol[i]
            check[i-1] = 0
            print(sol)
    if sol[i-2]<step[i-2]+sol[i]:
        sol[i-2] = step[i-2]+sol[i]
        print(sol)
print(max(sol[:2]))
# 다시!!