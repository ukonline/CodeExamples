# Counting the sum of the numbers in a list
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

i = 0

def sumelem_1(data):
    global i
    result = 0
    i = 0
    while i < len(data):
        result += data[i]
        i += 1
    return result

def sumelem_2(data):
    result = 0
    i = 0
    while i < len(data):
        result += data[i]
        i += 1
    return result


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(100000))'
measure_time('sumelem_1', params)
measure_time('sumelem_2', params)
