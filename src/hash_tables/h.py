import sys
import time


def h_ascii(key, N):
    total = 0
    for s in key:
        total += ord(s)
    return total % N

def h_rolling(key, N):
    total = 0
    i = 0
    p = 53
    for s in key:
        total += ord(s) * p**i
        i += 1
    return total % N

class LP:
    def __init__(self, N):
        self.N = N # size of table
        self.M = 0 # keys in table
        self.T = [ None for i in range(N) ]

    def add(self, key, value):
        start_at =  h_ascii(key, self.N)
        #start_at =  h_rolling(key, self.N)

        for i in range(self.N):
            hash_slot = (i + start_at)  % self.N
            if  self.T[hash_slot] == None:
                self.T[hash_slot] =  (key,value)
                self.M = self.M + 1
                break
    def search(self, key):
        #start_at =  h_ascii(key, self.N)
        start_at =  h_rolling(key, self.N)

        for i in range(self.N):
            hash_slot = (i + start_at)  % self.N
            if self.T[hash_slot] is None:
                return None # key is not in list
            if  key == self.T[hash_slot][0]:
                return self.T[hash_slot][1]
        # only if list is full and key is not in list
        return None 




file_name = sys.argv[1]
num_inserts = int(sys.argv[2])
N = 10000

ht = LP(N)
for  l in open(file_name):
    t0 = time.time()
    ht.add(l.rstrip(), l.rstrip())
    t1 = time.time()
    num_inserts -= 1
    if num_inserts == 0:
        break
    #print(ht.M/ht.N,t1-t0)

for i in range(100):
    t0 = time.time()
    print(ht.search('cyclistic'))
    t1 = time.time()
