import sys
input=sys.stdin.readline
T = int(input())
for i in range(T):
    S = list(map(str,input().strip()))
    string = []
    sol = 'YES'
    for j in S:
        if j=='(':
            string.append('(')
        elif '(' in string:
            string.pop()
        else:
            sol='NO'
            break
    if string:
        sol='NO'
    print(sol)