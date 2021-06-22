# recursive function to count the number of items in a list 
"""
Description                    :  Defining a function to get the max from a list of integers using recursion technique
Function arguments/ input      :  A list of integers
Function return value/ output  :  Max of the list of integers
"""
def recursive_list_max(m_list):
    if len(m_list) < 3:
        if m_list[0] > m_list[1]:
            return m_list[0]
        else:
            return m_list[1]
    else:
        if m_list[-1] > m_list[-2]:
            max = m_list[-1]
        else:
            max = m_list[-2]        
        m_list.pop()
        m_list[-1] = max
        return recursive_list_max(m_list)

print(recursive_list_max([5, 3, 1, 2, 6, 4]))