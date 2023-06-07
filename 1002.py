import sys
input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    line = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    if line == 0 and r1 == 0 and r2 == 0:
        print(1)
    elif line == 0 and r1 == r2:
        print(-1)
    elif line < abs(r2-r1) or line > r1+r2:
        print(0)
    elif line == r1+r2 or line == abs(r2-r1) :
        print(1)
    else:
        print(2)