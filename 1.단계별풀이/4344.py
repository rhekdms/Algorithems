import sys
input = sys.stdin.readline
C = int(input())
for i in range(C):
    N = list(map(float,input().split()))
    S = sum(N[1:])/N[0]
    a = 0
    for j in N[1:]:
        if j>S:
            a += 1
    print(f'{(a/N[0])*100:0.3f}%')      # round = 소수점 밑이 0이면 n.0으로 나옴/ format도 있음
print()