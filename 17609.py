import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    S = input().strip()
    R = len(S)-1
    L = 0
    sol = 0
    while R>L and sol<2:
        if S[R]==S[L]:
            R-=1
            L+=1
        else:
            if S[L+1]==S[R]:
                R-=1
                L+=2
                sol+=1
            elif S[L]==S[R-1]:
                R-=2
                L+=1
                sol+=1
            else:
                sol = 2
    print(sol)