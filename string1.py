n=input('Enter your string:')
x=n.lower()
print('Uppercase:',x)
a=len(x)
y=n.upper()
print('Lowercase:',y)
count1=0
count2=0
count3=0
for i in range(0,a):
    if(x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u'):
        count1=count1+1
    elif(x[i]==' '):
        continue
    else:
        count2=count2+1
for j in range(0,a):
    if(x[j]=='i'):
        count3=count3+1
print('No of vowels:',count1)
print('No of consonants:',count2)
print('No of character i:',count3)