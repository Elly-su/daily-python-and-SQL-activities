#still python datatypes
x = 1
y = 2.8
z = 1j

# Converting from int to float
a = float(x)

# Converting from float to int (will truncate decimal part)
b = int(y)

# Converting from int to complex
c = complex(x)

# Converting from float to complex
d = complex(y)

print("Float from int:", a)
print("Int from float:", b)
print("Complex from int:", c)
print("Complex from float:", d)

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))

#Random number
import random
print(random.randrange(1,10))
 
 
#looping through a string 
# The for loop automatically iterates over the characters in a string.
# Strings in Python are iterable, meaning they can be processed character by character.
# The print(x) function outputs each character on a new line because print() by default ends with a newline (\n).
for x in "banana":
    print(x)
    
#checking a string 
txt="The  best things in life are free"
print("free"in txt)

txt="The best things in life are free"
if "free" in txt:
    print("Yes,'free'is present.")
if "expensive" not in txt:
    print("'expensive' is not present.")
#still python datatypes
x = 1
y = 2.8
z = 1j

# Converting from int to float
a = float(x)

# Converting from float to int (will truncate decimal part)
b = int(y)

# Converting from int to complex
c = complex(x)

# Converting from float to complex
d = complex(y)

print("Float from int:", a)
print("Int from float:", b)
print("Complex from int:", c)
print("Complex from float:", d)

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))

#Random number
import random
random_number = random.randrange(1,10)
print("Random number between 1 and 10:", random_number)

#looping through a string 
# The for loop automatically iterates over the characters in a string.
# Strings in Python are iterable, meaning they can be processed character by character.
# The print(x) function outputs each character on a new line because print() by default ends with a newline (\n).
for char in "banana":
    print(char)
    
#checking a string 
txt="The  best things in life are free"
print("free" in txt)

txt="The best things in life are free"
if "free" in txt:
    print("Yes, 'free' is present.")
if "expensive" not in txt:
    print("'expensive' is not present.")