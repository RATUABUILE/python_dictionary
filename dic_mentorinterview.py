# a=[1,2,3,4,5]
# b=['Apple','ball','cat','dog','flower']
# l={}
# i=0
# while i<len(a):
#     l[a[i]]=b[i]
#     i+=1
# print(l)

# d={'ap':[1,2,3],'pc':[4,5,6]}
# a={}
# for i in d:
#     s=0
#     for j in d[i]:
#         s=s+j
#     a[i]=[s]
# print(a)

# dic={1:'mango',2:'apple',3:'ball'}
# for i in dic:
#     for j in dic:
#         if dic[j]<dic[i]:
#             dic[j],dic[i]=dic[i],dic[j]
#         if dic[j]>dic[i]:
#             dic[i],dic[j]=dic[j],dic[i]
# print(dic)


# l=int(input("enter sl.no:"))
# m=input("enter name:")
# n=input("enter detials:")

# a="Humpty"
# print(len(a))

# a=567
# b=str(a)
# len= len(b)
# print(len)

# x=4
# y=5
# print(y)

# dic={}
# d1={}
# d={}
# i=0
# while i<3:
#     name=input("enter the name")
#     age=int(input("enter the age"))
#     hair=input("enter about hair")
#     skin=input("enter the colour")
#     d["age"]=age
#     d["hair"]=hair
#     d["skin"]=skin
#     d1[name]=d
#     dic[i+1]=d1
#     i=i+1
# print(dic)

# year=int(input("enter year to be checked"))  
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print("not leap year")

# i=1
# while i<=4:
#     j=4
#     while j>i:
#         print(" ",end=" ")
#         j-=1
#     a=1
#     while a<=j:
#         print("*",end=" ")
#         a+=1
#     print()
#     i+=1

# a=6%5**3//2+9/2
# print(a)

# def first():
#     def second():
#         i=1
#         sum=0
#         while i<=10:
#             sum=sum+1
#             i+=1
#         return sum+1
#     return second()
# print(first())

# def sum(a):
#     i=0
#     s=0
#     while i<len(a):
#         if type(a[i])==type([]):
#             j=0
#             while j<len(a[i]):
#                 s=s+a[i][j]
#                 j+=1
#         else:
#             s+=a[i]
#         i+=1
#     return s
# # [1,2,[3,4],5,6]
# print(sum([1,2,[3,4],5,6]))

a={"maths":82,"eng":70,"sci":90,"social":92}
l=[]
for i in a:
    l.append(a[i])
print(l)