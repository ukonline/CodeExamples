# Avoid using unnecessary multiplications
# Auteur : Sébastien Combéfis
# Version : October 10, 2020

import timeit

REPEATS = 100

def gen10multiple_1(n):
    result = []
    for i in range(n):
        result.append(i * 10)
    return result

def gen10multiple_2(n):
    result = []
    for i in range(0, 10*n, 10):
        result.append(i)
    return result


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(1000000)'
measure_time('gen10multiple_1', params)
measure_time('gen10multiple_2', params)
