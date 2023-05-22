import sys
input = sys.stdin.readline

N = int(input())
box = 0
while True:
    if N % 5 != 0:
        N -= 3
        box += 1
        if N == 0:
            break
        elif N < 0:
            box = -1
            break
    else:
        box += N // 5
        break
print(box)