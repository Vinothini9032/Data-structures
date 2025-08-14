row=3
col=3
matrix=[]
for i in range(row):
    arr=list(map(int,input().split()))
    matrix.append(arr)
target=int(input("Enter target: "))
l=0
r=col-1
while l<row and r>0:
    if matrix[l][r]==target:
        print(l,r)
        break
    elif matrix[l][r] > target:
        r-=1
    else:
        l+=1
