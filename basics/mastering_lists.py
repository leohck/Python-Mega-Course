#  Copyright (c)  7/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer

monday_temperatures = [9.1, 8.8, 7.5]

# appending itens on the final ou list (colocar um valor no final da lista)
monday_temperatures.append(8.1)
print(monday_temperatures)

# return the position of an argument of list (returnar a posição de algum valor da list)
indexlist = monday_temperatures.index(8.1)
print(indexlist)

# remove item from a list (remover item da lista)
monday_temperatures.remove(8.1)

# access item
iten1 = monday_temperatures[0]
iten2 = monday_temperatures.__getitem__(1)

# accessing itens by slice
itens = monday_temperatures[0:2]
print(itens)

# clean list ( apagar tudo)
monday_temperatures.clear()


# Lists, strings, and tuples have a positive index system:

days_pos_rank = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# 0      1      2      3      4      5      6

# And a negative index system:

days_neg_rank = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# -7     -6     -5     -4     -3     -2     -1

# In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[1:4])


# First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[:3])

# Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[-3:])

# Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[:-1])

# Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[:-2])

# A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
print(phone_numbers["Marry Simpsons"])
Output: '+423998200919'
