import csv
f=open("namepassword.txt","r+")
n=input("Enter name:")
s=(input("Enter password: ")
for i in f:
    if(i.split(" ")[0]==n and i.split(" ")[1]==s):
        print("already having an account")
        break
else:
    f.write("\n")
    f.write(n)
    f.write(" ")
    f.write(s)
    print("account created successfully")
  
f.close()
