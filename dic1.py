from binascii import a2b_base64


r=[[1,'a','red'],[2,'b','black'],[3,'c','green']]
a={}
i=0
while i<len(r):
    j=0
    while j<len(r[i]):
        a[r[i][0]]=[r[i][1],r[i][2]]
        j+=1
    i+=1
print(a)