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