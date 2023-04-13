import sys
input = sys.stdin.readline
N = int(input())
for a in range(N):
    b = input().strip()
    c = list(set(b))
    count = 0
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            del b[i]
    if b == c:
        count += 1
print(N)
# 모르겠다