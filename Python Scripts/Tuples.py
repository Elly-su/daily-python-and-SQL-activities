#Tuples in python
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
 

x = ("apple", "banana", "cherry")#convert the tuple into a list to be able to change it
y = list(x) #convert the tuple into a list to be able to change it
y[1] = "kiwi"#change the second item
x = tuple(y)#convert the list back into a tuple

print(x)

thistuple = ("apple", "banana", "cherry")#add items
y = list(thistuple)#convert the tuple into a list to be able to change it
y.append("orange")#add an item
thistuple = tuple(y)#convert the list back into a tuple
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")#remove an item from a tuple by converting it into a list
thistuple = tuple(y)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)): #using the range() function to get the index numbers of the tuple
  print(thistuple[i])  