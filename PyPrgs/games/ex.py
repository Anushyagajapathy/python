a="mango"
list=[]
for i in a:
    list.append('_ ')
print(*list)
def check():
    b=input("change: ")
    for i in range (len(a)):
        if (a[i]==b):
            list[i]=b
            print(*list)
for i in a:
    check()
