l=[]
l1=[]
def error(l,n):
    try:
        if(n==4):
            l[4]=l[4]+1
    except:
        print("Index error!")
    else:
        print("No error!")
n=int(input("Enter range of list:"))
for i in range(0,n):
    l.append(int(input("Enter value:")))
error(l,n)
n1=int(input("Enter range of list:"))
for i in range(0,n1):
    l1.append(int(input("Enter value:")))
error(l1,n1)