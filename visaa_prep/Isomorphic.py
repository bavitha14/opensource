n=int(input())
s1=input()
s2=input()
if len(s1)!=len(s2):
    print("false")
else:
    m1={}
    m2={}
    flag=1
    for i in range(0,len(s1)):
        if s1[i] in m1 and m1[s1[i]]!=s2[i]:
            flag=0
            break
        if s2[i] in m2 and m2[s2[i]]!=s1[i]:
            flag=0
            break
        m1[s1[i]]=s2[i]
        m2[s2[i]]=s1[i]
    if flag:
        print("true")
    else:
        print("false")
