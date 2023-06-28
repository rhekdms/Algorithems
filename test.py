from collections import deque

n, l = map(int, input().split())
arr = [*map(int, input().split())]
m = deque()
for i in range(n):
    tmp = arr[i]
    print('tmp',tmp)
    while m and m[-1] > tmp:
        m.pop()
        print('m',m)
    m.append(tmp)
    print('m2',m)
    #윈도우 크기보다 커진 단계에서 arr와 비교한 후 left pop
    if i >= l and m[0] == arr[i - l]: 
        m.popleft()
        print('m3',m)
    print('sol',m[0])