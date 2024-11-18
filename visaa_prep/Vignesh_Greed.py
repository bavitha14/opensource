a=int(input())
array= list(map(int,input().split()))

array.sort()
for i in range(a-1,1,-1):
    if (array[i-2] + array[i-1])>array[i]:
        print(array[i-2]+array[i-1]+array[i])
        
        break
else:
    print(-1)
    
