def probability(numbers_list, number):
    return round(sum(1 for n in numbers_list if n >= number) / len(numbers_list) * 100, 1)
