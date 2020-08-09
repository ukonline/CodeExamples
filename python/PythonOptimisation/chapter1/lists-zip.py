# Iterating the numbers of two sequences to compute their sum
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

def vectorsum_1(x, y):
    return [x[i] + y[i] for i in range(len(x))]

def vectorsum_2(x, y):
    return [a + b for a, b in zip(x, y)]


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(100000), range(1, 100001))'
measure_time('vectorsum_1', params)
measure_time('vectorsum_2', params)
