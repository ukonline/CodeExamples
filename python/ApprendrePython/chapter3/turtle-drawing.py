# Programme de dessin d'une forme particulière
# Auteur : Sébastien Combéfis
# Version : 24 aout 2015

from turtle import *

MAX = 23
FACTOR = 1.2
len = 10
i = 0

while i < MAX:
    forward(len)
    left(90)
    i += 1
    len *= FACTOR

done()