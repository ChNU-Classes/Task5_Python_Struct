from src.sum_primes import sum_primes


def test_sum_primes1():
    assert sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 17


def test_sum_primes2():
    assert sum_primes([2, 3, 4, 11, 20, 50, 71]) == 87


def test_sum_primes3():
    assert sum_primes([4, 8, 20, 50, 70]) == 0


def test_sum_primes4():
    assert sum_primes([11, 11, 11, 11, 11, 22, 22, 22]) == 55


def test_sum_primes5():
    assert sum_primes([]) is None



