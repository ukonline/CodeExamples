# Capitalising the first letter of every word in a sentence
# Author: Sébastien Combéfis
# Version: August 9, 2020

import timeit

REPEATS = 100

def wordcapital_1(s):
    result = []
    for w in s.split(' '):
        result.append(w.capitalize())
    return ' '.join(result)

def wordcapital_2(s):
    result = []
    append = result.append
    capitalize = str.capitalize
    for w in s.split(' '):
        append(capitalize(w))
    return ' '.join(result)


def measure_time(name, params):
    t = timeit.Timer(name + params, f'import random\nimport string\nfrom __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '(" ".join(["".join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 10))) for i in range(10000)]))'
measure_time('wordcapital_1', params)
measure_time('wordcapital_2', params)
