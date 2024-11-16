st=input().strip()
count=1
ress=""
for i in range(1,len(st)+1):
    if i<len(st) and st[i]==st[i-1]:
        count+=1
    else:
        ress += st[i-1]+str(count)
        count=1
print(ress)
