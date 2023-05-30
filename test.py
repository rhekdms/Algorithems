col,row = map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
for i in range(col):
    for j in range(row):
        if matrix[i][j] == '.':
            count = 0
            for k in range(i-1,i+2):
                for m in range(j-1,j+2):
                    if k < 0 or k > col or m < 0 or m > row:
                        continue
                    if matrix[k][m] == '*':
                        count += 1
            matrix[i][j] = count
print(matrix)