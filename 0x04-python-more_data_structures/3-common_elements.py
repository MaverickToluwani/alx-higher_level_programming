#!/usr/bin/python3
def common_elements(set_1, set_2):
    comm_ele = []
    for i in set_1:
        for j in set_2:
            if i == j:
                comm_ele.append(j)
    return comm_ele
