# Find the intersection between two lists
# Auteur : Sébastien Combéfis
# Version : October 11, 2020

import timeit

REPEATS = 100

def overlap_1(a, b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return result

def overlap_2(a, b):
    return list(set(a) & set(b))


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(100000), range(100000))'
measure_time('overlap_1', params)
measure_time('overlap_2', params)
