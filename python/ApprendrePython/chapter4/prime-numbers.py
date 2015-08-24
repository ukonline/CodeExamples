# Programme d'affichage d'une séquence de nombres premiers
# Auteur : Sébastien Combéfis
# Version : 24 aout 2015

def isDivisor(d, n):
    return n % d == 0

def isPrime(n):
    d = 1
    nbDivisors = 0
    while d <= n:
        if isDivisor(d, n):
            nbDivisors += 1
        d += 1
    return nbDivisors == 2

def printPrimes(nb):
    n = 1
    while nb > 0:
        if isPrime(n):
            print(n)
            nb -= 1
        n += 1

printPrimes(10)