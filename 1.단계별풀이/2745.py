import sys
input = sys.stdin.readline
N, B = input().split()
n = []
for i in N:
    n += i
B = int(B)
english = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
for j in range(len(n)):
    if n[j] in english:
        n[j] = 10 + english.index(n[j])
b = 0
for k in range(len(n)):
    b = b + (B ** k) * int(n[-1-k])
print(b)
# N에 들어있는 영어를 숫자로 변환
# B진법을 10진법으로 변환((B**range(len(N))*N[range(len(N))])