import sys
from math import ceil
input = sys.stdin.readline
N = int(input())
sol = 0
pizza = {'1/4':0, '1/2':0, '3/4':0}
for i in range(N):
    a = input().strip()
    pizza[a]+=1
