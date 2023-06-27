import os
import shutil
f = open(file="test.txt", mode="w")
f.write("Shreyash")
f.close()

f = open(file="test.txt", mode="w")
f.write("This is my file")
f.close()

f = open(file="test.txt", mode="a")
f.write("\nAppend hogaya")
f.close()

f = open(file="test.txt", mode="r")
print(f.read())

f.seek(0)
"""Seek to set the pointer to the start in a file seek(0)
You can also set any index from where u want to start seek(11)"""
print(f.readline())
f.close()

f = open(file="test.txt", mode="r")
for i in f:
    print(i)
f.close()

print(os.path.getsize("test.txt"))

os.remove("test.txt")

f = open(file="test1.txt", mode="w")
f.write("DGHDHDJDH\nwhhslfhahfshfoi")
f.close()

"""Renaming"""
os.rename("test1.txt", "new.txt")

"""Making copy of file"""
shutil.copy("new.txt", "copy.txt")

with open("new.txt", "r") as f:
    print(f.read())
    