import sys
N = int(sys.stdin.readline())
for i in range(N):
    pw = input()
    if 6 <= len(pw) <= 9:
        print('yes')
    else:
        print('no')