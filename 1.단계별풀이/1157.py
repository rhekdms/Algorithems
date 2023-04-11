import sys
input = sys.stdin.readline
english = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
a = input().upper()
c = 0
for i in english:
    b = a.count(i)
    if c < b:
        c = b
        d = i
    elif c == b:
        d = '?'
print(d)
'''
1. a-셋a=>가장작은 알파벳
2. 카운트 알파벳 a 가장 큰거
'''