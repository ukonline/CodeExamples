# Sorting a nearly sorted list
# Auteur : Sébastien Combéfis
# Version : October 11, 2020

import bisect
import timeit

REPEATS = 100

def insertion_sort(data):
    for i in range(1, len(data)):
        bisect.insort(data, data.pop(i), 0, i)

def quick_sort(data):
    data.sort()

def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '([x for x in range(1, 800)] + [0])'
measure_time('insertion_sort', params)
measure_time('quick_sort', params)
