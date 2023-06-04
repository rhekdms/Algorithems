S = input()
a = 0
for i in range(1,len(S)):
    if S[i] != S[i-1]:
        a += 1
print((a//2)+(a%2))