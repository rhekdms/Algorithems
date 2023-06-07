import sys
input = sys.stdin.readline

sol = {1:0,2:1,3:1}
def one(n):
    if n in sol:
        return sol[n]
    elif n % 6 == 0:
        sol[n] = min(one(n/2),one(n/3))+1
        return sol[n]
    elif n % 3 == 0:
        sol[n] = min(one(n-1),one(n/3))+1
        return sol[n]
    elif n % 2 == 0:
        sol[n] = min(one(n-1),one(n/2))+1
        return sol[n]
    else:
        sol[n] = one(n-1)+1
        return sol[n]

while True:
    n = int(input())
    print(one(n))

'''
1-> 0
[2-> 1]
(3-> 1)
[4-> 2]
5-> 3
{6-> 2}
7-> 3
[8-> 3]
(9-> 2)
10-> 3
11-> 4
{12-> 3}
13-> 4
14-> 4
15-> 4
[16-> 4]
17-> 5
{18-> 3}
19-> 4
20-> 4
21-> 4
22-> 5
'''