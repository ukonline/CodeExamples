# Concatenate strings with the format method of str objects
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

def format_1(n):
    result = ''
    for i in range(n):
        result += str(i) + ' x 10 = ' + str(i*10) + '\n'
    return result

def format_2(n):
    result = ''
    for i in range(n):
        result += '{} x 10 = {}\n'.format(i, i*10)
    return result

def format_3(n):
    result = ''
    for i in range(n):
        result += f'{i} x 10 = {i*10}\n'
    return result

def format_4(n):
    return ''.join([f'{i} x 10 = {i*10}\n' for i in range(n)])


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(100000)'
measure_time('format_1', params)
measure_time('format_2', params)
measure_time('format_3', params)
measure_time('format_4', params)
