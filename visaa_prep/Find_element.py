n=int(input())
arr=list(map(int,input().split()))
k=int(input())

flag="0"
for i in range(0,len(arr)):
    if arr[i]==k:
        flag="1"
        print(i)
if flag=="0":
    print("-1")
