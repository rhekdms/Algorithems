import sys
input = sys.stdin.readline
N = int(input())
A = sorted([list(map(int,input().split())) for i in range(N)])
cnt = 0
a = [-1,-1]
for i in A:
    if a[1]<=i[0]:
        cnt+=1
        a = i
    elif a[0]<=i[0] and a[1]>i[1]:
        a = i
print(cnt)