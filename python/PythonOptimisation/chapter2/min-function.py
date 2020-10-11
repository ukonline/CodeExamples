# Find the minimal value from a list
# Auteur : Sébastien Combéfis
# Version : October 10, 2020

import timeit

REPEATS = 100

def min_1(data):
    result = data[0]
    for d in data:
        if d < result:
            result = d
    return result

def min_2(data):
    return min(data)


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(1000000))'
measure_time('min_1', params)
measure_time('min_2', params)
