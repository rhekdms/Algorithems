import sys

while True:
    input = sys.stdin.readline
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif a > b:
        if a % b == 0:
            print('multiple')
        else:
            print('neither')
    else:
        if b % a == 0:
            print('factor')
        else:
            print('neither')