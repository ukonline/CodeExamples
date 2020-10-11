# Test whether all the boolean values from a list are True
# Auteur : Sébastien Combéfis
# Version : October 10, 2020

import timeit

REPEATS = 100

def all_1(data):
    for d in data:
        if not d:
            return False
    return True

def all_2(data):
    return all(data)


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(True for x in range(1000000))'
measure_time('all_1', params)
measure_time('all_2', params)
