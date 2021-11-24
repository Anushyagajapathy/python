import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="@#$%^&*?~!"

all= lower + upper + numbers + symbols
length=8
n=str(input("Enter password:"))
if(len(n)>=8):
    password="".join(random.sample(all,length))
    print("Your password is saved")
else:
    print("Warning: password must as 8 variant with mix of letters (upper and lower case), numbers, and symbols, no ties to your personal information")


    
