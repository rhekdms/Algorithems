T = int(input())
for i in range(T):
    a = input().split()
    num = 0
    for j in a:
        if j == '%':
            num += 5
        elif j == '#':
            num -= 7
        elif j == '@':
            num *= 3
        else:
            num += float(j)
    print(f"{num:.2f}")