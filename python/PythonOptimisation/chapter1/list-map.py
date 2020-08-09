# List creation with the map predefined function
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

def map_1(n):
    result = []
    for i in range(n):
        result.append(2 ** i)
    return result

def map_2(n):
    data = map(lambda i: 2**i, range(n))
    return list(data)

def map_3(n):
    return [2**i for i in range(n)]


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(10000)'
measure_time('map_1', params)
measure_time('map_2', params)
measure_time('map_3', params)
