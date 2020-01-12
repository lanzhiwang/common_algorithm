#!/usr/bin/env python3
"""
    module to operations with prime numbers
"""


def check_prime(number):
        """
            it's not the best solution

            number = 0 -> 2
            number = 1 -> 2
            number = 2 -> 3

            >>> number = 20
            >>> l1 = [i for i in range(2, number)]
            >>> l1
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
            >>> l2 = [number % i for i in l1]
            >>> l2
            [0, 2, 0, 0, 2, 6, 4, 2, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            >>> all(l2)
            False
            >>>
        """
        special_non_primes = [0,1,2]
        if number in special_non_primes[:2]:
            return 2
        elif number == special_non_primes[-1]:
            return 3
            
        return all([number % i for i in range(2, number)])


def next_prime(value, factor=1, **kwargs):
    value = factor * value  # 2 * 10
    first_value_val = value  # 10
    
    while not check_prime(value):
        value += 1 if not ("desc" in kwargs.keys() and kwargs["desc"] is True) else -1
    
    if value == first_value_val:
        return next_prime(value + 1, **kwargs)
    return value



if __name__ == '__main__':
    print(check_prime(0))  # 2
    print(check_prime(1))  # 2
    print(check_prime(2))  # 3
    print(check_prime(3))  # True
    print(check_prime(4))  # False
    print(check_prime(5))  # True
    print(check_prime(20))  # False

    print(next_prime(10, 2))  # 23
    