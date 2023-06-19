import sys
input = sys.stdin.readline
N = int(input())
kids = [0]+list(int(input()) for i in range(N))+[N+1]
