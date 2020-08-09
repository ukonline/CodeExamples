# Counting the frequency of letters in a word
# Author: Sébastien Combéfis
# Version: August 9, 2020

import collections
import timeit

REPEATS = 100

def frequencies_1(word):
    freq = {}
    for c in word:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    return freq

def frequencies_2(word):
    freq = {}
    for c in word:
        try:
            freq[c] += 1
        except KeyError:
            freq[c] = 1
    return freq


def measure_time(name, params):
    t = timeit.Timer(name + params, f'import random\nimport string\nfrom __main__ import {name}')
    print(t.timeit(REPEATS) / REPEATS * 1000)

params = '("".join(random.choice(string.ascii_lowercase) for i in range(100000)))'
measure_time('frequencies_1', params)
measure_time('frequencies_2', params)
