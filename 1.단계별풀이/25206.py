import sys
input = sys.stdin.readline
N = 0
T = 0
for i in range(20):
    name, time, score = input().split()
    if score == 'A+':
        N = N + 4.5 * float(time)
        T += float(time)
    elif score == 'A0':
        N = N + 4.0 * float(time)
        T += float(time)
    elif score == 'B+':
        N = N + 3.5 * float(time)
        T += float(time)
    elif score == 'B0':
        N = N + 3.0 * float(time)
        T += float(time)
    elif score == 'C+':
        N = N + 2.5 * float(time)
        T += float(time)
    elif score == 'C0':
        N = N + 2.0 * float(time)
        T += float(time)
    elif score == 'D+':
        N = N + 1.5 * float(time)
        T += float(time)
    elif score == 'D0':
        N = N + 1.0 * float(time)
        T += float(time)
    elif score == 'F':
        T += float(time)
    else:
        pass
print(f'{N/T:0.6f}')