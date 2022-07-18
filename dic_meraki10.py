dict={'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
s=0
for i,j in dict.items():
   s=s+len(j)
print(s)