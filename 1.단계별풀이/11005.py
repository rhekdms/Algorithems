import sys
input = sys.stdin.readline
english = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
N, B = map(int,input().split())
b = []
while N >= B:
    if N % B >= 10:
        b += english[(N%B)-10]
    else:
        b += str(N % B)
    N //= B
if N >= 10:
    b += english[N-10]
else:
    b += str(N)
for i in b[::-1]:
    print(i, end='')