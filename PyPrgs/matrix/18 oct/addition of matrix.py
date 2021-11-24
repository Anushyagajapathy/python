z=[]
l=[[1,2],[3,4]]
l1=[[2,3],[4,5]]
for i in range(len(l)):
    z.append([])
    for j in range(len(l[0])):
        z[i].append(l[i][j]+l1[i][j])
print(z)


    
