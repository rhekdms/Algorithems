import sys
input = sys.stdin.readline
a = [list(map(str,input().rstrip)) for i in range(5)]
c = ''
for i in range(15):
    for j in range(5):
        try:
            c += a[j][i]
        except:
            continue
print(c)