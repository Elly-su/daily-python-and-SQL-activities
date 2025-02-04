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