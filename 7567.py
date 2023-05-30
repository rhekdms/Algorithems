a = input()
n = 10
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        n += 5
    else:
        n += 10
print(n)