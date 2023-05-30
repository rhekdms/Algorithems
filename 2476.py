N = int(input())
first = 0
for i in range(N):
    a = list(map(int,input().split()))
    if a[0] == a[1] == a[2]:
        if 10000+a[0]*1000 > first:
            first = 10000+a[0]*1000
    elif a[0] != a[1] != a[2] != a[0]:
        if max(a)*100 > first:
            first = max(a)*100
    else:
        if a[1]==a[0] or a[0]==a[2]:
            if 1000+a[0]*100 > first:
                first = 1000+a[0]*100
        else:
            if 1000+a[1]*100 > first:
                first = 1000+a[1]*100
print(first)