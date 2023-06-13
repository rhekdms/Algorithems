chess = [[True,False]*4,[False,True]*4]
H = [list(input()) for i in range(8)]
cnt = 0
for i in range(64):
    if chess[(i//8)%2][i%8] and H[i//8][i%8] == 'F':
        cnt += 1
print(cnt)