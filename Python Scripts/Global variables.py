x = "awesome"

def myfunc():
    """Modify the global variable x."""
    global x
    x = "fantastic"

def update_global():
    """Update the global variable y."""
    global y
    y = 20
    print(y)

myfunc()
print("Python is " + x)

y = 10
update_global()
print("Updated global variable y:", y)

#Python Datatypes
x=5
print(type(x))



