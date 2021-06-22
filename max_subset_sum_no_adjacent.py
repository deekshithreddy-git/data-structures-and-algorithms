"""
Description                    :  Defining a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array.
Function arguments/ input      :  A list/array of integers
Function return value/ output  :  Max sum of non-adjacent elements in the array
"""
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
	curr_index = 2
	arr_length = len(array)
	if arr_length == 0:
		return 0
	elif arr_length == 1:
		return array[0]
	else:
		if array[0] > array[1]: 
			previous_max_sum = array[0]
			current_max_sum = array[0]
		else:
			previous_max_sum = array[0]
			current_max_sum = array[1]
		while curr_index < arr_length:
			if array[curr_index] + previous_max_sum > current_max_sum:
                previous_max_sum_stg = current_max_sum
                current_max_sum = array[curr_index] + previous_max_sum
                previous_max_sum = previous_max_sum_stg
				curr_index += 1
			else:
				previous_max_sum = current_max_sum
				curr_index += 1
	
		return current_max_sum