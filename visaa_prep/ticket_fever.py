t=int(input())
for i in range(0,t):
    a,b=map(int,input().strip().split())
    print(max(0,a-b))
