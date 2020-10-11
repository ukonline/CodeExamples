# Avoid exact code repetition
# Auteur : Sébastien Combéfis
# Version : October 10, 2020

import math
import timeit

REPEATS = 100

def circle_perimeter_1(data):
    result = []
    for r in data:
        result.append(2 * math.pi * r)
    return result

def circle_perimeter_2(data):
    result = []
    dp = 2 * math.pi
    for r in data:
        result.append(dp * r)
    return result


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(1000000))'
measure_time('circle_perimeter_1', params)
measure_time('circle_perimeter_2', params)
