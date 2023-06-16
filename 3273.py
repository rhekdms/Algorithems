import sys
input = sys.stdin.readline
n = int(input())-1
a = sorted(list(map(int,input().split())))
x = int(input())
l = 0
cnt = 0
while l != n:
    if a[l]+a[n]==x:
        cnt+=1
        l+=1
    elif a[l]+a[n]<x:
        l+=1
    else:
        n-=1
print(cnt)