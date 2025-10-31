import sys
import time

def simple_hash(key, N):

    hash_value = 0
    for c in key:
        hash_value += ord(c) 

    return hash_value % N

def h_polynomial_rolling(key, N, p=53, m=2**64):
    s=0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    s=s%m
    return s % N

def get_words(file):
    words = []
    with open(file, 'r') as f:
        for line in f:
            words.append(line.strip())
    return words

def insert(L, hash_function, key, value):
    N = len(L)
    L[hash_function(key, N)].append((key, value))

def get(L, hash_function, key):

    N = len(L)
    hash_pos = hash_function(key, N)

    for hash_key, hash_value in L[hash_pos]:
        if hash_key == key:
            return hash_value

    return None

if len(sys.argv) != 4:
    print("Usage: python h.py <word_file> <table_size> <hash_type>")
    sys.exit(1)

word_file = sys.argv[1]
table_size = int(sys.argv[2])
hash_type = sys.argv[3]

hash_fuction = None
if hash_type == 'simple':
    hash_fuction = simple_hash
elif hash_type == 'polynomial':
    hash_fuction = h_polynomial_rolling

L = [ [] for i in range(table_size) ]

words = get_words(word_file)
value = 0
#start_time = time.time()
for key in words:
    #print('+', key, value)
    insert(L, hash_fuction, key, value)
    value+=1
#end_time = time.time()
#print('insert time', hash_type, end_time - start_time)

i = 0
for key in words:
    start_time = time.time()
    value = get(L, hash_fuction, key)
    #print('-', key, value)
    end_time = time.time()
    print(i, end_time - start_time)
    i+=1
    #print('get time', i, hash_type, end_time - start_time)


