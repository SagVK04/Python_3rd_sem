a=(input('Enter values using space:'))
b=a.split(" ")
print(b)
c=len(b)
sum=0
for i in range(0,c):
    sum=sum+int(b[i])
print('Sum of the list is:',sum)