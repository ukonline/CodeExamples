# Iterating the numbers of a sequence to compute their square
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

def square_1(x):
    s = ''
    i = 0
    while i < len(x):
        s += f'{i}: {x[i]**2}\n'
        i += 1
    return s[:-1]

def square_2(x):
    s = ''
    for i in range(len(x)):
        s += f'{i}: {x[i]**2}\n'
    return s[:-1]

def square_3(x):
    s = ''
    for i, e in enumerate(x):
        s += f'{i}: {e**2}\n'
    return s[:-1]

def square_4(x):
    return '\n'.join([f'{i}: {e**2}' for i, e in enumerate(x)])


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(100000))'
measure_time('square_1', params)
measure_time('square_2', params)
measure_time('square_3', params)
measure_time('square_4', params)
