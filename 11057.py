N = int(input())
G = [1]*10
for j in range(1,N):
    for i in range(1,10):
        G[i]+=G[i-1]
print(sum(G)%10007)