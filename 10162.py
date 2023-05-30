A = 5*60
B = 60
C = 10
T = int(input())
a = T//A
b = (T%A)//B
c = ((T%A)%B)//C
if ((T%A)%B)%C != 0:
    print(-1)
else:
    print(a,b,c)