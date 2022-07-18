dict = {
 'a':50, 
 'b':58,
 'c': 56,
 'd':40,
 'e':100, 
 'f':20
 }
r=0
s=0
t=0
l=[]
for i in dict:
    for j in dict:
        if dict[j]>r:
            r=dict[j]
            a=j
        elif dict[j]>s and dict[j]<r:
            s=dict[j]
            b=j
        elif dict[j]>t and dict[j]<s:
            t=dict[j]
            c=j
l.append(a)
l.append(b)
l.append(c)
print(l)