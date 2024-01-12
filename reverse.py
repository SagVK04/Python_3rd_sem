list1=[]
list2=[]
n=int(input('Enter length of string:'))
for i in range(0,n):
    a=input('Enter a word:')
    list1.append(a)
print('Original list:',list1)
for j in range(n-1,-1,-1):
    list2.append(list1[j])
print('Reversed list is:',list2)
