import sys
input = sys.stdin.readline

N = int(input())
box = list(map(int,input().split()))
check = [0]*N
i = 1
while check.count(i-1)>1:
    for j in range(check.index(i-1),N):
        if check[j] == i-1:
            for k in range(j,N):
                if box[j]<box[k]:
                    check[k]=i
    i+=1
print(max(check)+1)