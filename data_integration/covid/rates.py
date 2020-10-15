from operator import itemgetter
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

def plot_lines(points, labels, file_name):
    """Take a list of list of points and plot each list as a line.

        Parameters
        ----------
        points    : list of list of points
                    Each sublist corresponds to the points for one element.
                    Each point has two values, the first will be the X value
                    and the second the Y value
        labels    : list of strings
                    Each element in lables corresponds to the sublist at the
                    same poisiting in data
        file_name : string
                    Name of the output file.
    """
    fig = plt.figure(figsize=(10,3), dpi=300)
    ax = fig.add_subplot(1,1,1)

    i = 0
    for pairs in points:
        X = []
        Y = []
        for pair in pairs:
            X.append(pair[0])
            Y.append(pair[1])

        ax.plot(X, Y, lw=0.5)
        ax.text(X[-1], Y[-1], labels[i], size=5)

        i += 1

    plt.savefig(file_name, bbox_inches='tight')


co_county_cases = get_columns(covid_data, 2, 'Colorado', (0,1,4))
co_county_pop = get_columns(cencus_data, 5, 'Colorado', (6,7))
for co in co_county_pop:
    co[0]  = co[0][:-7]
    co[1]  = int(co[1])

co_county_pop.sort(key=itemgetter(0))

co_rates = []
for co in co_county_cases:
    if co[1] == 'Unknown':
        continue
    co_pop = binary_search(co[1], co_county_pop)
    co_rates.append((co[0], co[1], int(co[2])/co_pop))

co_rates.sort(key=itemgetter(1))

last_co = None
curr_points = []
points = []
labels = []
for date, curr_co, rate  in co_rates:
    if curr_co == last_co:
        curr_points.append( [datetime.strptime(date, '%Y-%m-%d'), rate ] )
    else:
        if len(curr_points) > 0:
            points.append(curr_points)
            labels.append(last_co)

        curr_points = [ [datetime.strptime(date, '%Y-%m-%d'), rate ] ]

    last_co = curr_co

curr_points.append( [datetime.strptime(date, '%Y-%m-%d'), rate ] )
points.append(curr_points)
labels.append(last_co)

plot_lines(points, labels, 'test.png')
