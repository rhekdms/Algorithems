import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
if a+b+c != 180:
    print('Error')
elif a == b == c:
    print('Equilateral')
elif a == b or b == c or c == a:
    print('Isosceles')
else:
    print('Scalene')