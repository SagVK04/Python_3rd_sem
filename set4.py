set1={}
set2={}
list1=[]
list2=[]
n1=int(input("Enter range of 1st list:"))
n2=int(input("Enter range of 2nd list:"))
for i in range(0,n1):
    list1.append(int(input("Enter value of 1st list:")))
for j in range(0,n2):
    list2.append(int(input("Enter value of 2nd list:")))
print(list1)
print("\n")
print(list2)
print("\n")
print("Missing in 2nd list:",set(list1).difference(list2))
print("Additioal in 2nd list:",set(list2).difference(list1))
