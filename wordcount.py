n=input('Enter a sentence:')
count=1
for i in range(0,len(n)):
    if(n[i]==' '):
        count=count+1
    else:
        continue
print('No of words:',count)

