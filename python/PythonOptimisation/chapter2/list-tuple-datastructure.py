# Find the number of common elements between two sequences
# Auteur : Sébastien Combéfis
# Version : July 10, 2021

import timeit

REPEATS = 100

def common(a, b):
    result = set()
    for i in a:
        if i in b:
            result.add(i)
    return len(result)

def common_1(a, b):
    return common(list(a), list(b))

def common_2(a, b):
    return common(tuple(a), tuple(b))


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(list(range(5000)), list(range(5001, 1, -1)))'
measure_time('common_1', params)
measure_time('common_2', params)
