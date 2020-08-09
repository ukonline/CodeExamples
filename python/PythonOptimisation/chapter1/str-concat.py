# Concatenate strings with the join method of str objects
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

def concat_1(n):
    result = ''
    for i in range(n):
        result += 'Nom'
    return result

def concat_2(n):
    result = []
    for i in range(n):
        result.append('Nom')
    return ''.join(result)

def concat_3(n):
    return ''.join(['Nom' for i in range(n)])


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(1000000)'
measure_time('concat_1', params)
measure_time('concat_2', params)
measure_time('concat_3', params)
