import sys
input = sys.stdin.readline
N,M = map(int,input().split())
num = [0]
for i in tuple(map(int,input().split())):
    if num:
        num.append(num[-1]+i)
    
for k in range(M):
    i,j = map(int,input().split())
    print(num[j]-num[i-1])