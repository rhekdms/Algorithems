import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = sorted(list(int(input()) for i in range(n)))
cnt = 0

sol = [[[0,0] for _ in range(k)], [[0,0] for _ in range(k)]]
for i in coin:
    sol[0][-1] = [i,0]

i = 0
while n-(i*min(coin))>=0:
    for j in range((1+i)*min(coin),n+1):
        if sol[i%2][-j][0]!=0 and sol[i%2][-j][1]==i:
            for l in coin[coin.index(sol[i%2][-j][0]):]:
                sol[(i+1)%2][-j-l]=[l,i+1]
    i+=1
    if sol[i%2][0][0]:
        cnt+=1
        sol[i%2][0]=[0,0]

print(cnt)