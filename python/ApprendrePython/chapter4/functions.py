# Programme d'affichage de tables de calcul
# Auteur : Sébastien Combéfis
# Version : 25 aout 2015

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def table(base, start=1, length=10, symbol="*", op=multiply):
    n = start
    while n < start + length:
        print(n, symbol, base, "=", op(n, base))
        n += 1

table(4, length=2)
table(4, length=2, symbol="+", op=add)
