# Lazy password checker from a file database with generators
# Author: Sébastien Combéfis
# Version: August 9, 2020

import hashlib

PASSWORD_FILE = 'passwords.txt'

def hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_1(identifier, password):
    with open(PASSWORD_FILE) as file:
        for line in file:
            s = line.strip().split(':')
            if s[0] == identifier and s[1] == hash(password):
                return True
    return False

def read_credentials(path):
    with open(path) as file:
        for line in file:
            yield tuple(line.strip().split(':'))

def login_2(identifier, password):
    for s in read_credentials(PASSWORD_FILE):
        if s[0] == identifier and s[1] == hash(password):
            return True
    return False


data = (
    ('combefis', 'password'),
    ('john', 'H9,m?2aB$d1'),
    ('john', 'H9,m?2aB$d2'),
    ('jane', 'azerty')
)

for credentials in data:
    print(login_2(*credentials))
