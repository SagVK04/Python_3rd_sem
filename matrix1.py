lst1=[]
a=int(input("Enter row numbers:"))
b=int(input("Enter column numbers:"))
print("Enter values:")
for i in range(0,a):
    lst2=[]
    for j in range(0,b):
        c=int(input())
        lst2.append(c)
    lst1.append(lst2)
print("Matrix is:")
for i in range(0,a):
    for j in range(0,b):
        print(lst1[i][j],end=' ')
    print()
