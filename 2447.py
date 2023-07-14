import sys
N = int(sys.stdin.readline())
for i in range(N):
    for j in range(N):
        check=1
        for k in range(1,8):
            if 3**(k-1)<=i%(3**k)<2*(3**(k-1)) and 3**(k-1)<=j%(3**k)<2*(3**(k-1)):
                print(' ', end='')
                check=0
                break
        if check:
            print('*', end='')
    print()