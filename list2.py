lst1=[]
n=int(input("enter no of elements in list"))
for l in range(0,n):
    new=int(input())
    lst1.append(new)
k=int(input("enter element you want to replace with" ))
for i in range(0,n):
    for j in range(i+1,n):
        if lst1[j]==lst1[i] and lst1[j]!=k:
            lst1[j]=k
print(lst1)
