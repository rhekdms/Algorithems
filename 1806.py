import sys
input=sys.stdin.readline
N,S = map(int,input().split())
num = list(map(int,input().split()))
L=0
R=1
sol = N
for i in num:
    if S <= i:
        print(1)
        sol = 0
        break
if sol != 0:
    if sum(num)<S:
        print(0)
    else:
        plus=num[0]
        while L<N:
            if plus<S and R<N:
                plus+=num[R]
                R+=1
            else:
                if sol>R-L and plus>=S:
                    sol=R-L
                plus-=num[L]
                L+=1   
        print(sol)