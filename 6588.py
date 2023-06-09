import sys
input = sys.stdin.readline

prime_num = [0,0]+[1]*(10**6)

for i in range(2,10**6):
    if prime_num[i]:
        for j in range(i*2,10**6+1,i):
            prime_num[j]=0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        for i in range(3,n//2+1,2):
            if prime_num[i] and prime_num[n-i]:
                print(f"{n} = {i} + {n-i}")
                break