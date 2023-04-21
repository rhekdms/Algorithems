import sys

while True:
    _input = sys.stdin.readline()
    n = int(_input)
    if n == -1:
        break
    k = []
    for i in range(1, n):
        if n % i == 0:
            k.append(i)
    if n == sum(k):
        print(f"{n} = " + " + ".join(map(str, k)))
    else:
        print(f'{n} is NOT perfect.')