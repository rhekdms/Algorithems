import sys
input = sys.stdin.readline
dice1 = list(map(int,input().split()))
dice2 = set(dice1)
if len(dice2) == 1:
    money = 10000 + sum(dice2) * 1000
elif len(dice2) == 2:
    money = 1000 + (sum(dice1) - sum(dice2)) * 100
else:
    money = max(dice1) * 100
print(money)