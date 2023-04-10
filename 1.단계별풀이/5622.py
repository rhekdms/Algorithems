arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO','PQRS','TUV','WXYZ']
call = input()
minute = 0
for i in arr:
    for j in call:
        if j in i:
            minute += (arr.index(i)+3)
print(minute)