t1=()
t2=()
t3=()
lst1=[]
lst2=[]
lst3=[]
n=int(input('Enter length of tuple:'))
for i in range(0,n):
    a=int(input('Enter +ve and -ve values alternatively:'))
    lst1.append(a)
t1=tuple(lst1)
print('Original tuple:',t1)
lst1=list(t1)
for i in range(0,len(lst1)):
    if(lst1[i]>=0):
        lst2.append(lst1[i])
    else:
        lst3.append(lst1[i])
t2=tuple(lst2)
t3=tuple(lst3)
print('Tuple with +ve values:',t2)
print('Tuples with -ve values:',t3)