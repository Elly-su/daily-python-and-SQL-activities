#python slicing strings
b= ("Hello, world!")
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2]) #Negative indexing

#Modifying python strings
a = "Hello, World!"
print(a.upper())
print(a.lower())

#removing whitespaces in python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#replacing a string in python 
a = "Hello, World!"
print(a.replace("H", "J"))

#splitting a string in python
a = "Hello, World!"
print(a.split(",")) #  this is supposed to return ['Hello', ' World!']

#string concatenation
a = "Hello"
b = "World" 
c = a +" "+ b
print(c)
#fstrings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

price= 59
txt= f"The price is {price}"
print(txt)
txt =f"The price is {price:.2f}"
txt= f"It is very {'Expensive'if price > 50 else 'Cheap'}"
print(txt)
fruit = "banana"
txt= f"I love {fruit.upper()}!"
print(txt)

def myconverter(x):
    return x * 0.3048
txt =f"the plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 59000
txt = f"The price is {price:,}"
print(txt)

price = 49
txt = "The price is {} dollars "
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

