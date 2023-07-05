import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
a = list(map(int,a))
b = list(map(int,b))
a_1 = a + [0]*(len(b))
a_2 = [0]*(len(b)) + a + [0]*(len(b))
solution = len(a_2)
k=0
for i in range(len(b)):
    sol = [i for i in a_2[len(b)+k:len(a)+len(b)+k] if i != 0]
    for j in range(len(b)):
        sol.append(a_2[j+k]+b[j])
    if 4 not in sol and len(sol)<solution:
        solution=len(sol)
    k+=1
    
i = 0
while i<=len(a):
    sol = a_1[:i]
    for j in range(len(b)):
        if b[j]+a_1[j+i]<=3:
            sol.append(b[j]+a_1[j+i])
        else:
            i+=1
            break
    if len(sol) == i+len(b):
        print(min(max(len(a),len(sol)),solution))
        break