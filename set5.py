list1=[]
list2=[]
def common(n1,n2):
    print("Is there any common value?:")
    for j in range(0,n1):
        for k in range(0,n2):
            if(list1[i]==list2[j]):
                print("Yes!",list1[i])
                break
        
n1=int(input("Enter range of 1st list:"))
n2=int(input("Enter range of 2nd list:"))
for i in range(0,n1):
    list1.append(int(input("Enter value of 1st list:")))
for j in range(0,n2):
    list2.append(int(input("Enter value of 2nd list:")))
common(n1,n2)