file_name = 'covid-19-data/us-counties.csv'

f = open(file_name, 'r')

for l in f:
    A = l.rstrip().split(',')

    date = A[0]
    county_city = A[1]
    state = A[2]
    fips = A[3]
    cases = A[4]
    deaths = A[5]

    if state == 'Colorado' and county_city == 'Boulder':
        print(date, cases)

f.close()
