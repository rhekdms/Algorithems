A, B, C = map(int,input().split())
D = int(input())

if C+D>=60:
    second = (C+D)%60
    B += ((C+D)//60)
else:
    second = C+D
if B>=60:
    minute = B%60
    A += (B//60)
else:
    minute = B
if A>=24:
    hour = A%24
else:
    hour = A
print(hour, minute, second)