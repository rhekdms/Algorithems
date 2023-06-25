import sys
from string import ascii_uppercase
input = sys.stdin.readline
a = input()
english = ascii_uppercase
for i in a:
    if i in english:
        print(i,end='')