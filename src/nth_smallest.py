def nth_smallest(list_numbers, ind_num):
    if ind_num > len(list_numbers):
        return None
    else:
        return sorted(list_numbers)[ind_num - 1]