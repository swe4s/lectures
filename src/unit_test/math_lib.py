def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def prod(a, b):
    return a * b

def div(a, b):
    return a / b

def file_add(file_name):
    f = open(file_name)
    s = 0
    for l in f:
        s += int(l)
    f.close()
    return s

def file_prod(file_name):
    f = open(file_name)
    s = 1
    for l in f:
        s *= int(l)
    f.close()
    return s
