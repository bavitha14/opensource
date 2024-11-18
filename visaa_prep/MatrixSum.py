n=int(input())
mat =[list(map(int,input().split()))
for _ in range(n)]

row_sum=[]
for i in range(n):
    row_sum.append(sum(mat[i]))
    
column_sum=[]
for j in range(n):
    sum=0
    for i in range(n):
        sum+= mat[i][j]
    column_sum.append(sum)

res=[]
for i in range(n):
    res.append(row_sum[i]+column_sum[i])

print(*res)
