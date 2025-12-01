# insertion sort

n_list = [23,98,56,10,5]

# external loop starting at one
for index in range(1, len(n_list)):
    # store the current item thats going to be inserted as 'current'
    current = n_list[index]

    index2 = index
    # internal loop starting at index
    while (index2 > 0 and current < n_list[index2-1]):
        # move the previous(?) item up 1 in the list and repeat this until the next item is less than current (or reach the end)
        n_list[index2] = n_list[index2-1]
        index2 -= 1
    # insert the item when the next item is less than it
    n_list[index2] = current

print(n_list)
