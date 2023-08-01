import sys
input = sys.stdin.readline
chess = tuple(['WBWBWBWB','BWBWBWBW']*4)
N,M = map(int,input().split())
board = tuple(input().strip() for i in range(N))
sol = 32
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if chess[k][l]!=board[k+i][l+j]:
                    cnt+=1
        sol = min(sol,cnt,64-cnt)
print(sol)