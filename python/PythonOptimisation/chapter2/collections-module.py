# Split a list in two lists separating positive numbers from negative ones
# Auteur : Sébastien Combéfis
# Version : October 11, 2020

from collections import deque
import timeit

REPEATS = 100

def split_numbers_1(data):
    result = []
    for d in data:
        if d < 0:
            result.insert(0, d)
        else:
            result.append(d)
    return result

def split_numbers_2(data):
    result = deque()
    for d in data:
        if d < 0:
            result.appendleft(d)
        else:
            result.append(d)
    return list(result)

def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(-50000, 50000))'
measure_time('split_numbers_1', params)
measure_time('split_numbers_2', params)
