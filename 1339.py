import sys
input = sys.stdin.readline
N = int(input())
S = [input().strip() for i in range(N)]
s = [[] for i in range(8)]
for j in range(-1,-9,-1):
    for k in S:
        try:
            s[j].append(k[j])
        except:
            pass
s = s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7]

num = {}
j = 9
for i in s:
    if i not in num:
        num[i]=str(j)
        j-=1
        
sol = 0
for i in S:
    for key,value in num.items():
        i = i.replace(key,value)
    sol+=int(i)
print(sol)