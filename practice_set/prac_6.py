set1=set()
list1=[]
list2=[]
for i in range(0,5):
    set1.add(input("Enter elements:"))
print("Original set is:",set1)
list1=list(set1)
l=len(set1)
for i in range(l-1,-1,-1):
    list2.append(list1[i])
print("Reverse order:",list2)
print("First element:",list1[0])
print("Last element is:",list1[l-1])