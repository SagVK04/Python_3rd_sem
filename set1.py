set1={10, True, 'Sagnik', 8.35}
set2={1, 2, 10, -10, 0, 53}
print(type(set2))
set3=set()
print(type(set3))
set1.add(99)
print(set1)
print(len(set1))
set1.remove('Sagnik')
print(set1)
print(len(set1))
set1.discard(True)
print(set1)
print(set1.pop())
print(set1)
set1.add((13,14,15))
print(set1)
#no order in sets
#all elements are unordered so indexing not possible
#we cannot update values inside sets
#we can change complete sets(Add, Remove)
#no duplicate elements inside it
#empty set is a dictionary
#list can't be added to the set as it is mutable
#sets use hashtable to store the items