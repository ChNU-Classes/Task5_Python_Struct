def pops(pop_list):
    ground_list = list(range(max(pop_list) + 1))
    return ground_list + ground_list[::-1][1:]