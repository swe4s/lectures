import sys
import hash_functions
import time
import random

def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val

class ChainHashTable:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [ [] for i in range(N) ]
        self.M = 0

    def insert(self, key, value):
        hash_slot = self.hash(key, self.N)
        self.T[hash_slot].append((key,value))
        self.M += 1
        return True

    def find(self, key):
        hash_slot = self.hash(key, self.N)

        for k,v in self.T[hash_slot]:
            if key == k:
                return v
        return None


class LPHashTable:
    def __init__(self, N, hash_method):
        self.hash = hash_method
        self.N = N
        self.T = [ None for i in range(N) ]
        self.M = 0

    def insert(self, key, value):
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def find(self, key):
        hash_slot = self.hash(key, self.N)

        for i in range(self.N):
            test_slot = (hash_slot + i) % self.N
            if self.T[test_slot] == None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None

if __name__ == '__main__':

    N = int(sys.argv[1])
    hash_alg = sys.argv[2]
    collision_strategy = sys.argv[3]
    data_file_name= sys.argv[4]
    keys_to_add = int(sys.argv[5])

    ht = None

    if hash_alg == 'ascii':

        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.h_ascii_sum)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_ascii_sum)

    elif hash_alg == 'rolling':

        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.h_polynomial_rolling)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_polynomial_rolling)

    elif hash_alg == 'python':
        if collision_strategy == 'linear':
            ht = LPHashTable(N, hash_functions.h_python)
        elif collision_strategy == 'chain':
            ht = ChainHashTable(N, hash_functions.h_python)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.insert(l, l)
        t1 = time.time()
        print('insert', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.find(v)
        t1 = time.time()
        print('search', ht.M/ht.N, t1 - t0)
