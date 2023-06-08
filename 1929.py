import sys
input = sys.stdin.readline

M,N = map(int,input().split())

prime_num = [1,0]*(N//2+2)
prime_num[1] = 1
prime_num[2] = 0

for i in range(2,N+1):
    if prime_num[i] == 0:
        j = 1
        while i != 2 and j*i <= N:
            prime_num[j*i] = 1
            j+=1
        if i>=M:
            print(i)