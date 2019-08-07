#  Copyright (c)  7/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer


def sums(*args):
    return sum(args)


print(sums(1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 5, 4, 2, 6, 4, 4, 2, 7, 8, 9, 5, 6, 3, 2, 1, 4, 5, 2, 3, 8, 4))


def average(*args):
    return sum(args) / len(args)


print(average(10, 20, 30, 40))


def sortandupperlist(*args):
    return sorted([x.upper() for x in args])


print(sortandupperlist("snow", "glacie", "iceberg"))


def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=1, b=1, c=3, d=4))
