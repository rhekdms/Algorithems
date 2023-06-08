import sys
input = sys.stdin.readline

prime_num = [0,0,1]+[1,0]*(10**7//2)

for i in range(3,10**7):
    if prime_num[i]:
        for j in range(i*2,10**7+1,i):
            prime_num[j]=0

while True:
    n = int(input().strip())
    if n == 0:
        break
    elif n % 2 == 1:
        print("Goldbach's conjecture is wrong.")
    else:
        for i in range(2,n):
            if prime_num[i] and prime_num[n-i]:
                print(f"{n} = {i} + {n-i}")
                break