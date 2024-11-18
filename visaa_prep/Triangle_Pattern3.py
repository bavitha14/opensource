a = int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    print(" "*(2*(a-i)),end="")
    
    for j in range(i,0,-1):
        print(j,end="")
    print()
