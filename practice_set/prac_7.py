t1=()
l1=[]
for i in range(0,5):
    l1.append(int(input("Enter value:")))
print("The tuple is:",tuple(l1))
t1=tuple(l1)
t1=t1+(int(input("Enter an value to add:")),)
print("Modified tuple is:",t1)
l1=list(t1)
l1.insert(int(input("Enter position from 0:")),int(input("Enter value to add:")))
print("Modified tuple is:",tuple(l1))
p=int(input("Enter position to delete:"))
for i in range(0,len(l1)):
    if(i==(p-1)):
        l1.remove(l1[i])
print("Modified tuple:",tuple(l1))
val=int(input("Enter a data to count:"))
count=tuple(l1).count(val)
if(count==1):
    print("%d is not repeated"%val)
else:
    print("%d is repeated %d times"%(val,count))
d=int(input("Enter an item to check:"))
print(d in tuple(l1))