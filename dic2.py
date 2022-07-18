d={"v":[10,5,20],"v1":[25,30,32],"v2":[24,1,3]}
for i in d:
    x=d[i]
    j=0
    b=[]
    while j<len(x):
        if x[j]%2==0:
            b.append(x[j])
        j+=1
    d[i]=b
print(d)