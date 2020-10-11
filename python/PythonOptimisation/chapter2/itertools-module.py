# Computing a cartesian product itertools.product
# Auteur : Sébastien Combéfis
# Version : October 11, 2020

from itertools import product
import timeit

REPEATS = 100

def pairs_1(a, b):
    return [(i, j) for i in a for j in b]

def pairs_2(a, b):
    return list(product(a, b))

def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(1000), range(1000))'
measure_time('pairs_1', params)
measure_time('pairs_2', params)
