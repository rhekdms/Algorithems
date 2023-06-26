import sys
input = sys.stdin.readline
N = int(input())
num = [[0,1,1,1,1,1,1,1,1,1],[0]*10]
for i in range(1,N):
    num[i%2][0]=num[i%2-1][1]
    num[i%2][9]=num[i%2-1][8]
    for j in range(1,9):
        num[i%2][j]=num[i%2-1][j-1]+num[i%2-1][j+1]
print(sum(num[N%2-1])%1000000000)