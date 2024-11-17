a=int(input())
array = list(map(int,input().split()))

if len(array) != a:
    print("false")
else:
    flag = 1
    for i in range(a-1):
        if array[i]>array[i+1]:
            flag= 0
        
    if flag:
        print("true")
    else:
        print("false")
