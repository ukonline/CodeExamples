# Evaluating a polynomial at a given x value
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

def polyval_1(coeff, data):
    result = []
    for i in range(len(data)):
        result.append(coeff[2]*data[i]**2 + coeff[1]*data[i] + coeff[0])
    return result

def polyval_2(coeff, data):
    result = []
    c, b, a = coeff
    for i in range(len(data)):
        x = data[i]
        result.append(a*x**2 + b*x + c)
    return result

def polyval_3(coeff, data):
    return [coeff[2]*x**2 + coeff[1]*x + coeff[0] for x in data]


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '([1, 1, 1], range(100000))'
measure_time('polyval_1', params)
measure_time('polyval_2', params)
measure_time('polyval_3', params)
