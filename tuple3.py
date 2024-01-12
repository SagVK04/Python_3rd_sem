t1=(("A",7,8.96),("B",8,8.35),("C",45,8.59))
print('Original record:',t1)
lst1=list(t1)
r=int(input("Enter roll no. to modify:"))
n=len(lst1)
for i in range(0,n):
    lst2=list(lst1[i])
    if(lst2[1]==r):
        ch=int(input('1 to change name, 2 to change roll, 3 to change CGPA:'))
        if(ch==1):
            a=input('Enter new name:')
            lst2.insert(0,a)
            lst2.pop(1)
            lst1[i]=tuple(lst2)
        elif(ch==2):
            b=int(input('Enter new roll:'))
            lst2.insert(1,b)
            lst2.pop(2)
            lst1[i]=tuple(lst2)
        elif(ch==3):
            c=int(input('Enter new CGPA:'))
            lst2.insert(2,c)
            lst2.pop(3)
            lst1[i]=tuple(lst2)
        else:
            print('Enter valid choice!')
    else:
        lst1[i]=tuple(lst2)
t1=tuple(lst1)
print('Modified record:',t1)