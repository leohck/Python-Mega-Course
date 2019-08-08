#  Copyright (c)  7/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer


# myfile = open("fruits.txt")
# content = myfile.read()
# myfile.close()
# print(content)
#
# del content
# del myfile
#
# _file = open("files/bear.txt")
# content = _file.read()
# _file.close()
# print(content[:90])


# def charinfile(filepath, *args):
#     _file = open(filepath)
#     content = _file.read()
#     _file.close()
#     occurences = {}
#     for character in args:
#         occurences[character] = content.count(character)
#     return occurences
#
#
# print(charinfile('files/bear.txt', 'b', 'c'))

# with open("files/fruits.txt", 'r') as myfile:
#     content = myfile.read()
# print(content)

# with open("files/vegetables.txt", 'w') as myfile:
#     myfile.write("Tomato\nCucumber\nOnion\n")
#     myfile.write("Garlic")

# with open("files/vegetables.txt", 'w') as myfile:
#     myfile.write("Tomato\nCucumber\nOnion\n")
#     myfile.write("Garlic")

# with open("files/bear.txt", "r") as bearfile:
#     content = bearfile.read()[:90]
#
# with open("files/first.txt", "w") as first:
#     first.write(content)

# with open("files/candies.txt", "x") as candies:
#     candies.write("chocolate")
#
# with open("files/candies.txt", "a") as candies:
#     candies.write("\nicecream")

with open("files/data.txt", 'a+') as datafile:
    datafile.write('\n')
    datafile.seek(0)
    content = datafile.read()
    datafile.write(content*2)
