import sys
input = sys.stdin.readline
n = list(range(1,31))
while True:
    try:
        del n[n.index(int(input()))]
    except:
        for n in n:
            print(n)
        break