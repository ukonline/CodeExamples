# List creation with the filter predefined function
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

def filter_1(n):
    result = []
    for i in range(n):
        if i % 2 == 0 or i % 3 == 0:
            result.append(i)
    return result

def filter_2(n):
    data = filter(lambda i: i % 2 == 0 or i % 3 == 0, range(n))
    return list(data)

def filter_3(n):
    return [i for i in range(n) if i % 2 == 0 or i % 3 == 0]


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(1000000)'
measure_time('filter_1', params)
measure_time('filter_2', params)
measure_time('filter_3', params)
