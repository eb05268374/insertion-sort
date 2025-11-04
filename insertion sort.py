# SORTING!

def recursive_selection_sort(lst, index=0):
    if index == len(lst) - 1:
        return lst # if finished return sorted lst

    # Find index of smallest element from index to end
    min_pos = index
    for i in range(index + 1, len(lst)):
        if lst[i] < lst[min_pos]: # < sorts smallest to greatest, > vise versa
            min_pos = i

    lst[index], lst[min_pos] = lst[min_pos], lst[index] # swapsies

    return recursive_selection_sort(lst, index + 1) # repeat for next index

import random
lst = [random.randint(0,1000) for _ in range(1000)]

print(recursive_selection_sort(lst))
