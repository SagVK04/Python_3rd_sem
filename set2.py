set1=set()
list1=[]
for i in range(0,5):
    n=int(input("Enter element:"))
    set1.add(n)
n1=int(input("Enter element to add:"))
set1.add(n1)
print("Original set:",set1)
print("Length of set:",len(set1))
list1=list(set1)
max=list1[0]
min=list1[0]
l=len(list1)
for i in range(0,l):
    if(list1[i]>max):
        max=list1[i]
for j in range(0,l):
    if(list1[i]<min):
        min=list1[j]
print("Max value:",max)
print("Min value:",min)
list1.remove(list1[2])
set1=set(list1)
print("Modified set:",set1)
print("Is 66 is present?:",'66' in set1)
print("After clearing:",set1.clear())