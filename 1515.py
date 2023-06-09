import sys
input = sys.stdin.readline

N = input().strip()

sol = 1
N_num = 0

while N_num < len(N):
    string_sol = str(sol)
    check = 1
    for i in string_sol:
        if N_num >= len(N):
            break
        elif N[N_num] == i:
            N_num += 1
        if i == string_sol[-1]:
            check = 0
    if check == 0:
        sol += 1
        
if check == 0:
    sol -= 1
    
print(sol)