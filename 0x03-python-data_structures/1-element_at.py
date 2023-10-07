#!/usr/bin/python3
def element_at(my_list, idx):
    byte = int(len(my_list))
    if idx < 0 or idx > byte:
        return None
    for count in range(byte):
        if count == idx:
            return my_list[count]
