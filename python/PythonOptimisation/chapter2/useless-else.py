# Avoid useless else clause
# Auteur : Sébastien Combéfis
# Version : October 10, 2020

import timeit

REPEATS = 100

def abs_1(val):
    if val < 0:
        return -val
    else:
        return val

def abs_2(val):
    if val < 0:
        return -val
    return val

def absall_1(data):
    for d in data:
        abs_1(d)

def absall_2(data):
    for d in data:
        abs_2(d)


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(range(-500000, 500000))'
measure_time('absall_1', params)
measure_time('absall_2', params)
