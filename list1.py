lst1=[]
for i in range(0,5):
    a=int(input('Enter value:'))
    lst1.append(a)
print('Original list:',lst1)
sum=0
print('First index value:',lst1[0])
print('Last index value:',lst1[4])
for i in range(0,5):
    sum=sum+lst1[i]
print('Sum of the values:',sum)
lst1[2:5]=[11,22,33]
print('Modified list:',lst1)