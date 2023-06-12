import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().split()))
a = 0
for i in range(1,N):
    if sum(num[i-1:i+1])>num[i]:
        num[i]=sum(num[i-1:i+1])
    else:
        a = i
        
print(max(num))