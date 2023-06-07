import sys
import string

input = sys.stdin.readline

input()
n = list(input().strip())
s = '0'
sol = 0
for i in n:
    if i in string.ascii_letters:
        sol += int(s)
        s = '0'
    else:
        s += i
sol += int(s)
print(sol)