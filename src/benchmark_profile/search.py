import random
import sys
import time

def linear_search(key, L):
    hit = -1
    for i  in range(len(L)):
        curr =  L[i]
        if key == curr:
            return i
    return -1

def binary_search(key, D):
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid]:
            return D[mid]

        if ( key < D[mid] ):
            hi = mid
        else:
            lo = mid

    return -1

def main():
    D_num = int(sys.argv[1])
    D = [random.randint(0,1000000) for x in range(D_num)]

    Q_num = int(sys.argv[2])
    Q = [D[random.randint(0,D_num - 1)] for x in range(Q_num)]

    op = sys.argv[3]

    if op == 'L':

        t0 = time.time() 
        for q in Q:
            linear_search(q, D)
        t1 = time.time()
        print(t1-t0)

    elif op == 'B':
        t0 = time.time() 

        t0_sort = time.time() 
        D.sort()
        t1_sort = time.time() 

        t0_search = time.time() 
        for q in Q:
            binary_search(q, D)
        t1_search = time.time() 

        t1 = time.time()
        print(t1-t0, (t1_sort-t0_sort)/(t1-t0), (t1_search-t0_search)/(t1-t0))

if __name__ == '__main__':
    main()
