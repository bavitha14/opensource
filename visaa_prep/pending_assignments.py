a,b,x=map(int,input().split())
time= a*b
available= x*1440
if time <=available:
    print("YES")
else:
    print("NO")
