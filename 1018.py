import sys
input = sys.stdin.readline
N, M = map(int,input().split())
board = list(input() for i in range(N))
W = 'WBWBWBWBBWBWBWBW'*4
B = 'BWBWBWBWWBWBWBWB'*4
cnt = 40
if board[0][0] == 'W':
    for i in range(N-8):
        for j in range(M-8):
            