a=list(input("Enter a numbers: "))
for i in range(len(a)):
    for j in range(0,len(a)-1):
        if (a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            
        i=i+1
print(a)
print(a[0])
print(a[-1])
