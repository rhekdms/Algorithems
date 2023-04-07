import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int,input().split()))
c = int(input())
cnt = b.count(c)
print(cnt)