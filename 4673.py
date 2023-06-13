num = [i for i in range(1,10001)]
for i in range(1,10001):
    if i + sum(list(map(int,str(i)))) in num:
        num.remove(i + sum(list(map(int,str(i)))))
    if i in num:
        print(i)