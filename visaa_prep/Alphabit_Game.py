string=input()
vowel_c=0
consonant_c=0

for x in string:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="I" or x=="E" or x=="O" or x=="U" :
        vowel_c +=1
    elif x.isalpha():
        consonant_c +=1
print(f"{vowel_c},{consonant_c}")
