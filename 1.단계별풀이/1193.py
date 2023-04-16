import sys
input = sys.stdin.readline
X = int(input())
k = 1
j = 2
i = 0
for x in range(X):
    i += 1
    j -= 1
    if j == 0:
        i = 1
        k += 1
        j = k
if k % 2 == 0:
    print(f'{i}/{j}')
else:
    print(f'{j}/{i}')

'''
k 는 1
j 는 2
i 는 0
i 는 증가
j 는 감소
j 가 0이 되면 i는 1,k 는 1 증가, j는 k
왜 런타임 에러!!!!! 왜!!!!! 왜!!!!!!!!!!!!!
'''