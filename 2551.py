import sys
from math import ceil
input = sys.stdin.readline
N = int(input())
num = tuple(sorted(map(int,input().split())))
print(num[ceil(N/2)-1], (sum(num)//N if sum(num)/N<=sum(num)//N+0.5 else sum(num)//N+1))