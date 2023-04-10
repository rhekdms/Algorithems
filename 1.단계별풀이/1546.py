import sys
input = sys.stdin.readline
N = int(input())
score = list(map(int,input().split()))
M = max(score)
print(sum(score) / M * 100 / N)