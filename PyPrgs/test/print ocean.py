n= input("Enter: ")
for i in range(len(n)):
    for j in range (len(n)):
        if (i==j or j==4-i):
            print(n[j],end=' ')
        else:
            print("  ",end=' ')
    print(" ")   
