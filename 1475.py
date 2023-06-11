import sys
input = sys.stdin.readline
N = list(map(int,input().strip()))
cnt = [0]*9
for i in range(10):
    if i == 9:
        cnt[6] = ((cnt[6]+N.count(i))//2)+((cnt[6]+N.count(i))%2)
    else:
        cnt[i] = N.count(i)
print(max(cnt))