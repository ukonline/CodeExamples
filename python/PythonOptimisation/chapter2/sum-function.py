# Sum the values in a list with the sum predefined function
# Auteur : Sébastien Combéfis
# Version : October 10, 2020

import timeit

REPEATS = 100

def sumint_1(data):
    result = 0
    for d in data:
        result += d
    return result

def sumint_2(data):
    return sum(data)


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(1000000))'
measure_time('sumint_1', params)
measure_time('sumint_2', params)
