# recursive function to count the number of items in a list 
"""
Description                    :  Defining a function to count the list of integers using recursion technique
Function arguments/ input      :  A list of integers
Function return value/ output  :  Count of the list of integers
"""
def recursive_list_count(c_list):
    if c_list == []:
        return 0
    else:
        c_list.pop()
        return 1 + recursive_list_count(c_list)

print(recursive_list_count([1, 2, 3, 4, 5, 6]))