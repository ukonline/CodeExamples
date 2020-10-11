# Lazy and on demand generation with generators
# Auteur : Sébastien Combéfis
# Version : August 9, 2020

import timeit
import tracemalloc

REPEATS = 100

def gen_1(n):
    return [i for i in range(n)]

def gen_2(n):
    return (i for i in range(n))


def measure_time(name, params):
    t = timeit.Timer(name + params, f'from __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

def measure_memory(fct, params):
    tracemalloc.start()
    result = fct(*params)
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    
    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)

measure_time('gen_1', '(1000000)')
measure_memory(gen_1, (1000000,))

measure_time('gen_2', '(1000000)')
measure_memory(gen_2, (1000000,))
