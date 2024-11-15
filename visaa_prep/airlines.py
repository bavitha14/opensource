X,N = map(int,input().split())
cap = X*100
if cap>=N:
    print(0)
else:
    remaining = N-cap
    additional = (remaining+99)//100
    print(additional)
