T = int(input())
for i in range(T):
    N = int(input())
    n = str(N**2)
    if n[-len(str(N)):] == str(N):
        print('YES')
    else:
        print("NO")