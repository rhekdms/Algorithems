import sys
a, b, c = map(int,sys.stdin.readline().split())
Triangle = [a,b,c]
if sum(Triangle) > 2*max(Triangle):
    print(sum(Triangle))
else:
    del Triangle[Triangle.index(max(Triangle))]
    print(2*sum(Triangle)-1)