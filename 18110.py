import sys
import math
input = sys.stdin.readline

def rounds(r):
    fr=int(r*10)%10
    if fr>4:
        return int(r)+1
    else:
        return int(r)

n = int(input())
if n == 0:
    print(0)

else:
    num = sorted(int(input()) for i in range(n))
    n = n*(15/100)
    n = rounds(n)
    num = num[n:len(num)-n]
    print(rounds(sum(num)/len(num)))