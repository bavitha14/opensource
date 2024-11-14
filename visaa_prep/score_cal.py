t = int(input())
for _ in range(0,t):
    a,n= map(int,input().split())
    points=a//10
    score=n*points
    
    print(score)
