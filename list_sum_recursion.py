"""
Description                    :  Defining a function to sum a list of integers using recursion technique
Function arguments/ input      :  A list of integers
Function return value/ output  :  Sum of the list of integers
"""
def rec_sum(s_list):
    if len(s_list) == 0:
        return 0
    elif len(s_list) == 1:
        return s_list[0]
    else:
        last_element = s_list.pop()
        return last_element + rec_sum(s_list)

print(rec_sum([1, 2, 3, 4, 5]))
