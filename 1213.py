import sys
input = sys.stdin.readline
start = list(map(str,input().strip()))
A = sorted(start)
sol = []
i = 0
while i <= len(start)//2 and len(A) > 1:
    if A[1] == A[0]:
        sol.append(A[0])
        del A[0:2]
        i+=1
    elif len(A)>2:
        if A[0] != A[1] !=A[2]:
            print("I'm Sorry Hansoo")
            i = -1
            break
        else:
            sol.append(A[1])
            del A[1:3]
            i+=1
    else:
        print("I'm Sorry Hansoo")
        i = -1
        break
        
if i != -1:
    print(*(sol+A+sol[::-1]),sep='')