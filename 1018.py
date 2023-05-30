import sys
input = sys.stdin.readline
N, M = map(int,input().split())
board = [list(input()) for i in range(N)]
chess = 100
for i in range(N-8):
    cnt = 0
    for j in range(N):
        cnt += list(board[i,i+8]).count('B')-list(board[i,i+8]).count('W')
    if abs(cnt) < chess:
        chess = abs(cnt)
print(chess)