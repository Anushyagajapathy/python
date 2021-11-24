n=[10,5,4,5,3,2,1]
a=[]
for i in range(len(n)):
    for j in range(i+1,len(n)): 
        if(n[j]<n[i]):          
            a.append(n[j])
            break
    else:
        a.append(-1)
print(a)
