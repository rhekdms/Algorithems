S = input()
a = ''
n = 0
def sol(x,a,n):
    if S[x] == ' ':
        n = len[a]
        a += ' '
        return sol(n,a,n)
    elif S[x] == '<':
        i = x
        while True:
            i+=1
            if S[i]==">":
                break
        a += S[x:i+1]
        n = i+1
        if i+1 == len(S):
            return
        else:
            return sol(n,a,n)
    else:
        a[n] += S[x]
        if n+1 == len(S):
            return
        else:
            return sol(n+1,a,n)
sol(n,a,n)
print(a)