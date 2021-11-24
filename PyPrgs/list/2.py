s=input("Enter: ")
for i in range (len(s)):   
    if(i==len(s)//2):
        print(s[i-1],end='')
        print(s[i],end='')
        print(s[i+1])

    
