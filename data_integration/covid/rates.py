from operator import itemgetter
import re
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt

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

co_rates = []
for co in co_county_cases:
    co_pop = binary_search(co[1], co_county_pop)
    co_rates.append((co[0], co[1], int(co[2])/co_pop))

co_rates.sort(key=itemgetter(1))

last_co = None
dates = []
rates = []

fig = plt.figure(figsize=(10,3), dpi=300)
ax = fig.add_subplot(1,1,1)



for date, curr_co, rate  in co_rates:
    if curr_co == last_co:
        dates.append(datetime.strptime(date, '%Y-%m-%d'))
        rates.append(rate)
    else:
        if len(dates) > 0 and min(rates) > 0:
            ax.plot(dates, rates, lw=0.5)
            ax.text(dates[-1], rates[-1], last_co, size=5)

        dates = [datetime.strptime(date, '%Y-%m-%d')]
        rates = [rate]

    last_co = curr_co

plt.savefig('out.png', bbox_inches='tight')
