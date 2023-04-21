import sys
x, y, w, h = map(int,sys.stdin.readline().split())
if h-y < x and h-y < y and h-y < w-x:
    print(h-y)
elif w-x < x and w-x < y and w-x < h-y:
    print(w-x)
elif x < w-x and x < y and x < h-y:
    print(x)
else:
    print(y)
'''
x,y는 점, w,h는 직사각형
'''