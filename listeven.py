lst=[]
count=0
for i in range(0,5):
    a=int(input('Enter a value:'))
    lst.append(a)
for i in range(0,5):
    if(lst[i]%2==0):
        count=count+1
        print(lst[i],end=' ')
        print()
print('No of even numbers:',count)