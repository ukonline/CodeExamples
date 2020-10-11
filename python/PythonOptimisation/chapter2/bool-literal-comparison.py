# Avoid comparisons with boolean literals
# Auteur : Sébastien Combéfis
# Version : October 10, 2020

import timeit

REPEATS = 100

def count_bool_1(data):
    result = 0
    for d in data:
        if d == True:
            result += 1
    return result

def count_bool_2(data):
    result = 0
    for d in data:
        if d:
            result += 1
    return result


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(x % 2 == 0 or x % 3 == 0 for x in range(1000000))'
measure_time('count_bool_1', params)
measure_time('count_bool_2', params)
