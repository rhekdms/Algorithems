import sys
input = sys.stdin.readline
N = int(input())
string = [[] for i in range(51)]
for i in range(N):
    a = input().strip()
    string[len(a)].append(a)
for i in string:
    if i:
        print(*sorted(list(set(i))),sep='\n')