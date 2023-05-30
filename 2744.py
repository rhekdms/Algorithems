import sys
a = input()
mini = 'abcdefghijklmnopqrstuvwxyz'
for i in a:
    if i in mini:
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')