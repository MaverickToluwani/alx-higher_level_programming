#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == [] or my_list is None:
        return
    for ele in my_list[::-1]:
        print("{:d}".format(ele))
