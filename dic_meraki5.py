list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
l={}
i=0
while i<len(list1):
    l[list1[i]]=list2[i]
    i+=1
print(l)