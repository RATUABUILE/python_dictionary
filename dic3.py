d={'a':107,'b':40,'c':100,'d':10,'e':99,'f':104}
a={}
for i in d:
    if d[i]>=100:
        a[i]=d[i]
a.update(a)
print(a)