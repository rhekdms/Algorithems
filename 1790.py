import sys
input = sys.stdin.readline

N, k = map(int,input().split())
sol = 1
N_num = 0

a = 0
b = 0
while 9*(10**b)<N:
    N -= 9*(10**b)
    a += 9*(10**b)*(b+1)
    b += 1
a += N*(b+1)

if k > a:
    print(-1)
elif k < 10:
    print(k)
else:
    i = 0
    while k > int(str(i)+"8"*i+'9'):
        i+=1
    keep = (k-int(str(i-1)+"8"*(i-1)+'9'))
    sol = str((10**i)+int((keep-0.5)//(i+1)))
    print(sol[keep%(i+1)-1])