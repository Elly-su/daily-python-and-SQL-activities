thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(type(list1), type(list2), type(list3))

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
  #changing Item values in lists
  thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist.append("grapes")
print(thislist)

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)  
print(thislist)

thislist.remove("banana")
print(thislist)

thislist1 = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist1)

del thislist1[0]
print(thislist1)

thislist1.clear()
print(thislist1)

for x in thislist:
  print(x)
  
  for i in range (len(thislist)):
    print(thislist[i])
    i = 0
    while i < len(thislist):
      print(thislist[i])
      i = i + 1
      
      [print(x) for x in thislist]
      fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
      newlist = []
      for x in fruits:
        if "a" in x:
          newlist.append(x)
        
        print(newlist)
        
        newlist = [x for x in fruits if "a" in x]
        print(newlist)
      



