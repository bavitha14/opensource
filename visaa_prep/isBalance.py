a=int(input())
array=list(map(int,input().split()))
B=[]
total=sum(array)
left=0
for i in range(0,a):
    
    right =total-left-array[i]
    B.append(abs(left-right))
    left+= array[i]
print(" ".join(map(str,B)))
