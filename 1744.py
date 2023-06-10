import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

nums = deque(sorted(list(int(input()) for i in range(N))))
sol = 0

while len(nums)>1 and nums[1] < 1:
    a,b = nums.popleft(),nums.popleft()
    sol += a*b
    
while len(nums)>1 and nums[-2] > 1:
    a,b = nums.pop(),nums.pop()
    sol += a*b
print(sol+sum(nums))