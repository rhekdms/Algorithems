n = int(input())
Q = [0]*4
AXIS = 0
for i in range(n):
    x, y = map(int,input().split())
    if x == 0 or y == 0:
        AXIS += 1
    elif x < 0 < y:
        Q[1] += 1
    elif x > 0 > y:
        Q[3] += 1
    elif x > 0:
        Q[0] += 1
    elif x < 0:
        Q[2] += 1
for i in range(4):
    print(f'Q{i+1}: {Q[i]}')
print(f'AXIS: {AXIS}')
'''
Q1: ++
Q2: -+
Q3: --
Q4: +-
AXIS: 0 or 0
'''