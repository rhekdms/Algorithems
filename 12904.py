from collections import deque
S = list(input())
T = deque(input())
ab = 0
for i in range(len(T)-len(S)):
    if ab == 0:
        if T[-1] == 'B':
            ab = 1
        T.pop()
    else:
        if T[0] == 'B':
            ab = 0
        T.popleft()
if (list(T) == S and ab == 0) or (list(reversed(T)) == S and ab == 1):
    print(1)
else:
    print(0)