import sys
while True:
    a = sys.stdin.readline().lower()
    n = 0
    if a == '#':
        break
    n += a.count('a')
    n += a.count('i')
    n += a.count('u')
    n += a.count('e')
    n += a.count('o')
    print(n)