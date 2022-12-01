def sum_primes(list_numbers):
    return sum(filter(lambda x: 2 in [x, 2 ** x % x], list_numbers)) if list_numbers else None

