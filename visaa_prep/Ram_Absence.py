a=int(input().strip())
arr=list(map(int,input().split()))
maxs=0
current=0

for i in arr:
    if i==0:
        current +=1
    else:
        maxs=max(maxs,current)
        current=0
maxs=max(maxs,current)
print(maxs)
