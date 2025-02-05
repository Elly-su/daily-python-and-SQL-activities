f= open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f= open("demofile.txt", "r")
print(f.read())
f.close()

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())

f = open("Myfile.txt", "x")
import os
os.remove("Myfile.txt")

import os
if os.path.exists("Myfile.txt"):
  os.remove("Myfile.txt")
else:
  print("The file does not exist")