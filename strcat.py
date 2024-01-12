lst1=['Coll','O','Engi','an','Manage','Kola']
lst2=['ghat','ment','d','neering','f','ege']
lst3=[]
n=len(lst1)
for i in range(0,n):
    lst3.append(lst1[i]+lst2[n-1])
    n=n-1
print('Final list is:',lst3)