import sys
input=sys.stdin.readline
while True:
    S = input().rstrip()
    if S == '.':
        break
    else:
        string = []
        sol = 'yes'
        for j in S:
            if j=='(':
                string.append('(')
            elif j=='[':
                string.append('[')
            elif string and (j==']' or j==')'):
                if j==']' and '[' == string[-1]:
                    string.pop()
                elif j==')' and '(' == string[-1]:
                    string.pop()
                elif (j==']' and '[' != string[-1]) or (j==')' and '(' != string[-1]):
                    sol='no'
                    break
            elif not string and (j==']' or j==')'):
                sol='no'
                break
        if string:
            sol='no'
        print(sol)