d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
a={}
for i,j in d1.items():
    if i in d2.keys():
        a[i]=d1[i]+d2[i]
    else:
        a[i]=d1[i]
for i,j in d2.items():
    if i not in d1.keys():
        a[i]=d2[i]
print(a)