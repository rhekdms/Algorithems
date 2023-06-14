import sys
input = sys.stdin.readline

N,K = map(int,input().split())

prime_num = [0]*(N+1)
cnt = 0
for i in range(2,N+1):
    if prime_num[i] == 0:
        j = 1
        while j*i < N:
            prime_num[j*i] = 1
            cnt+=1
            if cnt == K:
                print(i)
            j+=1