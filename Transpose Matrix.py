'''Given a matrix mat, return its transpose.
Example:

lua
Copy
Edit
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]'''
row=3
col=3
matrix=[]
for i in range(row):
    arr=list(map(int,input().split()))
    matrix.append(arr)
print("orginal Matrix")
for i in matrix:
    print(i)
print("Transpose matrix")
transpose=[]
for i in range(col):
    rows=[]
    for j in range(row):
        rows.append(matrix[j][i])
    transpose.append(rows)
for i in transpose:
    print(i)
