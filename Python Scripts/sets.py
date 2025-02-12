myset = {"apple", "banana", "cherry"}
print(myset)
#sets are used to store mutiple items in a single variable
thissset = {"apple", "banana", "cherry"}
print(thissset)
#sets are unordered, so the items will appear in a random order
print(len(thissset))
print(type(thissset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
print("banana" in thisset)

#adding items in a set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

#joining sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
#Set methods
#set.add()
#set.clear()
#set.copy()
#set.difference()
#set.difference_update()
#set.disjoint()
#set.intersection()
#set.intersection_update()
#set.isdisjoint()
#set.issubset()
#set.issuperset()
#set.pop()
#set.remove()
#set.symmetric_difference()
#set.symmetric_difference_update()
#set.union()
#set.update()
#set() constructor
