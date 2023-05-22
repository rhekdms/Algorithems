N = int(input())
# 1
for i in range(N):
    print('*'*(i+1))

# 2
for i in range(N):
    print(' '*(N-i-1), '*'*(i+1), sep='')

# 3
for i in range(N):
    print('*'*(N-i))

# 4
for i in range(N):
    print(' '*i, '*'*(N-i), sep='')

# 5
for i in range(N):
    print(' '*(N-i-1), '*'*(2*i+1), sep='')

# 6
for i in range(N):
    print(' '*i, '*'*(2*(N-i)-1), sep='')

# 7
for i in range(2*N-1):
    if i < N:
        print(' '*(N-i-1), '*'*(2*i+1), sep=' ')
    else:
        print(' '*(i-N+2), '*'*(2*(2*N-i)-3), sep='')

# 8
for i in range(2*N-1):
    if i < N:
        print('*'*(i+1), ' '*(2*(N-i-1)), '*'*(i+1), sep='')
    else:
        print('*'*((2*N-1)-i), ' '*2*(i-N+1), '*'*((2*N-1)-i), sep='')

# 9
for i in range(2*N-1):
    if i < N:
        print(' '*i, '*'*(2*(N-i)-1), sep='')
    else:
        print(' '*(2*(N-1)-i), '*'*(2*(i-N)+3), sep='')

# 12
for i in range(2*N-1):
    if i < N:
        print(' '*(N-i-1), '*'*(i+1), sep='')
    else:
        print(' '*(i-N+1), '*'*(2*N-1-i), sep='')

# 13
for i in range(2*N-1):
    if i < N:
        print('*'*(i+1))
    else:
        print('*'*(2*N-i-1))

# 15
for i in range(N):
    if i == 0:
        print(' '*(N-1), '*', sep='')
    else:
        print(' '*(N-i-1), '*', ' '*(2*i-1), '*', sep='')

# 16
for i in range(N):
    print(' '*(N-i-1), '* '*(i+1), sep='')

# 17
for i in range(N):
    if i == 0:
        print(' '*(N-1), '*', sep='')
    elif i == N-1:
        print('*'*(2*N-1))
    else:
        print(' '*(N-i-1), '*', ' '*(2*i-1), '*', sep='')

# 20
for i in range(N):
    if i % 2 == 0:
        print('* '*N)
    else:
        print(' *'*N)

# 21
for i in range(2*N):
    for j in range(N):
        if i % 2 == 1 and j % 2 == 1 or i % 2 == 0 and j % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()