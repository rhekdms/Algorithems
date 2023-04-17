import sys
input = sys.stdin.readline
import math
A, B, V = map(int,input().split())
print(math.ceil((V-A)/(A-B))+1)
'''
A 올라감
B 미끄러짐
V 전체 올라가야 할 높이 
V-A <= (A-B)n
'''