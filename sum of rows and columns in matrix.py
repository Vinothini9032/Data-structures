row=3
col=4
matrix=[]
for i in range(row):
    arr=list(map(int,input().split()))
    matrix.append(arr)
for i in range(row):
    row_sum=0
    for j in range(col):
        row_sum+=matrix[i][j]
    print(row_sum)
for j in range(col):
    col_sum=0
    for i in range(row):
        col_sum+=matrix[i][j]
    print(col_sum)