#  Copyright (c)  7/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer

myfile = open("fruits.txt")
content = myfile.read()
myfile.close()
print(content)

del content
del myfile

_file = open("bear.txt")
content = _file.read()
_file.close()
print(content[:90])
