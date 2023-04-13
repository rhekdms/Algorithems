import sys
input = sys.stdin.readline
a = input().strip()
c = 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='
for i in c:
    a = a.replace(i,'*')
print(len(a))