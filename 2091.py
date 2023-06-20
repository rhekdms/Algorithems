import sys
input = sys.stdin.readline
X,A,B,C,D = map(int,input().split())
cost = [[((X%25)%10)%5,((X%25)%10)//5,(X%25)//10,X//25]]

for a in range(cost[3],-1,-1):
    for 