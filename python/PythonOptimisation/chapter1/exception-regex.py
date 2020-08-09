# Counting the sum of the integers in a list of strings
# Author: Sébastien Combéfis
# Version: August 9, 2020

import re
import timeit

REPEATS = 100

def sumtextint_1(data):
    result = []
    for d in data:
        if re.match('^[1-9][0-9]*$', d):
            result.append(int(d))
    return sum(result)

def sumtextint_2(data):
    result = []
    for d in data:
        try:
            result.append(int(d))
        except ValueError:
            pass
    return sum(result)


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '([str(i) for i in range(100000)])'
measure_time('sumtextint_1', params)
measure_time('sumtextint_2', params)
