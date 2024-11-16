a= int(input())
arr=list(map(int,input().split()))

set_1=set()
res=[]
for n in arr:
    if n not in set_1:
        res.append(n)
        set_1.add(n)
print(' '.join(map(str,res)))
