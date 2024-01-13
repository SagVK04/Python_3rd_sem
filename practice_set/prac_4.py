set1=set()
l1=[]
for i in range (0,5):
    n=input("Enter elements:")
    set1.add(n)
set1.add(input("Enter new element:"))
print("Length of the set:",len(set1))
print("New set:",set1)
l1=list(set1)
l=len(l1)
max=min=l1[0]
for i in range(0,l):
    if(l1[i]>max):
        max=l1[i]
for i in range(0,l):
    if(l1[i]<min):
        min=l1[i]
print("Max element is:",max)
print("Min element is:",min)
print("Removed third element:",l1[2])
l1.remove(l1[2])
set1=set(l1)
print("Modified set:",set1)
print("66 is present?:",'66' in set1)
set1.clear()
print(set1)