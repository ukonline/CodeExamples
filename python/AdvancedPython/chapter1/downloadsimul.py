# Programme de simulation d'une progression de téléchargement
# Auteur : Sébastien Combéfis
# Version : 9 avril 2016

import random
import time

def downloadsimul():
    def printprogress(percent):
        progress = percent // 10
        print('\r{}{} ({}%)'.format('\u2588' * progress, '\u2591' * (10 - progress), percent), end='')
    progress = 0
    while progress < 100:
        progress = min(100, progress + random.randint(1, 20))
        printprogress(progress)
        time.sleep(1)

try:
    downloadsimul()
except KeyboardInterrupt:
    pass