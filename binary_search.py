"""
Description: Defining a function for binary search 
Function arguments: a sorted list of integers and a number to be searched from the list
Function return value: index of the searched number
"""
import math
def binary_search(num_list, num_to_be_searched):
    curr_left_most_index = 0
    curr_right_most_index = len(num_list) - 1

    while curr_left_most_index <= curr_right_most_index:
        curr_mid_index = math.floor((curr_left_most_index + curr_right_most_index) / 2)
        guessed_num = num_list[curr_mid_index]
        if guessed_num == num_to_be_searched:
            return f'Index of the number to be searched is: {curr_mid_index}'
        elif guessed_num < num_to_be_searched:
            curr_left_most_index = curr_mid_index + 1
        else:
            curr_right_most_index = curr_mid_index - 1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3))