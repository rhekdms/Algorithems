import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())

if a != 0 and b != 0 and d != 0 and e != 0:
    y = (c*d-f*a)/(b*d-e*a)
    x = (c-b*y)/a
    
elif a == 0 and b != 0 and d != 0 and e != 0:
    y = c/b
    x = (f-e*y)/d

elif a == 0 and b != 0 and d != 0 and e == 0:
    y = c/b
    x = f/d

elif a != 0 and b == 0 and d != 0 and e != 0:
    x = c/a
    y = (f-d*x)/e

elif a != 0 and b == 0 and d == 0 and e != 0:
    y = f/e
    x = c/a

elif a != 0 and b != 0 and d == 0 and e != 0:
    y = f/e
    x = (c-b*y)/a

elif a != 0 and b != 0 and d != 0 and e == 0:
    x = f/d
    y = (c-a*x)/b

print(int(x), int(y))