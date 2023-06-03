import sys
input = sys.stdin.readline
N, M = map(int,input().split())
board = list(input() for i in range(N))
W = [('WBWBWBWB','BWBWBWBW')*4]
B = [('BWBWBWBW','WBWBWBWB')*4]
cnt = 40
