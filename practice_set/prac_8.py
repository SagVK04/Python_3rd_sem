t1=(("A",7,8.96),("B",8,8.35),("C",9,8.58))
print("Original Record:",t1)
l1=list(t1)
for i in range(0,len(l1)):
    l2=list(l1[i])
    if(l2[1]==int(input("Enter roll to check-in:"))):
        ch=int(input("1 to change name, 2 to change roll, 3 to change SGPA:"))
        if(ch==1):
            l2.insert(0,input("Enter new name:"))
            l2.pop(1)
            l1[i]=tuple(l2)
        elif(ch==2):
            l2.insert(1,int(input("Enter new roll:")))
            l2.pop(2)
            l1[i]=tuple(l2)
        elif(ch==3):
            l2.insert(2,float(input("Enter new SGPA:")))
            l2.pop(3)
            l1[i]=tuple(l2)
        else:
            print("Enter valid input!")
    else:
        print("Enter valid roll number!")
        l1[i]=tuple(l2)
t1=tuple(l1)
print("New record:",t1)       