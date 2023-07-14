import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    S = input().strip()
    if S==S[::-1]:
        print(0)
    else:
        check = 1
        for i in range(len(S)):
            if i==0 and S[1:]==S[len(S)-1:0:-1]:
                print(1)
                check = 0
                break
            elif S[:i]+S[i+1:]==S[len(S)-1:i:-1]+S[i-1::-1]:
                print(1)
                check = 0
                break
        if check:
            print(2)