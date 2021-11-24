from functools import reduce
n=input("Enter: ")
num=list(map(int,n))      
s=reduce(lambda x,y:x+y,num)   
b=reduce(lambda x,y:x*y,num)
if(int(n)%s==0 and int(n)%b==0):
    print(1)
else:
    print(0)
