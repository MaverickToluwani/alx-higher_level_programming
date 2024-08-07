#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for elem in my_list:
            if count < x:
                print(elem, end="")
                count += 1
        print("")
    except Exception as error:
        print(error)
    return count
