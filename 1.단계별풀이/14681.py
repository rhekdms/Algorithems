import sys
input = sys.stdin.readline
x = int(input())
y = int(input())
if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
elif x>0 and y<0:
    print(4)
'''
x>0, y>0 1
x>0, y<0 4
x<0, y>0 2
x<0, y<0 3
'''