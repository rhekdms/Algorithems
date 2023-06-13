N,K = map(int,input().split())
fac = [1]
if K==0 or N==K:
    print(1)
else:
    for i in range(1, N+1):
        fac.append(fac[i-1]*i)
    print((fac[N]//(fac[K]*fac[N-K]))%10007)