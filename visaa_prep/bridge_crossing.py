a,b,c= map(int,input().split())
weight=c-b

if weight<=0:
    print(0)
else:
    max_mango=weight//a
    print(max_mango)
