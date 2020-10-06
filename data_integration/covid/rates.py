from operator import itemgetter
import re

covid_data='covid-19-data/us-counties.csv'
cencus_data='co-est2019-alldata.csv'

def linear_search(key, L):
    hit = -1
    for i  in range(len(L)):
        curr =  L[i]
        if key == curr[0]:
            return curr[1]
    return -1

def binary_search(key, D):
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == D[mid][0]:
            return D[mid][1]

        if ( key < D[mid][0] ):
            hi = mid
        else:
            lo = mid

    return -1


def get_columns(file_name,
                query_column,
                query_value,
                target_columns):

    f = open(file_name, 'r', encoding = "ISO-8859-1")

    header = f.readline()

    hits = []

    for l in f:
        A = l.rstrip().split(',')

        if A[query_column] == query_value:
            hit = []
            for target_column in target_columns:
                hit.append(A[target_column])
            hits.append(hit)

    return hits

co_county_cases = get_columns(covid_data, 2, 'Colorado', (0,1,4))
co_county_pop = get_columns(cencus_data, 5, 'Colorado', (6,7))
for co in co_county_pop:
    #co[0]  = co[0][:-7]
    co[0] = re.sub(' County', '', co[0])
    co[1]  = int(co[1])

co_county_pop.sort(key=itemgetter(0))

co_rate = []
for co in co_county_cases:
    co_pop = binary_search(co[1], co_county_pop)
    print(co, co_pop, int(co[2])/co_pop)
    co_rate.append((co[0], co[1], int(co[2])/co_pop))

co_rate.sort(key=itemgetter(2))

for co in co_rate:
    print(co)
