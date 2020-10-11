# Computing the nth Fibonacci number with functools.lru_cache
# Auteur : Sébastien Combéfis
# Version : October 11, 2020

from functools import lru_cache
import timeit

REPEATS = 100

def fib_1(n):
    if n <= 1:
        return n
    return fib_1(n - 1) + fib_1(n - 2)

@lru_cache(maxsize=128)
def fib_2(n):
    if n <= 1:
        return n
    return fib_2(n - 1) + fib_2(n - 2)

def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(25)'
measure_time('fib_1', params)
measure_time('fib_2', params)
