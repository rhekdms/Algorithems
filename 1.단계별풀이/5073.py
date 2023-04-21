import sys
while True:
    Triangle = list(map(int,sys.stdin.readline().split()))
    if Triangle[0] == Triangle[1] == Triangle[2] == 0:
        break
    if 2*max(Triangle) >= sum(Triangle):
        print('Invalid')
    elif Triangle[0] == Triangle[1] == Triangle[2] :
        print('Equilateral ')
    elif Triangle[0] == Triangle[1] or Triangle[1] == Triangle[2] or Triangle[2] == Triangle[0]:
        print('Isosceles')
    else:
        print('Scalene')