N,m = map(int,input().split())
array=list(map(int,input().split()))

num1= 0
num2= 0
for num in array:
    if num%m==0:
        num2+=num
    else:
        num1+=num
print(num2-num1)
