import sys
from math import gcd
input = sys.stdin.readline
A,B = map(int,input().split())
print('1'*gcd(A,B))