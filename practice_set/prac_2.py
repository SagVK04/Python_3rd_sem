def error(l1,n1):
    try:
        if(n1==5):
            l1[5]=l1[5]+l1[0]
        else:
            print(l1)
    except:
        print("Index out of range!")
    else:
        print("No error occured!")
l1=[]
l2=[]
n1=int(input("Enter range of list:"))
for i in range(0,n1):
    l1.append(int(input("Enter elements:")))
error(l1,n1)
n2=int(input("Enter range of list:"))
for i in range(0,n2):
    l2.append(int(input("Enter elements:")))
error(l2,n2)
