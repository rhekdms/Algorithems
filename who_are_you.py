T = int(input())
A = [tuple(map(int,input().split())) for i in range(T)]
A_sort = sorted(A)
print(A)
print(A_sort)