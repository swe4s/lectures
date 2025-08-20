import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out_file',
                        type=str,
                        help="Output file",
                        required=True)

    parser.add_argument('--cases',
                        type=str,
                        help="County case data",
                        required=True)

    parser.add_argument('--population',
                        type=str,
                        help="Population data",
                        required=True)

    parser.add_argument('--state',
                        type=str,
                        help="Target state",
                        required=True)

    parser.add_argument('--width',
                        type=float,
                        default=3.0,
                        help='Plot width (defult 3)')

    parser.add_argument('--height',
                        type=float,
                        default=3.0,
                        help='Plot height (defult 3)')

    return parser.parse_args()

def get_population_data(args):
    population  = {}
    for l in open(args.population, encoding='ISO-8859-1'):
        A = l.rstrip().split(',')

        state = A[5]

        if state != args.state:
            continue

        county = A[6]
        pop = int(A[7])

        population[county] = pop
    return population

def get_case_data(args):
    population = get_population_data(args)

    counties = {}
    dates = []

    for l in open(args.cases):
        A = l.rstrip().split(',')
        
        state = A[2]
        date = A[0]

        if state != args.state:
            continue

        if date not in dates:
            dates.append(date)

        county = A[1]
        cases = int(A[4])

        if county == 'Unknown':
            continue

        if county not in counties:
            counties[county] = {}

        counties[county][date] = cases/population[county + ' County']


    county_list = []
    county_matrix = []
    for county in counties:
        county_list.append(county)
        county_cases = []
        for date in dates:
            if date not in counties[county]:
                if len(county_cases) == 0:
                    county_cases.append(0)
                else:
                    county_cases.append(county_cases[-1])
            else:
                county_cases.append(counties[county][date])
        county_matrix.append(county_cases)

    return county_matrix, county_list, dates


def main():
    args = get_args()
    county_matrix, county_list, dates = get_case_data(args)

    fig = plt.figure(figsize=(args.width, args.height),dpi=300)

    ax = fig.add_subplot(1,1,1)

    im = ax.imshow(np.array(county_matrix),cmap='Reds')

    fig.colorbar(im)

    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.savefig(args.out_file,bbox_inches='tight')

if __name__ == '__main__':
    main()
