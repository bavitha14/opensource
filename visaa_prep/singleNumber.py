a=int(input())
arr=list(map(int,input().split()))
list={}
for n in arr:
    if n in list:
        list[n]+=1
    else:
        list[n]=1
for n in list:
    if list[n]==1:
        print(n)
        break
