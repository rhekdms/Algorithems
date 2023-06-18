import sys
input = sys.stdin.readline

N = list(input().strip())
cuser = len(N)
for i in range(int(input())):
    M = input().rstrip()
    if M == 'L':
        if cuser == 0:
            pass
        else:
            cuser -= 1
    elif M == 'D':
        if cuser == len(N):
            pass
        else:
            cuser += 1
    elif M == 'B':
        if cuser == 0:
            pass
        else:
            del N[cuser-1]
            cuser -= 1
    else:
        N.insert(cuser,list(M.split())[1])
        cuser += 1
print(*N,sep='')
'''
L = move left
D = move right
B = delete -1
P = insert 1
나중에 다시!
'''